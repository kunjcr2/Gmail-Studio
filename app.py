import streamlit as st
import streamlit_auth

### Session states and session's experimental rerun ! ####

def main():
    st.title("Gmail Studio")
    st.write("Welcome to Gmail Studio!")
    
    # Authentication in sidebar
    with st.sidebar:
        st.header("🔐 Authentication")
        
        menu = ["Login", "Register"]
        choice = st.selectbox("Menu", menu)
        
        if choice == "Login":
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            
            if st.button("Login"):
                if streamlit_auth.authenticate_user(username, password):
                    st.success("Logged in successfully!")
                    logged_in()
                else:
                    st.error("Invalid username or password.")
        
        elif choice == "Register":
            st.subheader("Register")
            username = st.text_input("Username")
            password1 = st.text_input("Password", type='password')
            password2 = st.text_input("Confirm Password", type='password')
            
            if st.button("Register"):
                if streamlit_auth.register_user(username, password1, password2):
                    st.success("User registered successfully!")
                    logged_in()
                else:
                    st.error("Registration failed.")

def logged_in():
    st.title("Welcome to Gmail Studio")