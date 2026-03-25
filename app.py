import streamlit as st

st.title("🦷 Advanced Periodontal Diagnosis")

# Patient Info
name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 120, 25)
gender = st.selectbox("Gender", ["Male", "Female"])

# Medical History
smoking = st.selectbox("Smoking", ["No", "Yes"])
diabetes = st.selectbox("Diabetes", ["No", "Controlled", "Uncontrolled"])
systemic = st.selectbox("Other Systemic Diseases", ["No", "Yes"])

# Clinical Data
pocket = st.number_input("Pocket Depth (mm)", 1, 15, 3)
bleeding = st.selectbox("Bleeding on Probing", ["No", "Yes"])
cal = st.number_input("Clinical Attachment Loss (mm)", 0, 15, 0)

if st.button("Diagnose"):

    # Diagnosis
    if bleeding == "Yes" and pocket <= 3 and cal == 0:
        diagnosis = "Gingivitis"
        stage = "-"
        grade = "-"
        treatment = "Scaling and oral hygiene"

    elif cal >= 1:
        diagnosis = "Periodontitis"

        # Stage
        if cal <= 2:
            stage = "Stage I"
        elif cal <= 4:
            stage = "Stage II"
        elif cal <= 6:
            stage = "Stage III"
        else:
            stage = "Stage IV"

        # Grade (CAL/Age)
        ratio = cal / age

        if ratio < 0.25:
            grade = "Grade A"
        elif ratio < 1:
            grade = "Grade B"
        else:
            grade = "Grade C"

        # 🔥 تعديل Grade حسب الحالة
        if smoking == "Yes" or diabetes == "Uncontrolled":
            grade = "Grade C (High Risk)"
        elif diabetes == "Controlled":
            grade = "Grade B (Moderate Risk)"

        # Treatment
        treatment = "Scaling + Root Planing"

        if stage in ["Stage III", "Stage IV"]:
            treatment += " + Surgical Therapy"

        if smoking == "Yes":
            treatment += " + Smoking cessation advice"

        if diabetes != "No":
            treatment += " + Medical consultation"

    else:
        diagnosis = "Healthy"
        stage = "-"
        grade = "-"
        treatment = "Routine care"

    # Output
    st.subheader("Result")
    st.write("Name:", name)
    st.write("Diagnosis:", diagnosis)
    st.write("Stage:", stage)
    st.write("Grade:", grade)
    st.write("Treatment:", treatment)
