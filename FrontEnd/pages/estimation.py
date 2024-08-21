import streamlit as st

def estimation():
    st.title("Estimation Tools")
    
    # Sidebar for parameter adjustments
    st.sidebar.subheader("Estimation Parameters")
    wall_thickness = st.sidebar.slider("Wall Thickness (cm)", 10, 50, 30)
    material_type = st.sidebar.selectbox("Material Type", ["Brick", "Concrete", "Wood"])
    
    st.subheader("Estimation Results")
    st.write(f"Estimated wall thickness: {wall_thickness} cm")
    st.write(f"Material selected: {material_type}")
    
    # Display dynamic results (mock data for now)
    st.metric("Total Cost", "$15,000")
    st.metric("Total Material Quantity", "10,000 bricks")
