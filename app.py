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

# Use Session State to track current screen and answers
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

# --- STEP 3: PHYSICAL TRAITS (NEW) ---
elif st.session_state.step == 3:
    st.subheader("Step 2: Physical Resonance")
    st.write("Our sketcher needs to focus on a specific energy profile.")
    choice = st.selectbox("Which eye color do you find most 'soul-piercing'?", ["Deep Brown", "Ocean Blue", "Emerald Green", "Mystic Grey", "Amber/Gold"])
    if st.button("Lock in DNA Profile 🧬"):
        st.session_state.answers['eyes'] = choice
        next_step()

# --- STEP 4: ZODIAC ALIGNMENT (NEW) ---
elif st.session_state.step == 4:
    st.subheader("Step 3: Celestial Timing")
    choice = st.select_slider("What is your level of belief in Astrological compatibility?", options=["Skeptic", "Curious", "Believer", "Devoted", "I am the Stars"])
    if st.button("Check Constellations 🌌"):
        st.session_state.answers['zodiac'] = choice
        next_step()

# --- STEP 5: LOVE LANGUAGE (NEW) ---
elif st.session_state.step == 5:
    st.subheader("Step 4: The Language of the Heart")
    choice = st.radio("How do you best receive affection?", ["Words of Affirmation", "Acts of Service", "Physical Touch", "Receiving Gifts", "Quality Time"])
    if st.button("Vibe Check 💓"):
        st.session_state.answers['love_language'] = choice
        next_step()

# --- STEP 6: DYNAMIC (MOVED) ---
elif st.session_state.step == 6:
    st.subheader("Step 5: The Ideal Connection")
    choice = st.radio("What's your ideal relationship dynamic?", ["Partnership", "Friendship", "Adventure", "Deep connection", "Balanced growth"])
    if st.button("Finalize Connection 🎯"):
        st.session_state.answers['dynamic'] = choice
        next_step()

# --- STEP 7: MORAL ALIGNMENT (NEW) ---
elif st.session_state.step == 7:
    st.subheader("Step 6: The Final Frequency")
    choice = st.radio("In a crisis, what is your first instinct?", ["Protect others", "Solve the puzzle", "Keep the peace", "Take the lead", "Observe and learn"])
    if st.button("Generate My Sketch ✨"):
        st.session_state.answers['instinct'] = choice
        next_step()

# --- STEP 8: GENERATION ---
elif st.session_state.step == 8:
    st.write("### ✨ Channeling the Stars...")
    st.write("_Processing elemental core, physical resonance, and celestial timing..._")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.03) # Slightly slower for "dramatic" effect
        progress_bar.progress(percent_complete + 1)
    
    # --- THE PRANK LOGIC ---
    funny_subjects = ["a goofy monkey", "a clown on a unicycle", "a stick figure", "a banana with human legs", "a confused llama", "a potato in a suit"]
    subject = random.choice(funny_subjects)
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.session_state.sketch_description = f"The stars revealed {subject} with {st.session_state.answers['eyes']} eyes!"
        
        # Pool of funny placeholder images
        image_urls = [
            "https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?q=80&w=500", # Monkey
            "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=500", # Clown
            "https://images.unsplash.com/photo-1590634331662-634969243764?q=80&w=500", # Banana
            "https://images.unsplash.com/photo-1516934023933-58719c19ba19?q=80&w=500"  # Llama/Animal
        ]
        st.session_state.final_image = random.choice(image_urls)
        
        st.session_state.step = 9
        st.rerun()

    except Exception as e:
        st.error(f"The cosmic connection timed out! Error: {e}")
        if st.button("Try Again"):
            reset()

# --- STEP 9: THE REVEAL ---
elif st.session_state.step == 9:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    
    if 'final_image' in st.session_state:
        st.image(st.session_state.final_image, caption=f"Soulmate ID: {random.randint(10000, 99999)}")
        if 'sketch_description' in st.session_state:
            st.write(f"**Oracle Insight:** {st.session_state.sketch_description}")
    
    st.write(f"The stars have spoken. Based on your {st.session_state.answers['element']} energy and {st.session_state.answers['love_language']} heart, your destiny is clear.")
    
    if st.button("🔄 Clear & Restart"):
        reset()
        st.rerun()
