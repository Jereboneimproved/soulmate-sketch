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

# --- STEP 11: THE FACE REVEAL LOGIC ---
elif st.session_state.step == 11:
    st.write("### ✨ Channeling the Stars...")
    st.write(f"_Finding the one for a {st.session_state.answers.get('user_sex')} soul..._")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    
    # Curated Library of Expressive/Funny Face IDs
    # Using a service that generates random human faces based on specific 'funny' seeds
    face_seeds = [
        "crazy", "funny", "silly", "expression", "shock", "goofy", 
        "surprised", "weird", "laughing", "confused", "staring"
    ]
    random_seed = random.choice(face_seeds) + str(random.randint(1, 100))
    
    # This URL specifically pulls from a human face database using a random seed
    st.session_state.final_image = f"https://robohash.org/{random_seed}.png?set=set4" 
    # NOTE: set4 creates hilarious 'Kitten/Humanoid' faces. 
    # If you want REAL funny human photos, use the library below:
    
    funny_human_photos = [
        "https://images.unsplash.com/photo-1544723795-3fb3afef99a3?w=500", # Surprise
        "https://images.unsplash.com/photo-1595152772835-219674b2a8a6?w=500", # Goofy Smile
        "https://images.unsplash.com/photo-1520451644838-906a72aa7c86?w=500", # Confusion
        "https://images.unsplash.com/photo-1599566150163-29194dcaad36?w=500"  # Intense Stare
    ]
    # To use real photos instead, uncomment the line below:
    # st.session_state.final_image = random.choice(funny_human_photos)

    try:
        model = genai.GenerativeModel('gemini-3-flash')
        prompt = f"Write a hilarious 1-sentence soulmate reading. They picked {st.session_state.answers.get('element')} and were born on {st.session_state.answers.get('birthdate')}. Their soulmate is a 'magnificent weirdo'. Be witty."
        response = model.generate_content(prompt)
        st.session_state.oracle_msg = response.text
    except:
        st.session_state.oracle_msg = "The stars were too stunned by this beauty to speak."

    st.session_state.step = 12
    st.rerun()

# --- STEP 12: THE REVEAL ---
elif st.session_state.step == 12:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    
    # Centering the funny face
    st.image(st.session_state.final_image, use_container_width=True)
    
    st.subheader("The Oracle's Verdict:")
    st.info(st.session_state.oracle_msg)
    
    st.write(f"**Compatibility Score:** {random.randint(98, 99)}.{random.randint(1, 9)}%")
    st.caption(f"Soulmate ID: {random.randint(10000, 99999)}")
    
    if st.button("🔄 Clear & Restart"):
        reset()

