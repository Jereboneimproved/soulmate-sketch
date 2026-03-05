import streamlit as st
import google.generativeai as genai
import random
import time
from datetime import date

# --- CLOUD CONFIGURATION ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Missing GEMINI_API_KEY in Streamlit Secrets!")

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

# --- STEPS 1-10: THE JOURNEY ---
if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Using Gemini 3 Flash to align your cosmic vibrations and sketch your true soulmate.")
    st.info("No email required. No login. Just destiny.")
    if st.button("Begin the Alignment 🚀"): next_step()

elif st.session_state.step == 2:
    st.subheader("Profile Initialization")
    st.session_state.answers['user_sex'] = st.radio("What is your sex/gender identity?", ["Male", "Female", "Non-Binary"])
    if st.button("Confirm Identity 👤"): next_step()

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

elif st.session_state.step == 5:
    st.subheader("Elemental Core")
    st.session_state.answers['element'] = st.radio("Choose your element:", ["Fire 🔥", "Water 💧", "Earth 🌍", "Air ☁️", "Quintessence ✨"])
    if st.button("Next ➡️"): next_step()

elif st.session_state.step == 6:
    st.subheader("Physical Resonance")
    st.session_state.answers['eyes'] = st.selectbox("Preferred eye color?", ["Deep Brown", "Ocean Blue", "Emerald Green", "Mystic Grey"])
    if st.button("Lock DNA 🧬"): next_step()

elif st.session_state.step == 7:
    st.subheader("Energy Source")
    st.session_state.answers['energy'] = st.radio("Where do you recharge?", ["Solitude", "Socializing", "Nature", "The Moon"])
    if st.button("Analyze Energy 🔋"): next_step()

elif st.session_state.step == 8:
    st.subheader("Love Language")
    st.session_state.answers['love'] = st.radio("Primary love language?", ["Words", "Service", "Touch", "Gifts", "Time"])
    if st.button("Vibe Check 💓"): next_step()

elif st.session_state.step == 9:
    st.subheader("Lifestyle Sync")
    st.session_state.answers['hobby'] = st.selectbox("Ideal Saturday activity?", ["Hiking", "Gaming", "Sleeping", "Cooking", "Time Travel"])
    if st.button("Finalizing Pattern..."): next_step()

elif st.session_state.step == 10:
    st.subheader("The Final Frequency")
    st.session_state.answers['strength'] = st.radio("Your greatest strength?", ["Loyalty", "Intelligence", "Bravery", "Wit"])
    if st.button("Generate My Sketch ✨"): next_step()

# --- STEP 11: THE STABLE GENERATION ---
elif st.session_state.step == 11:
    st.write("### ✨ Channeling the Stars...")
    st.write(f"_Analyzing a {st.session_state.answers.get('user_sex')} soul seeking {st.session_state.answers.get('preference')}..._")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    
    # Stable library of funny human faces (using IDs to ensure they work)
    face_ids = list(range(1, 51))
    selected_id = random.choice(face_ids)
    
    # We use a reliable placeholder service for funny faces
    st.session_state.final_image = f"https://picsum.photos/500/500?random={selected_id}"
    
    try:
        model = genai.GenerativeModel('gemini-3-flash')
        prompt = f"Write a funny 1-sentence soulmate reading for a {st.session_state.answers.get('user_sex')} born on {st.session_state.answers.get('birthdate')}. Their soulmate is a 'magnificent weirdo'. Mention their {st.session_state.answers.get('element')} energy."
        response = model.generate_content(prompt)
        st.session_state.oracle_msg = response.text
    except:
        st.session_state.oracle_msg = "The stars were too stunned to speak, but the image of your destiny is clear."

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
