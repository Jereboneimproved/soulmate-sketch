import streamlit as st
import google.generativeai as genai
import random
import time
from datetime import date

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
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- STEP 1: WELCOME ---
if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Using Gemini 3 Flash to align your cosmic vibrations and sketch your true soulmate.")
    st.info("No email required. No login. Just destiny.")
    if st.button("Begin the Alignment 🚀"):
        next_step()

# --- STEP 2: USER SEX ---
elif st.session_state.step == 2:
    st.subheader("Profile Initialization")
    choice = st.radio("What is your sex/gender identity?", ["Male", "Female", "Non-Binary / Other"])
    if st.button("Confirm Identity 👤"):
        st.session_state.answers['user_sex'] = choice
        next_step()

# --- STEP 3: PREFERENCE ---
elif st.session_state.step == 3:
    st.subheader("Seeking Connection")
    choice = st.radio("What is your soulmate preference?", ["Male", "Female", "Doesn't Matter / All"])
    if st.button("Set Intentions ✨"):
        st.session_state.answers['preference'] = choice
        next_step()

# --- STEP 4: BIRTHDATE ---
elif st.session_state.step == 4:
    st.subheader("Temporal Alignment")
    dob = st.date_input("When were you born?", min_value=date(1940, 1, 1), max_value=date.today())
    if st.button("Sync Timeline 📅"):
        st.session_state.answers['birthdate'] = str(dob)
        next_step()

# --- STEPS 5-10: COSMIC QUESTIONS ---
elif st.session_state.step == 5:
    st.subheader("Elemental Core")
    choice = st.radio("Which element matches your personality?", ["Fire 🔥", "Water 💧", "Earth 🌍", "Air ☁️", "Quintessence ✨"])
    if st.button("Next ➡️"):
        st.session_state.answers['element'] = choice
        next_step()

elif st.session_state.step == 6:
    st.subheader("Physical Resonance")
    choice = st.selectbox("Which eye color do you find most 'soul-piercing'?", ["Deep Brown", "Ocean Blue", "Emerald Green", "Mystic Grey", "Amber/Gold"])
    if st.button("Lock DNA 🧬"):
        st.session_state.answers['eyes'] = choice
        next_step()

elif st.session_state.step == 7:
    st.subheader("Celestial Timing")
    choice = st.select_slider("How strongly do the stars influence you?", options=["Skeptic", "Curious", "Believer", "Devoted", "I am the Stars"])
    if st.button("Check Constellations 🌌"):
        st.session_state.answers['zodiac'] = choice
        next_step()

elif st.session_state.step == 8:
    st.subheader("Energy Source")
    choice = st.radio("Where do you recharge?", ["In solitude", "With a small group", "At a party", "The moon decides"])
    if st.button("Analyze Energy 🔋"):
        st.session_state.answers['energy'] = choice
        next_step()

elif st.session_state.step == 9:
    st.subheader("Language of the Heart")
    choice = st.radio("How do you best receive affection?", ["Words", "Service", "Touch", "Gifts", "Time"])
    if st.button("Vibe Check 💓"):
        st.session_state.answers['love_language'] = choice
        next_step()

elif st.session_state.step == 10:
    st.subheader("The Final Frequency")
    choice = st.radio("What is your greatest strength?", ["Loyalty", "Intelligence", "Bravery", "Compassion", "Wit"])
    if st.button("Generate My Sketch ✨"):
        st.session_state.answers['strength'] = choice
        next_step()

# --- STEP 11: GENERATION (THE STUCK SCREEN FIX) ---
elif st.session_state.step == 11:
    st.write("### ✨ Channeling the Stars...")
    st.write(f"_Analyzing a {st.session_state.answers.get('user_sex', 'unique')} soul seeking {st.session_state.answers.get('preference', 'connection')}..._")
    
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02) 
        progress_bar.progress(percent_complete + 1)
    
    # Prank library
    funny_results = [
        {"url": "https://placedog.net/500/500?id=15", "msg": "A noble monkey who only wears designer tuxedos."},
        {"url": "https://placedog.net/500/500?id=25", "msg": "A nano-banana with an Olympic-level marathon stride."},
        {"url": "https://placedog.net/500/500?id=35", "msg": "Gary the Stick Figure. He has a great personality."},
        {"url": "https://placedog.net/500/500?id=45", "msg": "A clown who just passed their CPA exam."}
    ]
    
    selected = random.choice(funny_results)
    st.session_state.final_image = selected['url']
    st.session_state.oracle_msg = selected['msg']
    
    # Force the step update and rerun
    st.session_state.step = 12
    st.rerun()

# --- STEP 12: THE REVEAL ---
elif st.session_state.step == 12:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    
    st.image(st.session_state.final_image, caption=f"Soulmate ID: {random.randint(10000, 99999)}")
    st.subheader(f"Oracle Insight: {st.session_state.oracle_msg}")
    
    st.write(f"The stars have spoken. Based on your {st.session_state.answers.get('element', 'cosmic')} energy and your birthdate, this is your perfect match.")
    st.write("Compatibility Score: **99.9%**")
    
    if st.button("🔄 Clear & Restart"):
        reset()
