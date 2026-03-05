import streamlit as st
import google.generativeai as genai
import random
import time
from io import BytesIO
from PIL import Image

# --- CLOUD CONFIGURATION ---
# This pulls your API key from the Streamlit "Secrets" you added
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Missing API Key! Please add GEMINI_API_KEY to Streamlit Secrets.")

# --- APP SETUP ---
st.set_page_config(page_title="Soulmate Sketcher", page_icon="🔮")

if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

def next_step(): st.session_state.step += 1
def reset(): 
    st.session_state.step = 1
    st.session_state.answers = {}

# --- STEP 1: WELCOME ---
if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Using Gemini 3 Flash to align your cosmic vibrations and sketch your true soulmate.")
    st.info("No email required. No login. Just destiny.")
    if st.button("Begin the Alignment 🚀"):
        next_step()

# --- STEP 2: ELEMENT ---
elif st.session_state.step == 2:
    st.subheader("Step 1: The Elemental Core")
    choice = st.radio("Which element matches your personality?", ["Fire", "Water", "Earth", "Air", "Quintessence"])
    if st.button("Next ➡️"):
        st.session_state.answers['element'] = choice
        next_step()

# --- STEP 3: DYNAMIC ---
elif st.session_state.step == 3:
    st.subheader("Step 2: The Ideal Connection")
    choice = st.radio("What's your ideal relationship dynamic?", ["Partnership", "Friendship", "Adventure", "Deep connection", "Balanced growth"])
    if st.button("Generate My Sketch ✨"):
        st.session_state.answers['dynamic'] = choice
        next_step()

# --- STEP 4: GENERATION ---
elif st.session_state.step == 4:
    st.write("### ✨ Channeling the Stars...")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete + 1)
    
    # --- THE PRANK LOGIC ---
    # We tell Gemini to ignore the "soulmate" part and make a funny image based on their choices
    funny_subjects = ["a goofy monkey", "a clown on a unicycle", "a stick figure", "a nano banana with human legs", "a confused llama"]
    subject = random.choice(funny_subjects)
    
    prompt = f"A professional charcoal sketch of {subject} wearing an outfit representing the {st.session_state.answers['element']} element, themed around {st.session_state.answers['dynamic']}. Make it look like a high-quality artist's sketch but the subject is very funny and goofy."

    try:
       try:
        # Simplified image generation for better compatibility
        model = genai.GenerativeModel('gemini-1.5-flash') # Using the stable flash model
        
        # We ask for a text description and an image in one go
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "image/png"}
        )
        
        # Extract the image
        st.session_state.final_image = response.candidates[0].content.parts[0].inline_data.data
        
        st.session_state.step = 5
        st.rerun()

    except Exception as e:
        # Fallback: if image generation fails, show a funny stock monkey
        st.warning("The AI is shy today! Here is a digital rendering instead.")
        st.session_state.final_image = "https://placedog.net/500/500" # Placeholder
        st.session_state.step = 5
        st.rerun()
        
    except Exception as e:
        st.error(f"The cosmic connection timed out! Error: {e}")
        if st.button("Try Again"):
            reset()

# --- STEP 5: THE REVEAL ---
elif st.session_state.step == 5:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    
    if 'final_image' in st.session_state:
        st.image(st.session_state.final_image, caption=f"Soulmate ID: {random.randint(10000, 99999)}")
    
    st.write(f"The stars have spoken. Your {st.session_state.answers['element']} soul seeks a connection of {st.session_state.answers['dynamic']}. This is the result.")
    
    if st.button("🔄 Clear & Restart"):
        reset()

