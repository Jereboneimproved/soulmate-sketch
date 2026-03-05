import streamlit as st
import google.generativeai as genai
import random
import time
from datetime import date

# --- CLOUD CONFIGURATION ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Missing API Key! Please add Secrets in Streamlit settings.")

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

# --- STEPS 1-10: THE "SERIOUS" QUIZ ---
# (Includes Sex, Preference, Birthdate, Element, Eyes, Zodiac, Energy, Heart, Strength)

if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Using Gemini 3 Flash to align your cosmic vibrations and sketch your true soulmate.")
    if st.button("Begin the Alignment 🚀"): next_step()

elif st.session_state.step == 2:
    st.subheader("Profile Initialization")
    st.session_state.answers['user_sex'] = st.radio("What is your sex/gender identity?", ["Male", "Female", "Non-Binary"])
    if st.button("Confirm 👤"): next_step()

elif st.session_state.step == 3:
    st.subheader("Seeking Connection")
    st.session_state.answers['preference'] = st.radio("What is your soulmate preference?", ["Male", "Female", "Doesn't Matter"])
    if st.button("Set Intentions ✨"): next_step()

elif st.session_state.step == 4:
    st.subheader("Temporal Alignment")
    dob = st.date_input("When were you born?", min_value=date(1940, 1, 1), max_value=date.today())
    if st.button("Sync Timeline 📅"):
        st.session_state.answers['birthdate'] = str(dob)
        next_step()

# --- QUESTIONS 5-10 (Simplified for this block) ---
elif st.session_state.step <= 10:
    questions = {
        5: ("Elemental Core", ["Fire 🔥", "Water 💧", "Earth 🌍", "Air ☁️"]),
        6: ("Eye Color Resonance", ["Brown", "Blue", "Green", "Grey"]),
        7: ("Celestial Timing", ["Skeptic", "Believer", "Devoted"]),
        8: ("Energy Source", ["Solitude", "Social", "Moonlight"]),
        9: ("Love Language", ["Words", "Touch", "Gifts", "Time"]),
        10: ("Ideal Dynamic", ["Adventure", "Peace", "Growth", "Passion"])
    }
    title, options = questions[st.session_state.step]
    st.subheader(title)
    st.session_state.answers[title] = st.radio("Choose carefully:", options)
    if st.button("Next ➡️"): next_step()

# --- STEP 11: THE VIRAL-SAFE GENERATION ---
elif st.session_state.step == 11:
    st.write("### ✨ Channeling the Stars...")
    st.write(f"_Analyzing a {st.session_state.answers.get('user_sex')} soul seeking {st.session_state.answers.get('preference')}..._")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    # LIBRARY OF RIDICULOUS FACES
    # Note: These use placeholder links; you can replace these with actual funny face URLs
    funny_faces = [
        {"url": "https://placedog.net/500/500?id=50", "vibe": "a man with 12 chins and a confused eyebrow"},
        {"url": "https://placedog.net/500/500?id=60", "vibe": "someone who just smelled a very old lemon"},
        {"url": "https://placedog.net/500/500?id=70", "vibe": "a person whose face looks like a melting candle of joy"},
        {"url": "https://placedog.net/500/500?id=80", "vibe": "a high-speed camera shot of someone sneezing"}
    ]
    
    selected = random.choice(funny_faces)
    
    try:
        # Use Gemini 3 Flash (Text) - High Quota/Free
        model = genai.GenerativeModel('gemini-3-flash')
        prompt = f"Write a funny 1-sentence mystical reading for a {st.session_state.answers.get('user_sex')} whose soulmate looks like {selected['vibe']}. Mention their birthdate {st.session_state.answers.get('birthdate')}."
        response = model.generate_content(prompt)
        st.session_state.oracle_msg = response.text
    except:
        st.session_state.oracle_msg = "The stars were too stunned to speak, but the image is clear."

    st.session_state.final_image = selected['url']
    st.session_state.step = 12
    st.rerun()

# --- STEP 12: THE REVEAL ---
elif st.session_state.step == 12:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    st.image(st.session_state.final_image, caption=f"Soulmate ID: {random.randint(10000, 99999)}")
    st.subheader("The Oracle's Verdict:")
    st.write(st.session_state.oracle_msg)
    st.write("Compatibility Score: **99.9%**")
    if st.button("🔄 Clear & Restart"): reset()
