import streamlit as st
import psycopg as db
st.icon("123.jpg")
st.title("Inventory Management System")

st.text(" \n \n \n \n")
# Create a form
with st.form("my_form"):
    # Add input elements to the form
    role = st.text_input("Enter your Role")
    password = st.text_input("Enter your password", type="password")  # Secure input for password
    
    # Create two columns for the buttons to align them horizontally
    col1, col2 = st.columns(2)
    
    with col1:
        sign_up = st.form_submit_button("Sign up")
    
    with col2:
        sign_in = st.form_submit_button("Sign in")
        

# Logic after the form is submitted
if sign_up:
    st.write(f"Sign up successful for {role}!")
elif sign_in:
    if role.lower() in ["admin", "user"]:
        st.write(f"{role}, you have successfully logged in!")
    else:
        st.write("Invalid role! Please enter a valid role.")
