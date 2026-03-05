import streamlit as st
import google.generativeai as genai
import random
import time

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

# --- STEP 2: ELEMENT ---
elif st.session_state.step == 2:
    st.subheader("Step 1: The Elemental Core")
    choice = st.radio("Which element matches your personality?", ["Fire 🔥", "Water 💧", "Earth 🌍", "Air ☁️", "Quintessence ✨"])
    if st.button("Next ➡️"):
        st.session_state.answers['element'] = choice
        next_step()

# --- STEP 3: PHYSICAL TRAITS ---
elif st.session_state.step == 3:
    st.subheader("Step 2: Physical Resonance")
    choice = st.selectbox("Which eye color do you find most 'soul-piercing'?", ["Deep Brown", "Ocean Blue", "Emerald Green", "Mystic Grey", "Amber/Gold"])
    if st.button("Lock in DNA Profile 🧬"):
        st.session_state.answers['eyes'] = choice
        next_step()

# --- STEP 4: ZODIAC ALIGNMENT ---
elif st.session_state.step == 4:
    st.subheader("Step 3: Celestial Timing")
    choice = st.select_slider("How strongly do the stars influence your path?", options=["Skeptic", "Curious", "Believer", "Devoted", "I am the Stars"])
    if st.button("Check Constellations 🌌"):
        st.session_state.answers['zodiac'] = choice
        next_step()

# --- STEP 5: PERSONALITY (NEW) ---
elif st.session_state.step == 5:
    st.subheader("Step 4: The Introvert/Extrovert Scale")
    choice = st.radio("Where do you recharge your energy?", ["In total solitude", "With a small group", "At a crowded party", "It depends on the moon"])
    if st.button("Analyze Energy 🔋"):
        st.session_state.answers['energy'] = choice
        next_step()

# --- STEP 6: LOVE LANGUAGE ---
elif st.session_state.step == 6:
    st.subheader("Step 5: The Language of the Heart")
    choice = st.radio("How do you best receive affection?", ["Words of Affirmation", "Acts of Service", "Physical Touch", "Receiving Gifts", "Quality Time"])
    if st.button("Vibe Check 💓"):
        st.session_state.answers['love_language'] = choice
        next_step()

# --- STEP 7: HOBBIES (NEW) ---
elif st.session_state.step == 7:
    st.subheader("Step 6: Harmonious Activities")
    choice = st.multiselect("Pick two activities for a perfect Saturday:", ["Hiking", "Gaming", "Cooking", "Sleeping", "Time Travel", "Napping"])
    if st.button("Sync Lifestyles ⛵"):
        st.session_state.answers['hobby'] = choice
        next_step()

# --- STEP 8: MORAL ALIGNMENT ---
elif st.session_state.step == 8:
    st.subheader("Step 7: The Final Frequency")
    choice = st.radio("What is your greatest strength?", ["Loyalty", "Intelligence", "Bravery", "Compassion", "Wit"])
    if st.button("Complete Pattern 🎯"):
        st.session_state.answers['strength'] = choice
        next_step()

# --- STEP 9: GENERATION ---
elif st.session_state.step == 9:
    st.write("### ✨ Channeling the Stars...")
    st.write("_Processing your unique spiritual signature..._")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.04) # Slower for suspense
        progress_bar.progress(percent_complete + 1)
    
    # --- FIXED PRANK LOGIC ---
    # Using reliable funny images that won't break
    funny_results = [
        {"name": "The Executive Primate", "url": "https://placedog.net/500/500?id=1", "msg": "A noble monkey in a tuxedo."},
        {"name": "The Potassium King", "url": "https://placedog.net/500/500?id=2", "msg": "A nano-banana with surprisingly long legs."},
        {"name": "The Minimalist", "url": "https://placedog.net/500/500?id=3", "msg": "A highly detailed stick figure named Gary."},
        {"name": "The Honk Master", "url": "https://placedog.net/500/500?id=4", "msg": "A clown who is also a licensed accountant."}
    ]
    
    result = random.choice(funny_results)
    st.session_state.final_image = result['url']
    st.session_state.oracle_msg = result['msg']
    
    st.session_state.step = 10
    st.rerun()

# --- STEP 10: THE REVEAL ---
elif st.session_state.step == 10:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    
    st.image(st.session_state.final_image, caption=f"Soulmate ID: {random.randint(10000, 99999)}")
    st.subheader(f"Oracle Insight: {st.session_state.oracle_msg}")
    
    st.write(f"The stars have spoken. Your {st.session_state.answers['element']} energy has led you to this moment. Compatibility: **99.8%**")
    
    if st.button("🔄 Clear & Restart"):
        reset()
        st.rerun()
