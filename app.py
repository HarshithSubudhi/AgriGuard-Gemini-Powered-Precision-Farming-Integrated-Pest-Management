import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="AgriGuard – AI Farming Assistant",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AgriGuard")
st.subheader("Gemini-Powered Precision Farming & Pest Management")

st.markdown(
    """
    AgriGuard is an AI-powered farming assistant that helps farmers detect
    crop diseases, pest infestations, and stress conditions using images.
    """
)

st.header("📸 Upload Crop / Leaf Image")
uploaded_image = st.file_uploader(
    "Upload a clear image of a crop leaf or plant",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Crop"):
        st.info("Analyzing image using Gemini AI...")

        # -------------------------------
        # Dummy AI Logic (Replace later with Gemini API)
        # -------------------------------
        pests = [
            "Healthy Crop (No visible disease detected)",
            "Leaf Blight (Fungal Infection)",
            "Aphid Infestation",
            "Fall Armyworm Damage",
            "Nutrient Deficiency (Nitrogen)"
        ]

        diagnosis = random.choice(pests)

        st.success("Analysis Complete")

        st.subheader("🧪 Diagnosis")
        st.write(diagnosis)

        st.subheader("🌿 Recommended Action")

        if "Healthy" in diagnosis:
            st.write(
                "- Crop appears healthy.\n"
                "- Continue regular monitoring.\n"
                "- Ensure proper irrigation and nutrient balance."
            )
        else:
            st.write(
                "**Organic Treatment:**\n"
                "- Neem oil spray (2–3 ml per liter of water)\n"
                "- Remove heavily affected leaves\n\n"
                "**Chemical Treatment:**\n"
                "- Use recommended pesticide as per crop guidelines\n"
                "- Follow safety protocols during application\n\n"
                "**Best Time to Spray:**\n"
                "- Early morning or late evening\n"
                "- Avoid windy or rainy conditions"
            )

st.header("🗣️ Ask AgriGuard")
query = st.text_input("Ask a question about your crop:")

if query:
    st.write(
        f"**AgriGuard Response:**\n"
        f"Based on your query, monitor your crop closely and follow "
        f"integrated pest management practices for best results."
    )

st.markdown("---")
st.caption("Prototype demo for Kshitij 2026 | Gemini Track")
