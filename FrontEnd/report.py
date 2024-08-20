import streamlit as st

def generate_report():
    st.title("Generate Report")
    
    st.subheader("Choose Report Type")
    report_type = st.selectbox("Report Type", ["Summary", "Detailed", "Client-Facing"])
    
    st.subheader("Customize Report")
    include_costs = st.checkbox("Include Cost Details")
    include_annotations = st.checkbox("Include Annotations")
    
    if st.button("Generate Report"):
        st.write("Generating report...")
        # Mock report generation
        st.success("Report generated successfully!")
        st.download_button(label="Download Report", data="Report data", file_name="report.pdf", mime="application/pdf")
