import streamlit as st
import pandas as pd
import random

pd.options.mode.chained_assignment = None

# Load CSV
df = pd.read_csv("surviv_weapons_data.csv")
columns = df.columns

# Rebuild icon paths exactly like your script
for idx, i in enumerate(df[columns[2]]):
    df[columns[2]][idx] = f"icons/{idx}.png"

# Extract columns (same as your code)
weapons = df[columns[0]]
fire_types = df[columns[1]]
icons = df[columns[2]]
weapon_types = df[columns[3]]
ammo = df[columns[4]]
magazine_totals = df[columns[5]]
damage = df[columns[6]]
fire_rates = df[columns[7]]
dps = df[columns[8]]
reload = df[columns[9]]
features = df[columns[10]]
date_added = df[columns[11]]
how_to_counter = df[columns[12]]

# --- GAME STATE ---
if "index" not in st.session_state:
    st.session_state.index = random.randint(0, len(df) - 1)
    st.session_state.weapon = df.iloc[st.session_state.index]
    st.session_state.answer = st.session_state.weapon[0]
    st.session_state.attempts = 0

    # EXACT same hint creation order as your Tkinter script
    hints = []
    hints.append(f"Hint: {features[st.session_state.index]}")
    hints.append(f"Hint: {fire_rates[st.session_state.index]} fire rate")
    hints.append(f"Hint: {reload[st.session_state.index]} reload time")
    hints.append(f"Hint: {damage[st.session_state.index]} damage")
    hints.append(f"Counter: {how_to_counter[st.session_state.index]}")
    hints.append(f"Hint: {magazine_totals[st.session_state.index]} bullets in 1 magazine")
    hints.append(f"Hint: {ammo[st.session_state.index]} ammo")
    hints.append("Icon")

    # EXACT same shuffle behavior
    random.shuffle(hints)

    st.session_state.hints = hints
    st.session_state.revealed_hints = []  # store shown hints

st.title("Weapon Selection: Guess the Weapon")

# Weapon list (same as Tkinter Listbox)
guess = st.selectbox("Choose a weapon:", weapons)

# Show first hint automatically (same as your script)
if "first_hint" not in st.session_state:
    first = st.session_state.hints.pop()  # same as rand_num = len(hints)-1
    st.session_state.revealed_hints.append(first)
    st.session_state.first_hint = True

# Display all revealed hints so far
st.subheader("Hints:")
for h in st.session_state.revealed_hints:
    if h == "Icon":
        st.image(icons[st.session_state.index])
    else:
        st.write(h)

# Guess button
if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess != st.session_state.answer:
        st.error(f"{guess} is incorrect")

        # Show next hint (same pop-from-end logic)
        if st.session_state.hints:
            next_hint = st.session_state.hints.pop()
            st.session_state.revealed_hints.append(next_hint)
        else:
            st.info("No more hints available")

    else:
        st.success(f"{st.session_state.answer} is correct!")
        st.info(f"Attempts: {st.session_state.attempts}")
        st.image(icons[st.session_state.index])

        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
