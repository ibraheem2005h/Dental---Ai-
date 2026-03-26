import streamlit as st

st.set_page_config(page_title="Dental Diagnosis", page_icon="🦷")

# 🔹 Title + Clinic Name
st.title("🦷 Dental Diagnosis System")
st.markdown("<h2 style='text-align: center; color: #555;'>IMS Dental Clinic</h2>", unsafe_allow_html=True)

# 🔹 Patient Name
patient_name = st.text_input("Patient Name")

# 🔹 Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)

bleeding = st.selectbox("Bleeding on Probing", ["No", "Yes"])

pocket = st.number_input("Pocket Depth (mm)", min_value=1, max_value=15, value=3)

cal = st.number_input("Clinical Attachment Loss (mm)", min_value=0, max_value=15, value=0)

# 🔹 Life Style
lifestyle = st.multiselect(
    "Life Style",
    ["None", "Smoking", "Alcohol", "Drugs"]
)

# 🔹 Medical Conditions
medical = st.multiselect(
    "Medical Conditions",
    ["None", "Diabetes", "Hypertension", "Hypotension", "Liver Disease", "Kidney Disease"]
)

# 🔹 Diagnose
if st.button("Diagnose"):

    risk = "Normal"

    # 🔴 Risk
    if ("Smoking" in lifestyle or "Diabetes" in medical):
        risk = "High Risk Patient"

    # 🟢 Diagnosis
    if bleeding == "Yes" and cal == 0:
        if pocket > 3:
            diagnosis = "Severe Gingivitis"
        else:
            diagnosis = "Gingivitis"
        stage = "-"
        grade = "-"
        treatment = "Scaling and oral hygiene"

    elif cal >= 1:
        diagnosis = "Periodontitis"

        # 🔹 Stage
        if cal <= 2:
            stage = "Stage I"
        elif cal <= 4:
            stage = "Stage II"
        elif cal <= 6:
            stage = "Stage III"
        else:
            stage = "Stage IV"

        # 🔹 Grade
        ratio = cal / age

        if "Smoking" in lifestyle or "Diabetes" in medical:
            grade = "Grade C"
        elif ratio < 0.25:
            grade = "Grade A"
        elif ratio < 1:
            grade = "Grade B"
        else:
            grade = "Grade C"

        treatment = "Deep cleaning / Surgery if needed"

    else:
        diagnosis = "Healthy"
        stage = "-"
        grade = "-"
        treatment = "Routine check-up"

    # 🔹 Results
    st.subheader("IMS Dental Clinic")
    st.write(f"Patient Name: {patient_name}")

    if risk == "High Risk Patient":
        st.warning("⚠️ High Risk Patient")

    st.success(f"Diagnosis: {diagnosis}")
    st.write(f"Stage: {stage}")
    st.write(f"Grade: {grade}")
    st.write(f"Treatment: {treatment}")
