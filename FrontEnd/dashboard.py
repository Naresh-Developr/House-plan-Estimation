import streamlit as st
import os

def show_dashboard():
    st.title("Dashboard")

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

    st.subheader("Recent Activity")
    st.write("• Uploaded new plan for Project X")
    st.write("• Generated report for Project Y")

    st.subheader("Quick Actions")
    st.button("Create New Project")
    st.button("Upload New Plan")
