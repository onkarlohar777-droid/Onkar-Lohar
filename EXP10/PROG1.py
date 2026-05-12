import streamlit as st

# Title and Header
st.title("Simple Streamlit Application")
st.header("User Input and Display Demo")

# User Input Widgets
name = st.text_input("Enter your name:")

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=100
)

color = st.selectbox(
    "Choose your favorite color:",
    ["Red", "Blue", "Green"]
)

# Button
if st.button("Submit"):
    st.success("Data submitted successfully!")

    # Display User Data
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Favorite Color:", color)

# Display Text and Markdown
st.markdown("### This is a Markdown heading")
st.text("This is plain text output")
