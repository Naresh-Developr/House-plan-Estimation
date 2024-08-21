import streamlit as st
import os
import pandas as pd
from Buttons.createNewButton import save_project_to_csv
from datetime import datetime


def show_dashboard():
    st.title("Dashboard")

    # Display Projects
    st.subheader("Your Projects")
    project_columns = st.columns(3)
    for i in range(3):
        with project_columns[i]:
            image_path = "images/civil.png"
            if os.path.exists(image_path):
                st.image(image_path, use_column_width=True)
            else:
                st.text("No Thumbnail Available")
            st.button("View Project", key=f"view_{i}")

    # Display Recent Activity
    st.subheader("Recent Activity")
    st.write("• Uploaded new plan for Project X")
    st.write("• Generated report for Project Y")

    # Quick Actions Section
    st.subheader("Quick Actions")

    if 'creating_project' not in st.session_state:
        st.session_state.creating_project = False

    if st.button("Create New Project"):
        st.session_state.creating_project = True

    if st.session_state.creating_project:
        with st.container():
            with st.form(key='project_form'):
                st.subheader("Enter Project Details")

                # Form fields
                project_name = st.text_input("Project Name")
                description = st.text_area("Project Description")
                client_name = st.text_input("Client Name (Optional)")
                start_date = st.date_input("Start Date")
                end_date = st.date_input("Estimated Completion Date")

                # Submit button
                submit_button = st.form_submit_button(label='Save Project')

                if submit_button:
                    if project_name == "":
                        st.error("Project Name is required!")
                    else:
                        # Collect data into a dictionary
                        project_data = {
                            "Project Name": project_name,
                            "Description": description,
                            "Client Name": client_name,
                            "Start Date": start_date,
                            "End Date": end_date,
                            "Created On": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }

                        # Save the data to the CSV file using the save_project_to_csv function
                        save_project_to_csv(project_data)
                        
                        # Success message
                        st.success(f"Project '{project_name}' created successfully!")
                        
                        # Reset form and state
                        st.session_state.creating_project = False
                        st.experimental_rerun()

    # Upload New Plan Button
    if st.button("Upload New Plan"):
        st.query_params.update(page="upload")  # Set query parameter to navigate to upload page
        #  upload.upload_plan()


    # Display Existing Projects
    csv_file_path = os.path.join(os.path.dirname(__file__), '../../BackEnd/csv/newProject.csv')
    if os.path.exists(csv_file_path):
        st.write("File exists.")
        try:
            project_df = pd.read_csv(csv_file_path)
            st.write("Data loaded from file:")
            st.write(project_df)
        except pd.errors.EmptyDataError:
            st.write("CSV file is empty.")
    else:
        st.write("No projects created yet.")

    # Manual Refresh Button (Optional)
    if st.button("Refresh Dashboard"):
        st.experimental_rerun()
