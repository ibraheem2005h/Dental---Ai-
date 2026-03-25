import streamlit as st
from fpdf import FPDF

st.title("🦷 Periodontal Diagnosis Assistant")

# 🟢 Patient Info
name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])

# 🟢 Clinical Data
pocket = st.number_input("Pocket Depth (mm)", min_value=1, max_value=15, value=3)
bleeding = st.selectbox("Bleeding on Probing", ["No", "Yes"])
cal = st.number_input("Clinical Attachment Loss (mm)", min_value=0, max_value=15, value=0)

if st.button("Diagnose & Create PDF"):

    if bleeding == "Yes" and pocket <= 3 and cal == 0:
        diagnosis = "Gingivitis"
        treatment = "Scaling and oral hygiene"

    elif pocket >= 4 and cal >= 1:
        diagnosis = "Periodontitis"
        treatment = "Deep cleaning or surgery"

    else:
        diagnosis = "Healthy"
        treatment = "Routine care"

    # 🟢 إنشاء PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Dental Report", ln=True)

    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Gender: {gender}", ln=True)

    pdf.cell(200, 10, txt=f"Diagnosis: {diagnosis}", ln=True)
    pdf.cell(200, 10, txt=f"Treatment: {treatment}", ln=True)

    pdf.output("report.pdf")

    st.success("PDF Created ✅")

    # زر تحميل
    with open("report.pdf", "rb") as f:
        st.download_button("Download Report", f, file_name="report.pdf")