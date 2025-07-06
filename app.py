import streamlit as st
from src.text_inference import predict_text
from src.image_inference import predict_image
from src.audio_inference import predict_audio

st.set_page_config(page_title="Multimodal Emotion Analyzer")
st.title("🎨 Multimodal Sentiment & Emotion Analyzer")

choice = st.sidebar.selectbox("Choose Input Type", ["Text", "Image", "Audio"])

if choice == "Text":
    text = st.text_area("Enter text:")
    if st.button("Analyze Text"):
        label, prob = predict_text(text)
        st.success(f"Prediction: {label} ({prob*100:.2f}%)")

elif choice == "Image":
    img_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if img_file and st.button("Analyze Image"):
        with open("temp_img.jpg", "wb") as f:
            f.write(img_file.read())
        label = predict_image("temp_img.jpg")
        st.success(f"Predicted Emotion: {label}")

elif choice == "Audio":
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    if audio_file and st.button("Analyze Audio"):
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_file.read())
        label = predict_audio("temp_audio.wav")
        st.success(f"Predicted Emotion: {label}")