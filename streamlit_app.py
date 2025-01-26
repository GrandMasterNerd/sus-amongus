import streamlit as st
import time

# Initialize session state for page tracking and button click handling
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if "button3_clicked" not in st.session_state:
    st.session_state.button3_clicked = False

if "navigated" not in st.session_state:
    st.session_state.navigated = False

# Define a function for navigation
def navigate_to(page):
    st.session_state.current_page = page

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
    if st.session_state.button3_clicked:
        if not st.session_state.navigated:  # Only wait and navigate once
            st.success("I warned you...")
            time.sleep(3)
            st.session_state.navigated = True
            navigate_to("page1")
    elif st.button("DO NOT CLICK ME!!!"):
        st.session_state.button3_clicked = True

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")
    if st.button("Go Home"):
        navigate_to("home")

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")
    if st.button("Go Home"):
        navigate_to("home")

# Render the current page
if st.session_state.current_page == "home":
    home_page()
elif st.session_state.current_page == "page1":
    page1()
elif st.session_state.current_page == "page2":
    page2()
