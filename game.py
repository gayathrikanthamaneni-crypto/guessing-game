import streamlit as st
import random

# Initialize the random number in session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

st.title("🎯 Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# User guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to check guess
if st.button("Check"):
    if guess == st.session_state.secret_number:
        st.success(f"🎉 Correct! The number was {st.session_state.secret_number}!")
        st.balloons()
        # Reset for a new game
        st.session_state.secret_number = random.randint(1, 100)
        st.info("New number generated! Try again.")
    elif guess < st.session_state.secret_number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")

# Button to restart the game manually
if st.button("Reset Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.info("Game reset! I picked a new number.")
