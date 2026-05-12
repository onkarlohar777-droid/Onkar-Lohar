# number_guessing_game.py

import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

st.title("🎮 Number Guessing Game")

st.write("Guess a number between 1 and 100")

# Generate random number only once
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1
)

# Check guess
if st.button("Check Guess"):

    st.session_state.attempts += 1

    if guess < st.session_state.random_number:
        st.warning("Too Low! Try Again.")
    
    elif guess > st.session_state.random_number:
        st.warning("Too High! Try Again.")
    
    else:
        st.success(
            f"🎉 Correct! The number was {st.session_state.random_number}"
        )
        st.info(f"You guessed it in {st.session_state.attempts} attempts.")

# Restart game
if st.button("Restart Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("Game Restarted! Guess the new number.")
