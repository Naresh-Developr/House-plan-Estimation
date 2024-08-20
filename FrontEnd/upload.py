import streamlit as st

def upload_plan():
    st.title("Upload New Plan")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "dwg"])

    if uploaded_file is not None:
        st.write(f"File uploaded: {uploaded_file.name}")
        st.image(uploaded_file, use_column_width=True)  # If the file is an image
        st.button("Process Plan")
    else:
        st.write("Please upload a plan file.")