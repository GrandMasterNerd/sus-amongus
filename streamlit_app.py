import streamlit as st

# Define pages
def home_page():
    st.title("ඞ Hello World ඞ")
    st.write("Why are you here???")
    st.image("res/Dog_side_eye.jpg")
    st.write("Kinda sus...")

    # Blank space
    st.write(" ")

    # Create a button
    if st.button("Click Me!"):
        st.success("You clicked me!")
    else:
        st.info("You know you want to...")

    # Blank space
    st.write(" ")

    # Create a button 2
    if st.button("No, Click Me!"):
        st.success("You clicked me!")
    else:
        st.info("Just do it...")

    # Blank space
    st.write(" ")

    # Create a button 3
    if st.button("DO NOT CLICK ME!!!"):
        st.success("I warned you...")
    else:
        st.info("WHATEVER YOU DO, DO NOT CLICK THIS BUTTON!")
