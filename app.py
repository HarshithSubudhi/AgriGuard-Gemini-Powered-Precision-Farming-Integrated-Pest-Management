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

st.title("🌱 AgriGuard")
st.subheader("Gemini-Powered Precision Farming & Integrated Pest Management")

st.markdown("""
AgriGuard performs image-based crop health analysis and generates
Integrated Pest Management (IPM) recommendations using a
hybrid AI + rule-based decision engine.
""")

# --------------------------------------------------
# Model Logic Functions
# --------------------------------------------------

def preprocess_image(image):
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    return img_array

def extract_features(img):
    # Mean brightness and color variance as stress indicators
    brightness = np.mean(img)
    color_variance = np.var(img)
    return brightness, color_variance

def assess_health(brightness, variance):
    if brightness < 0.35 or variance < 0.02:
        return "Severe Crop Stress", 3
    elif brightness < 0.55:
        return "Moderate Crop Stress", 2
    else:
        return "Healthy Crop", 1

def pest_disease_reasoning(severity):
    if severity == 3:
        return "High likelihood of pest infestation or fungal disease."
    elif severity == 2:
        return "Early-stage pest attack or nutrient deficiency detected."
    else:
        return "No visible pest or disease symptoms detected."

def generate_ipm(severity, wind_speed):
    plan = []

    if severity >= 2:
        plan.append("Apply neem oil spray (3 ml per liter) as organic control.")
        if severity == 3:
            plan.append("Use recommended chemical pesticide with safety measures.")

    if wind_speed <= 10:
        plan.append("Spraying conditions are optimal (low wind speed).")
    else:
        plan.append("Avoid spraying due to high wind conditions.")

    plan.append("Adopt companion planting (e.g., marigold) for pest prevention.")
    plan.append("Regular monitoring is advised for early detect
