import streamlit as st
import os
from datetime import datetime
import pandas as pd

def save_upload_to_csv(upload_data):
    csv_file_path = os.path.join(os.path.dirname(__file__), '../../BackEnd/csv/uploads.csv')
    upload_df = pd.DataFrame([upload_data])

    if os.path.exists(csv_file_path):
        upload_df.to_csv(csv_file_path, mode='a', header=False, index=False)
    else:
        upload_df.to_csv(csv_file_path, index=False)

def upload_plan():
    st.title("Upload New Plan")

    # Select Project
    csv_file_path = os.path.join(os.path.dirname(__file__), '../../BackEnd/csv/newProject.csv')
    if os.path.exists(csv_file_path):
        project_df = pd.read_csv(csv_file_path)
        project_names = project_df['Project Name'].tolist()
        selected_project = st.selectbox("Select Project", project_names)
    else:
        st.error("No projects found. Please create a project first.")
        return

    # File Upload
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "dwg"])

    if uploaded_file is not None:
        st.write(f"File uploaded: {uploaded_file.name}")
        
        # Show preview if the file is an image
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, use_column_width=True)
        
        # Process the file upload
        if st.button("Process Plan"):
            upload_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            upload_directory = os.path.join(os.path.dirname(__file__), f'../../BackEnd/uploads/{selected_project}/')

            if not os.path.exists(upload_directory):
                os.makedirs(upload_directory)

            file_path = os.path.join(upload_directory, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Save upload details to CSV
            upload_data = {
                "Project Name": selected_project,
                "File Name": uploaded_file.name,
                "Upload Time": upload_time,
                "File Path": file_path
            }
            save_upload_to_csv(upload_data)
            
            st.success(f"File '{uploaded_file.name}' uploaded successfully for project '{selected_project}'!")

    else:
        st.write("Please upload a plan file.")
