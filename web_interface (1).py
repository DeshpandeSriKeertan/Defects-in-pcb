import streamlit as st
from PIL import Image
import tempfile
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PCB Defect Detection AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

body, .stApp {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(120deg, #0f2027, #2c5364, #00c6ff);
    color: white;
}

.glass {
    background: rgba(34, 40, 49, 0.6);
    backdrop-filter: blur(16px);
    border-radius: 18px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 1.5rem;
}

.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6rem 2rem;
}

[data-testid="metric-container"] {
    background: rgba(34,40,49,0.6);
    border-radius: 14px;
    padding: 1rem;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="glass" style="text-align:center">
<h1>PCB Defect Detection</h1>
<p>AI-Powered Circuit Board Inspection System</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## ⚙️ Configuration")

    confidence = st.slider("Confidence Threshold", 0.1, 1.0, 0.3)
    nms = st.slider("NMS Threshold", 0.1, 1.0, 0.4)

    st.markdown("### Defect Categories")
    st.markdown("""
    • Missing Hole  
    • Mouse Bite  
    • Open Circuit  
    • Short  
    • Spur  
    • Spurious Copper
    """)

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "🖼 Single Image",
    "📷 Live Capture",
    "📁 Batch Processing"
])

# ---------------- SINGLE IMAGE ----------------
with tab1:
    st.markdown("<div class='glass'><h3>Upload PCB Image</h3></div>", unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing (UI placeholder)..."):
                st.metric("Total Defects", "—")
                st.metric("Average Confidence", "—")
                st.info("🔌 Connect backend logic here")

# ---------------- LIVE CAPTURE ----------------
with tab2:
    st.markdown("<div class='glass'><h3>Live Camera Capture</h3></div>", unsafe_allow_html=True)

    cam = st.camera_input("Capture PCB Image")

    if cam:
        image = Image.open(cam)
        st.image(image, use_container_width=True)

        if st.button("Analyze Capture"):
            with st.spinner("Analyzing (UI placeholder)..."):
                st.metric("Detected Defects", "—")
                st.warning("Backend not connected")

# ---------------- BATCH PROCESSING ----------------
with tab3:
    st.markdown("<div class='glass'><h3>Batch PCB Inspection</h3></div>", unsafe_allow_html=True)

    files = st.file_uploader(
        "Upload Multiple Images",
        type=["jpg", "png", "jpeg"],
        accept_multiple_files=True
    )

    if files and st.button("Process Batch"):
        st.success(f"{len(files)} images uploaded")
        st.info("Batch inference logic goes here")

        for f in files:
            st.write(f"• {f.name} → Pending analysis")
