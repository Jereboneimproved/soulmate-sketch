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
    st.session_state.step = 1
    st.session_state.answers = {}
    if 'final_image' in st.session_state:
        del st.session_state.final_image

# --- STEP 1: WELCOME ---
if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Using Gemini 3 Flash to align your cosmic vibrations and sketch your true soulmate.")
    st.info("No email required. No login. Just destiny.")
    if st.button("Begin the Alignment 🚀"):
        next_step()

# --- STEP 2: USER SEX (NEW) ---
elif st.session_state.step == 2:
    st.subheader("Profile Initialization")
    choice = st.radio("What is your sex/gender identity?", ["Male", "Female", "Non-Binary / Other"])
    if st.button("Confirm Identity 👤"):
        st.session_state.answers['user_sex'] = choice
        next_step()

# --- STEP 3: PREFERENCE (NEW) ---
elif st.session_state.step == 3:
    st.subheader("Seeking Connection")
    choice = st.radio("What is your soulmate preference?", ["Male", "Female", "Doesn't Matter / All"])
    if st.button("Set Intentions ✨"):
        st.session_state.answers['preference'] = choice
        next_step()

# --- STEP 4: BIRTHDATE (NEW) ---
elif st.session_state.step == 4:
    st.subheader("Temporal Alignment")
    st.write("Your birth date determines your spiritual house.")
    # Standard calendar widget
    dob = st.date_input("When were you born?", min_value=date(1940, 1, 1), max_value=date.today())
    if st.button("Sync Timeline 📅"):
        st.session_state.answers['birthdate'] = dob
        next_step()

# --- STEP 5: ELEMENT ---
elif st.session_state.step == 5:
    st.subheader("Elemental Core")
    choice = st.radio("Which element matches your personality?", ["Fire 🔥", "Water 💧", "Earth 🌍", "Air ☁️", "Quintessence ✨"])
    if st.button("Next ➡️"):
        st.session_state.answers['element'] = choice
        next_step()

# --- STEP 6-10: LOGICAL QUESTIONS ---
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
    choice = st.radio("Where do you recharge?", ["In solitude", "With a small group", "At a party", "It depends on the moon"])
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
    st.subheader("The Ideal Connection")
    choice = st.radio("What's your relationship goal?", ["Partnership", "Friendship", "Adventure", "Deep connection", "Growth"])
    if st.button("Finalize Connection 🎯"):
        st.session_state.answers['dynamic'] = choice
        next_step()

# --- STEP 11: GENERATION ---
elif st.session_state.step == 11:
    st.write("### ✨ Channeling the Stars...")
    st.write(f"_Analyzing a {st.session_state.answers['user_sex']} soul seeking {st.session_state.answers['preference']}..._")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.04) 
        progress_bar.progress(percent_complete + 1)
    
    # FIXED: Using high-quality placeholder images that are stable
    funny_results = [
        {"name": "The Executive Primate", "url": "https://placedog.net/500/500?id=10", "msg": "A noble monkey who enjoys fine dining."},
        {"name": "The Potassium King", "url": "https://placedog.net/500/500?id=20", "msg": "A nano-banana with surprisingly athletic legs."},
        {"name": "The Minimalist", "url": "https://placedog.net/500/500?id=30", "msg": "A stick figure named Gary who is very good at listening."},
        {"name": "The Honk Master", "url": "https://placedog.net/500/500?id=40", "msg": "A clown who is also a licensed tax attorney."}
    ]
    
    result = random.choice(funny_results)
    st.session_state.final_image = result['url']
