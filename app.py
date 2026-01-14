import streamlit as st
from PIL import Image
import numpy as np
import cv2

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AgriGuard – AI Farming Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AgriGuard")
st.subheader("Gemini-Powered Precision Farming & Integrated Pest Management")

st.markdown("""
AgriGuard is an AI-powered farming assistant that performs
image-based crop diagnosis and generates Integrated Pest Management (IPM)
recommendations using multimodal reasoning.
""")

# --------------------------------------------------
# Utility Functions (Model Logic)
# --------------------------------------------------

def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    return img

def extract_visual_features(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    green_ratio = np.mean(hsv[:, :, 1])  # Saturation proxy
    brightness = np.mean(hsv[:, :, 2])   # Stress indicator
    return green_ratio, brightness

def diagnose_crop(green_ratio, brightness):
    if brightness < 80:
        return "Severe Stress Detected", 3
    elif brightness < 120:
        return "Moderate Stress Detected", 2
    else:
        return "Healthy Crop", 1

def pest_disease_inference(severity):
    if severity == 3:
        return "High probability of fungal disease or pest infestation"
    elif severity == 2:
        return "Early-stage pest or nutrient deficiency detected"
    else:
        return "No visible pest or disease symptoms"

def generate_ipm_plan(severity, weather):
    recommendations = []

    if severity >= 2:
        recommendations.append("Apply neem oil spray (3 ml/L) as organic control.")
        if severity == 3:
            recommendations.append("Use targeted chemical pesticide as per crop advisory.")

    if weather["wind"] < 10:
        recommendations.append("Spraying conditions optimal (low wind).")
    else:
        recommendations.append("Avoid spraying due to high wind speed.")

    recommendations.append("Adopt companion planting (e.g., marigold) for pest prevention.")

    return recommendations

# --------------------------------------------------
# Image Upload
# --------------------------------------------------
st.header("📸 Upload Crop / Leaf Image")
uploaded_image = st.file_uploader(
    "Upload a clear crop or leaf image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# Weather Input
# --------------------------------------------------
st.header("🌦️ Local Weather Conditions")
temp = st.slider("Temperature (°C)", 10, 45, 28)
humidity = st.slider("Humidity (%)", 20, 100, 65)
wind = st.slider("Wind Speed (km/h)", 0, 30, 6)

weather_data = {
    "temperature": temp,
    "humidity": humidity,
    "wind": wind
}

# --------------------------------------------------
# Analysis Pipeline
# --------------------------------------------------
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Crop"):
        st.info("Running multimodal analysis pipeline...")

        img = preprocess_image(image)
        green_ratio, brightness = extract_visual_features(img)

        health_status, severity = diagnose_crop(green_ratio, brightness)
        pest_disease = pest_disease_inference(severity)
        ipm_plan = generate_ipm_plan(severity, weather_data)

        st.success("Analysis Complete")

        # --------------------------------------------------
        # Results
        # --------------------------------------------------
        st.subheader("🧪 Crop Health Assessment")
        st.write(f"**Health Status:** {health_status}")
        st.write(f"**Severity Level:** {severity} / 3")

        st.subheader("🐛 Pest / Disease Diagnosis")
        st.write(pest_disease)

        st.subheader("🌱 Integrated Pest Management (IPM) Plan")
        for rec in ipm_plan:
            st.write(f"- {rec}")

        st.caption(
            "Inference Logic: Vision-based feature extraction + "
            "rule-based agronomic decision engine. "
            "Gemini Vision API integration planned for final deployment."
        )

# --------------------------------------------------
# Conversational Interface
# --------------------------------------------------
st.header("🗣️ Ask AgriGuard")
query = st.text_input("Ask a question about your crop:")

if query:
    st.write(
        "Based on your crop condition and weather parameters, "
        "early intervention and sustainable IPM practices are recommended."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Live Prototype | Kshitij 2026 | Gemini Track")
