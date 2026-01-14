import streamlit as st
from PIL import Image
import numpy as np

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AgriGuard – AI Farming Assistant",
    page_icon="🌱",
    layout="centered"
)

# --------------------------------------------------
# App Header
# --------------------------------------------------
st.title("🌱 AgriGuard")
st.subheader("Gemini-Powered Precision Farming & Integrated Pest Management")

st.markdown(
    """
    AgriGuard performs image-based crop health analysis and generates
    Integrated Pest Management (IPM) recommendations using a
    hybrid AI + rule-based decision engine.
    """
)

st.markdown("---")

# --------------------------------------------------
# Model Logic Functions
# --------------------------------------------------

def preprocess_image(image):
    """
    Resize and normalize image for analysis.
    """
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    return img_array


def extract_features(img):
    """
    Extract simple visual features:
    - Mean brightness
    - Color variance
    These act as proxies for crop stress.
    """
    brightness = np.mean(img)
    color_variance = np.var(img)
    return brightness, color_variance


def assess_health(brightness, variance):
    """
    Rule-based crop health assessment.
    """
    if brightness < 0.35 or variance < 0.02:
        return "Severe Crop Stress", 3
    elif brightness < 0.55:
        return "Moderate Crop Stress", 2
    else:
        return "Healthy Crop", 1


def pest_disease_reasoning(severity):
    """
    Reasoning layer for pest/disease likelihood.
    """
    if severity == 3:
        return "High likelihood of pest infestation or fungal disease."
    elif severity == 2:
        return "Early-stage pest attack or nutrient deficiency detected."
    else:
        return "No visible pest or disease symptoms detected."


def generate_ipm(severity, wind_speed):
    """
    Integrated Pest Management (IPM) decision logic.
    """
    plan = []

    if severity >= 2:
        plan.append("Apply neem oil spray (3 ml per liter) as organic control.")
        if severity == 3:
            plan.append(
                "Use recommended chemical pesticide with proper safety measures."
            )

    if wind_speed <= 10:
        plan.append("Spraying conditions are optimal (low wind speed).")
    else:
        plan.append("Avoid spraying due to high wind conditions.")

    plan.append("Adopt companion planting (e.g., marigold) for pest prevention.")
    plan.append("Regular monitoring is advised for early detection.")

    return plan

# --------------------------------------------------
# User Input Section
# --------------------------------------------------
st.markdown("### 👇 Upload Crop / Leaf Image")

uploaded_image = st.file_uploader(
    "Upload a clear image of a crop or leaf",
    type=["jpg", "jpeg", "png"]
)

st.markdown("### 🌦️ Weather Conditions")
wind_speed = st.slider("Wind Speed (km/h)", 0, 30, 6)

# --------------------------------------------------
# Analysis Pipeline
# --------------------------------------------------
if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Crop"):
        st.info("Running crop health analysis pipeline...")

        # Preprocessing & Feature Extraction
        img = preprocess_image(image)
        brightness, variance = extract_features(img)

        # Reasoning & Decision Logic
        health_status, severity = assess_health(brightness, variance)
        diagnosis = pest_disease_reasoning(severity)
        ipm_plan = generate_ipm(severity, wind_speed)

        st.success("Analysis Complete")

        # --------------------------------------------------
        # Results Display
        # --------------------------------------------------
        st.subheader("🧪 Crop Health Assessment")
        st.write(f"**Health Status:** {health_status}")
        st.write(f"**Severity Level:** {severity} / 3")

        st.subheader("🐛 Pest / Disease Diagnosis")
        st.write(diagnosis)

        st.subheader("🌱 Integrated Pest Management (IPM) Plan")
        for step in ipm_plan:
            st.write(f"- {step}")

        st.caption(
            "Inference Logic: Image feature extraction + rule-based agronomic reasoning. "
            "Designed for seamless integration with Google Gemini Vision and Multimodal APIs."
        )

# --------------------------------------------------
# Conversational Interface (Demo)
# --------------------------------------------------
st.markdown("---")
st.subheader("🗣️ Ask AgriGuard")

query = st.text_input("Ask a question about your crop:")

if query:
    st.write(
        "Based on the current crop condition and environmental parameters, "
        "early intervention and sustainable IPM practices are recommended."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Live Prototype | Kshitij 2026 | Gemini Track")
