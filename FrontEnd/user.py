import streamlit as st

def user_settings():
    st.title("User Settings")
    
    st.subheader("Profile Information")
    name = st.text_input("Name", "John Doe")
    email = st.text_input("Email", "johndoe@example.com")
    st.button("Update Profile")
    
    st.subheader("Preferences")
    st.checkbox("Receive Notifications")
    st.checkbox("Use Metric System")
    
    st.button("Save Preferences")
