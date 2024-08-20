import streamlit as st
import dashboard,upload,estimation,report,user

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Upload Plan", "Estimation", "Reports", "Settings"])

# Main content area changes based on selection
if page == "Dashboard":
    dashboard.show_dashboard()
elif page == "Upload Plan":
    upload.upload_plan()
elif page == "Estimation":
    estimation.estimation()
elif page == "Reports":
    report.generate_report()
elif page == "Settings":
    user.user_settings()



st.markdown(
    """
    <style>
    body {
        background-color: #2C2C2C;  /* Dark background */
        color: #f5f5f5;  /* Light text color */
        font-family: 'Arial', sans-serif;
    }
    
    .main {
        background-color: #2C2C2C;
    }

    .stButton>button {
        background-color: #4CAF50;  /* Green button */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        display: inline-block;
        font-size: 14px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }

    .stSidebar .stButton>button {
        background-color: #1E1E1E;
        color: #f5f5f5;
        border: none;
        padding: 10px 20px;
        font-size: 14px;
        margin: 4px 2px;
        cursor: pointer;
    }

    .stSidebar .stButton>button:hover {
        background-color: #333333;
        color: #4CAF50;
    }

    .stSidebar .sidebar-content {
        background-color: #1E1E1E;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)




