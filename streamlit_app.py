import streamlit as st

st.title("ඞ Hello World ඞ")
st.write("Why are you here???")
st.image("res/Dog_side_eye.jpg")
st.write("Kinda sus...")

# Blank space
st.write(" ")

# Create a button
if st.button("Click Me!"):
    st.success("Button clicked!")
else:
    st.info("Button not clicked yet.")

# Blank space
st.write(" ")

# Create a button 2
if st.button("No, Click Me!"):
    st.success("Button clicked!")
else:
    st.info("Button not clicked yet.")
