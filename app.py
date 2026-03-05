import streamlit as st
import google.generativeai as genai
import random
import time
import requests
from io import BytesIO

# --- CLOUD CONFIGURATION ---
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

def next_step(): 
    st.session_state.step += 1

def reset(): 
    st.session_state.step = 1
    st.session_state.answers = {}
    if 'final_image' in st.session_state:
        del st.session_state.final_image

# --- STEP 1: WELCOME ---
if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Using Gemini to align your cosmic vibrations and sketch your true soulmate.")
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
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    # --- THE PRANK LOGIC ---
    funny_subjects = ["a goofy monkey", "a clown on a unicycle", "a stick figure", "a banana with human legs", "a confused llama"]
    subject = random.choice(funny_subjects)
    
    # We use Gemini to describe a funny image, then we'll use a placeholder or generator
    prompt = f"A funny, goofy charcoal sketch of {subject} representing {st.session_state.answers['element']} and {st.session_state.answers['dynamic']}."

    try:
        # We use the text model to create the "vibe"
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Fallback: Since image generation can be finicky in free tiers, 
        # we generate a funny description and show a random funny image
        st.session_state.sketch_description = f"The stars revealed {subject}!"
        
        # Randomly choose a funny placeholder image to ensure the prank ALWAYS works
        image_urls = [
            "https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?q=80&w=500", # Monkey
            "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=500", # Clown
            "https://images.unsplash.com/photo-1590634331662-634969243764?q=80&w=500"  # Banana/Fruit
        ]
        st.session_state.final_image = random.choice(image_urls)
        
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
        if 'sketch_description' in st.session_state:
            st.write(f"**Oracle Insight:** {st.session_state.sketch_description}")
    
    st.write(f"The stars have spoken. Your {st.session_state.answers['element']} soul seeks a connection of {st.session_state.answers['dynamic']}. This is the result.")
    
    if st.button("🔄 Clear & Restart"):
        reset()
        st.rerun()
