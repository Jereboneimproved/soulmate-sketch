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
    
    # LARGE LIBRARY OF 50 RIDICULOUS FACES
    funny_faces = [
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_0", "vibe": "a face of pure, cross-eyed disbelief"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_1", "vibe": "someone whose expression suggests they just saw a bird wear a hat"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_2", "vibe": "a masterpiece of a squint and a stuck-out tongue"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_3", "vibe": "an individual with a truly legendary double-chin and wide eyes"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_4", "vibe": "someone making a face like they are trying to solve math with their nose"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_5", "vibe": "a face frozen in a chaotic, mid-laugh snort"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_6", "vibe": "a person whose expression is 40% surprise and 60% confusion"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_7", "vibe": "a look of intense, bulging-eyed suspicion"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_8", "vibe": "someone who looks like they are trying to smell their own ears"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_9", "vibe": "a person making a face that defies all known anatomy"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_10", "vibe": "a legendary pucker that makes their whole head look smaller"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_11", "vibe": "someone who just smelled something from the year 1994"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_12", "vibe": "a face of absolute, unadulterated shock"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_13", "vibe": "a person with an expression of chaotic, bug-eyed joy"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_14", "vibe": "someone whose smile is upside down for no apparent reason"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_15", "vibe": "a masterpiece of a mid-sneeze squint"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_16", "vibe": "an individual who looks like they are being tickled by an invisible ghost"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_17", "vibe": "a person with a face like a melting candle of happiness"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_18", "vibe": "someone who just realized they left the oven on in another life"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_19", "vibe": "a look of pure, unbridled bewilderment"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_20", "vibe": "a face that says 'I didn't do it, but I saw who did'"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_21", "vibe": "someone trying to lick their own nose with maximum effort"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_22", "vibe": "a face of intense, cross-eyed focus on a single fly"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_23", "vibe": "an expression of pure, open-mouthed awe at a taco"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_24", "vibe": "a person who looks like they are mid-teleportation"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_25", "vibe": "a look that combines fear, excitement, and a very itchy chin"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_26", "vibe": "someone with a smile that's 15% too wide for their face"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_27", "vibe": "a person who just figured out that water is wet"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_28", "vibe": "an expression of deep, philosophical confusion over a sock"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_29", "vibe": "a face of pure, cross-eyed determination"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_30", "vibe": "someone who looks like they are trying to communicate with a toaster"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_31", "vibe": "a masterpiece of an eyeroll and a lip-bite"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_32", "vibe": "a person with a face like a crumpled-up paper bag of joy"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_33", "vibe": "someone who just saw their own reflection for the first time"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_34", "vibe": "a look of intense, bulging-eyed curiosity about your hair"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_35", "vibe": "a face of absolute, cross-eyed bewilderment at a cloud"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_36", "vibe": "someone who looks like they are trying to whistle with their eyes"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_37", "vibe": "a person making a face like a very surprised owl"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_38", "vibe": "an individual with a face frozen in mid-yawn shock"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_39", "vibe": "a face of deep, suspicious squinting at a blueberry"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_40", "vibe": "someone who looks like they just solved a mystery that didn't exist"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_41", "vibe": "a masterpiece of a side-eye and a smirk"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_42", "vibe": "a person whose face is 70% eyebrows and 30% panic"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_43", "vibe": "someone who looks like they are trying to taste the air with their forehead"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_44", "vibe": "a look of pure, wide-eyed amazement at a spoon"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_45", "vibe": "a person making a face like they are auditioning for a role as a gargoyle"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_46", "vibe": "an expression of intense, cross-eyed focus on a speck of dust"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_47", "vibe": "someone who looks like they just heard a joke from the year 3000"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_48", "vibe": "a face of deep, philosophical pondering over a paperclip"},
        {"url": "http://googleusercontent.com/image_collection/image_retrieval/13520259614020122899_49", "vibe": "someone whose face is a chaotic blend of joy, fear, and a sneeze"}
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

