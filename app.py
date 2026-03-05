import streamlit as st
import random
import time

# --- SETUP & STYLING ---
st.set_page_config(page_title="Cosmic Soulmate Sketcher", page_icon="🔮")

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# --- NAVIGATION FUNCTIONS ---
def next_step(): st.session_state.step += 1
def reset(): st.session_state.step = 1

# --- SCREEN 1: INTRO ---
if st.session_state.step == 1:
    st.title("🔮 The Soulmate Sketcher")
    st.write("Welcome to the most accurate soulmate visualization tool in the galaxy. ✨")
    st.info("No email required. No login. Just destiny.")
    if st.button("Begin the Alignment 🚀"):
        next_step()

# --- SCREEN 2: QUESTION 1 ---
elif st.session_state.step == 2:
    st.subheader("Step 1: The Elemental Core")
    choice = st.radio("Which element resonates with your current vibe?", 
                     ["🔥 Fire", "💧 Water", "🌍 Earth", "☁️ Air", "✨ Quintessence"])
    if st.button("Confirm Connection 🎯"):
        st.session_state.answers['element'] = choice
        next_step()

# --- SCREEN 3: QUESTION 2 ---
elif st.session_state.step == 3:
    st.subheader("Step 2: The Lifestyle Anchor")
    choice = st.radio("What is your ideal relationship dynamic?", 
                     ["💞 Partnership", "💓 Friendship", "⛵ Adventure", "💖 Deep connection", "🎯 Balanced growth"])
    if st.button("Syncing Souls..."):
        st.session_state.answers['dynamic'] = choice
        next_step()

# --- SCREEN 4: THE GENERATION ---
elif st.session_state.step == 4:
    with st.spinner("✨ Channeling cosmic energy... (this takes 3 seconds)"):
        time.sleep(3) # Purely for dramatic effect
    next_step()
    st.rerun()

# --- SCREEN 5: THE REVEAL ---
elif st.session_state.step == 5:
    st.balloons()
    st.header("✨ Your Soulmate Sketch is Ready!")
    
    # Randomly pick a funny result
    results = [
        {"name": "The Executive Primate", "img": "https://placedog.net/500/500", "desc": "A noble soul who values bananas and board meetings."},
        {"name": "The Abstract Hero", "img": "https://via.placeholder.com/500/500?text=A+Literal+Stick+Figure", "desc": "Minimalist, thin, and always upright."},
        {"name": "The Nano-Legend", "img": "https://via.placeholder.com/500/500?text=A+Banana+With+Legs", "desc": "Short, sweet, and high in potassium."}
    ]
    
    final = random.choice(results)
    
    st.image(final['img'], caption=f"Sketch ID: {random.randint(1000, 9999)}")
    st.subheader(final['name'])
    st.write(final['desc'])
    
    if st.button("🔄 Try Again"):
        reset()
        st.rerun()