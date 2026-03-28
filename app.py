import streamlit as st

st.set_page_config(page_title="Dental Diagnosis", page_icon="🦷")

# 🔹 Header
col1, col2 = st.columns([3,1])
with col1:
    st.title("🦷 Dental Diagnosis System")
with col2:
    st.markdown("### IMS Dental Clinic")

# 🔹 اختيار نوع المرض
problem_type = st.sidebar.selectbox(
    "Choose Diagnosis Type",
    ["Periodontal", "Caries"]
)

# 🔹 Patient Info
st.subheader("Patient Information")
patient_name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 100, 25)

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

# 🔴 ================= PERIODONTAL =================
if problem_type == "Periodontal":

    st.header("Periodontal Diagnosis")

    bleeding = st.selectbox("Bleeding on Probing", ["No", "Yes"])
    pocket = st.number_input("Pocket Depth (mm)", 1, 15, 3)
    cal = st.number_input("Clinical Attachment Loss (mm)", 0, 15, 0)

    if st.button("Diagnose"):

        risk = "Normal"
        if ("Smoking" in lifestyle or "Diabetes" in medical):
            risk = "High Risk Patient"

        if bleeding == "Yes" and cal == 0:
            diagnosis = "Gingivitis" if pocket <= 3 else "Severe Gingivitis"
            stage = "-"
            grade = "-"
            treatment = "Scaling and oral hygiene"

        elif cal >= 1:
            diagnosis = "Periodontitis"

            if cal <= 2:
                stage = "Stage I"
            elif cal <= 4:
                stage = "Stage II"
            elif cal <= 6:
                stage = "Stage III"
            else:
                stage = "Stage IV"

            ratio = cal / age
            if "Smoking" in lifestyle or "Diabetes" in medical:
                grade = "Grade C"
            elif ratio < 0.25:
                grade = "Grade A"
            elif ratio < 1:
                grade = "Grade B"
            else:
                grade = "Grade C"

            treatment = "Deep cleaning / Surgery"

        else:
            diagnosis = "Healthy"
            stage = "-"
            grade = "-"
            treatment = "Routine check-up"

        st.subheader("IMS Dental Clinic Report")
        st.write(f"Patient Name: {patient_name}")

        if risk == "High Risk Patient":
            st.warning("⚠️ High Risk Patient")

        st.success(f"Diagnosis: {diagnosis}")
        st.write(f"Stage: {stage}")
        st.write(f"Grade: {grade}")
        st.write(f"Treatment: {treatment}")

# 🔵 ================= CARIES (ADVANCED) =================
elif problem_type == "Caries":

    st.header("Advanced Caries Diagnosis")

    # 🔹 Tooth (FDI system)
    tooth_number = st.text_input("Tooth Number (FDI e.g. 11, 26, 36)")

    # 🔹 Surface / Class
    caries_class = st.selectbox(
        "Caries Class (Black)",
        ["Class I", "Class II", "Class III", "Class IV", "Class V", "Class VI"]
    )

    # 🔹 Symptoms
    pain = st.selectbox("Pain", ["No", "Mild", "Severe"])
    sensitivity = st.selectbox("Sensitivity", ["No", "Cold", "Sweet", "Both"])
    cavity = st.selectbox("Visible Cavity", ["No", "Yes"])
    swelling = st.selectbox("Swelling / Abscess", ["No", "Yes"])

    # 🔹 X-ray
    xray = st.selectbox("Radiographic Lesion", ["None", "Enamel", "Dentin", "Pulp"])

    if st.button("Diagnose Caries"):

        risk = "Normal"
        if ("Smoking" in lifestyle or "Diabetes" in medical):
            risk = "High Risk Patient"

        # 🔥 Diagnosis logic
        if xray == "None" and cavity == "No":
            diagnosis = "Initial Caries"
        elif xray == "Enamel":
            diagnosis = "Enamel Caries"
        elif xray == "Dentin":
            diagnosis = "Dentin Caries"
        elif xray == "Pulp" or swelling == "Yes" or pain == "Severe":
            diagnosis = "Pulpal Involvement / Abscess"
        else:
            diagnosis = "Moderate Caries"

        # 🔹 Treatment logic
        if diagnosis == "Initial Caries":
            treatment = "Fluoride + Preventive care"
        elif diagnosis == "Enamel Caries":
            treatment = "Small filling"
        elif diagnosis == "Dentin Caries":
            treatment = "Filling"
        elif diagnosis == "Moderate Caries":
            treatment = "Deep filling"
        else:
            treatment = "Root canal / Extraction"

        # 🔹 Result
        st.subheader("IMS Dental Clinic Report")
        st.write(f"Patient Name: {patient_name}")
        st.write(f"Tooth Number: {tooth_number}")
        st.write(f"Class: {caries_class}")

        if risk == "High Risk Patient":
            st.warning("⚠️ High Risk Patient")

        st.success(f"Diagnosis: {diagnosis}")
        st.write(f"Treatment: {treatment}")
