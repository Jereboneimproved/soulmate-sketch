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

# --- STEP 11: THE CHARACTER REVEAL ---
elif st.session_state.step == 11:
    st.write("### ✨ Universal Alignment in Progress...")
    st.write(f"_Searching the multiverse for a match for {st.session_state.answers.get('user_sex')}..._")
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    
    # YOUR CUSTOM CHARACTER LIBRARY
    # Note: Use high-quality, direct .jpg links for these to work!
    character_library = [
        {"name": "Chucky", "url": "https://miro.medium.com/v2/resize:fit:1100/format:webp/0*q7vXds1n1-bYshJv.jpg", "vibe": "a tiny, stabby ginger doll"},
        {"name": "Jason Voorhees", "url": "https://en.wikipedia.org/wiki/Jason_Voorhees#/media/File:Jason_Voorhees_(Ken_Kirzinger).jpg", "vibe": "a hockey fan who never learned to swim"},
        {"name": "Michael Myers", "url": "https://en.wikipedia.org/wiki/Michael_Myers_(Halloween)#/media/File:MichaelMyers2018.jpg", "vibe": "a very quiet man in a painted William Shatner mask"},
        {"name": "Freddy Krueger", "url": "https://en.wikipedia.org/wiki/Freddy_Krueger#/media/File:Freddy_Krueger_(Robert_Englund).jpg", "vibe": "the ultimate dream-crashing burnt pizza man"},
        {"name": "Killer Clown", "url": "https://bloody-disgusting.com/wp-content/uploads/2015/08/Pennywise.jpg", "vibe": "a circus reject with bad intentions"},
        {"name": "Blacula", "url": "https://static.wikia.nocookie.net/monster-and-slashers/images/9/9d/Blacula_%282%29ac.JPG/revision/latest?cb=20190804034633", "vibe": "the smoothest vampire in the history of the night"},
        {"name": "Klingon", "url": "https://en.wikipedia.org/wiki/Worf#/media/File:WorfTNG.jpg", "vibe": "a warrior who takes dating very, very seriously"},
        {"name": "Pizza the Hutt", "url": "https://villains.fandom.com/wiki/Pizza_the_Hutt?file=HuttHD.jpg", "vibe": "literally a giant, melting pepperoni pizza"},
        {"name": "Pee Wee Herman", "url": "https://en.wikipedia.org/wiki/Pee-wee_Herman#/media/File:Pee-Wee_Herman_(1988).jpg", "vibe": "a man who loves his bike more than life itself"},
        {"name": "Chewbacca", "url": "https://specials-images.forbesimg.com/dam/imageserve/958761228/960x0.jpg", "vibe": "a walking carpet with a heart of gold"},
        {"name": "Angela Bassett", "url": "https://variety.com/wp-content/uploads/2024/09/JCO_7588_a3bd08.jpg", "vibe": "the most tremendous soulmate you've ever seen, believe me"},
        {"name": "Tyrone Biggums", "url": "https://comicvine.gamespot.com/a/uploads/original/2/29172/562318-tyrone_biggums2.jpg", "vibe": "a man who desperately needs sizzle candy"},
        {"name": "Captain Jack Sparrow", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Captain_Jack_Sparrow_%285763467649%29.jpg/1280px-Captain_Jack_Sparrow_%285763467649%29.jpg", "vibe": "you have a ridiculously high regard for fate, mate"},
        {"name": "Diva Plavalaguna", "url": "https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2Fjcsw4h2ifksd1.jpeg", "vibe": "She needs your help and your ______"},
        {"name": "Ghost Face", "url": "https://static.wikia.nocookie.net/scream/images/a/a5/Ghostface-Profile.jpg", "vibe": "What's your favorite movie?"}
    ]
    
    # Pick a random character
    selected = random.choice(character_library)
    st.session_state.final_image = selected['url']
    st.session_state.char_name = selected['name']
    
    try:
        # Gemini 3 Flash writes the funny verdict
        model = genai.GenerativeModel('gemini-3-flash')
        prompt = f"Write a funny 1-sentence soulmate reading for a {st.session_state.answers.get('user_sex')} who was just matched with {selected['name']} ({selected['vibe']}). Mention their element {st.session_state.answers.get('element')} and birthdate {st.session_state.answers.get('birthdate')}."
        response = model.generate_content(prompt)
        st.session_state.oracle_msg = response.text
    except:
        st.session_state.oracle_msg = f"The stars aligned you with {selected['name']}. Good luck, you're going to need it."

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




