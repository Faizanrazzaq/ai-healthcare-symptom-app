"""
AI Healthcare Symptom Information App
Educational demonstration only. It does not diagnose or replace a clinician.
"""

import streamlit as st

st.set_page_config(page_title="Healthcare Symptom Information", page_icon="🩺")

# A small, transparent rule-based knowledge base for demonstration.
# These examples are not a validated medical triage system.
SYMPTOM_GUIDANCE = {
    "chest pain": (
        "Chest pain can have serious causes.",
        "Seek emergency medical care now, especially if pain is severe, new, "
        "or occurs with shortness of breath, sweating, faintness, or nausea."
    ),
    "difficulty breathing": (
        "Difficulty breathing may be an emergency.",
        "Seek emergency medical care now if breathing is severe, sudden, or worsening."
    ),
    "fever": (
        "Fever can occur with many illnesses.",
        "Rest and fluids may help. Contact a healthcare professional for severe, "
        "persistent, or concerning symptoms, or if you are unsure what to do."
    ),
    "headache": (
        "Headaches have many possible causes.",
        "Seek emergency care for a sudden, extremely severe headache or one with "
        "confusion, weakness, fainting, or trouble speaking."
    ),
    "cough": (
        "Cough can occur with infections, allergies, and other conditions.",
        "Consider contacting a healthcare professional if it persists, worsens, "
        "or comes with breathing difficulty, chest pain, or coughing blood."
    ),
    "sore throat": (
        "A sore throat can have several causes.",
        "Seek professional advice if symptoms are severe, persistent, or make "
        "breathing or swallowing difficult."
    ),
}

st.title("🩺 Healthcare Symptom Information App")
st.write(
    "Enter symptoms to see general information from a small, predefined "
    "rule-based knowledge base."
)

st.warning(
    "Educational prototype only: this app cannot diagnose conditions or safely "
    "determine your individual urgency. Do not rely on it for medical decisions."
)

symptoms = st.text_area(
    "Describe your symptoms",
    placeholder="Example: I have a cough and sore throat",
    height=110,
)

if st.button("Show general information", type="primary"):
    if not symptoms.strip():
        st.info("Please enter a symptom description.")
    else:
        # Normalize the input so simple phrase matching ignores capitalization.
        text = symptoms.lower()
        matches = [
            (keyword, title, advice)
            for keyword, (title, advice) in SYMPTOM_GUIDANCE.items()
            if keyword in text
        ]

        if matches:
            st.subheader("General information")
            for keyword, title, advice in matches:
                st.markdown(f"**{title}**")
                st.write(advice)
        else:
            st.info(
                "No matching phrase was found in this small demonstration "
                "knowledge base. That does not mean the symptoms are harmless. "
                "Contact a healthcare professional for advice."
            )

st.caption(
    "Privacy: this prototype does not intentionally save symptom text. "
    "Avoid entering names or other identifying information."
)
st.caption(
    "If you may be experiencing a medical emergency, contact your local "
    "emergency number immediately."
)
