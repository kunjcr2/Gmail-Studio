# Authentication and Authorization for Streamlit App on emails
import streamlit as st
from pymongo import MongoClient
import bcrypt
import dotenv
import os

dotenv.load_dotenv()

# MongoDB connection
def get_user_collection():
    mongodb_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongodb_uri)
    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise ValueError("DB_NAME environment variable is not set.")
    collection_name = os.getenv("COLLECTION_USERS")
    return client[db_name][collection_name]

# Authenticate user with username and password
def authenticate_user(username, password):
    user_collection = get_user_collection()
    
    user = user_collection.find_one({"username": username})
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return True
    return False

# Register a new user
def register_user(username, password1, password2):
    user_collection = get_user_collection()
    
    if password1 != password2:
        st.error("Passwords do not match.")
        return False
    
    if user_collection.find_one({"username": username}):
        st.error("Username already exists.")
        return False
    
    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    user_collection.insert_one({"username": username, "password": hashed_password})
    return True

# Streamlit app for authentication
def main():
    st.title("Streamlit Authentication")

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if authenticate_user(username, password):
                st.success("Logged in successfully!")
                # Redirect to main app or dashboard
            else:
                st.error("Invalid username or password.")
    elif choice == "Register":
        st.header("Register")
        username = st.text_input("Username")
        password1 = st.text_input("Password", type='password')
        password2 = st.text_input("Confirm Password", type='password')

        if st.button("Register"):
            if register_user(username, password1, password2):
                st.success("User registered successfully!")
                # Redirect to login page or main app
    else:
        st.error("Please select a valid option from the menu.")

main()