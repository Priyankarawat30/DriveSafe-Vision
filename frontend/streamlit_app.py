import streamlit as st
import requests

st.set_page_config(page_title="Driver Drowsiness Detector", layout="centered")
st.title("🚘 Driver Drowsiness Detection")
st.markdown("Take a photo and detect if the driver is **drowsy or yawning**.")

img_file = st.camera_input("Capture your face:")

if img_file:
    files = {"file": img_file.getvalue()}
    with st.spinner("Analyzing..."):
        try:
            response = requests.post("http://127.0.0.1:8000/predict", files=files)
            if response.status_code == 200:
                data = response.json()
                st.success("✅ Prediction Complete")
                st.write(f"**EAR (Eye Aspect Ratio)**: `{data['ear']}`")
                st.write(f"**MAR (Mouth Aspect Ratio)**: `{data['mar']}`")
                st.write(f"**Drowsy**: `{data['drowsy']}`")
                st.write(f"**Yawning**: `{data['yawning']}`")
            else:
                st.error("❌ Backend returned error.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
