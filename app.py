import streamlit as st

st.title("🦷 Advanced Periodontal Diagnosis")

# Patient Info
name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 120, 25)
gender = st.selectbox("Gender", ["Male", "Female"])

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

        # Grade (based on age roughly)
        if age < 30:
            grade = "Grade C (Rapid progression)"
        elif age < 50:
            grade = "Grade B (Moderate)"
        else:
            grade = "Grade A (Slow)"

        treatment = "Scaling + Root Planing or Surgery"

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
