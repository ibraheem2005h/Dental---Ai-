import streamlit as st

st.title("🦷 Advanced Periodontal Diagnosis")

# Patient Info
name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 120, 25)
gender = st.selectbox("Gender", ["Male", "Female"])

# Life Style
lifestyle = st.multiselect(
    "Life Style",
    ["Smoking", "Alcohol", "Drugs"]
)

# Medical Conditions
diseases = st.multiselect(
    "Medical Conditions",
    [
        "Diabetes",
        "Cardiovascular Disease",
        "Hypertension",
        "Osteoporosis",
        "Immunocompromised",
        "Pregnancy",
        "None"
    ]
)

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

        # Grade
        ratio = cal / age

        if ratio < 0.25:
            grade = "Grade A"
        elif ratio < 1:
            grade = "Grade B"
        else:
            grade = "Grade C"

        # تعديل حسب lifestyle
        if "Smoking" in lifestyle or "Drugs" in lifestyle:
            grade = "Grade C (High Risk)"

        # تعديل حسب الأمراض
        if "Diabetes" in diseases or "Immunocompromised" in diseases:
            grade = "Grade C (Systemic Risk)"
        elif "Cardiovascular Disease" in diseases:
            grade = "Grade B (Medical Risk)"

        # Treatment
        treatment = "Scaling + Root Planing"

        if stage in ["Stage III", "Stage IV"]:
            treatment += " + Surgical Therapy"

        if "Smoking" in lifestyle:
            treatment += " + Smoking cessation"

        if diseases and "None" not in diseases:
            treatment += " + Medical consultation"

    else:
        diagnosis = "Healthy"
        stage = "-"
        grade = "-"
        treatment = "Routine care"

    # Output
    st.subheader("Result")

    # High Risk Alert
    if ("Smoking" in lifestyle or "Drugs" in lifestyle or
        "Diabetes" in diseases or stage in ["Stage III", "Stage IV"]):
        st.error("⚠️ High Risk Patient")

    # Colored Diagnosis
    if diagnosis == "Healthy":
        st.success(f"Diagnosis: {diagnosis}")
    elif diagnosis == "Gingivitis":
        st.warning(f"Diagnosis: {diagnosis}")
    else:
        st.error(f"Diagnosis: {diagnosis}")

    st.write("Name:", name)
    st.write("Stage:", stage)
    st.write("Grade:", grade)
    st.write("Treatment:", treatment)
