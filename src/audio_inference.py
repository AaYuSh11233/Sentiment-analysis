import librosa
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("models/audio_model.h5")

labels = ["happy", "sad", "angry", "neutral"]

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, duration=3, offset=0.5)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def predict_audio(audio_path):
    features = extract_features(audio_path)
    pred = model.predict(np.expand_dims(features, axis=0))
    emotion = np.argmax(pred)
    return labels[emotion]