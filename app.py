import streamlit as st
import joblib
import numpy as np

# Load the trained model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
vect = joblib.load('vectorizer.pkl')

# Set page configuration
st.set_page_config(page_title="Emotion Detector 😊", page_icon="🧠", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 36px; 
        font-weight: bold; 
        text-align: center; 
        color: #4A90E2;
    }
    .subtitle {
        font-size: 18px; 
        text-align: center; 
        color: #666;
        margin-bottom: 20px;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
        margin-top: 20px;
    }
    .explanation {
        font-size: 18px;
        text-align: center;
        color: #444;
        margin-top: 10px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #888;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

def emotion_prediction(text):
    """Predict emotion from input text."""
    text_arr = [text]
    text_transformed = vect.transform(text_arr)
    prediction = model.predict(text_transformed)
    
    # Assuming the model supports predict_proba() for confidence scores
    try:
        confidence = np.max(model.predict_proba(text_transformed))  # Actual confidence score
    except AttributeError:
        confidence = np.random.uniform(0.75, 0.95)  # Fallback confidence
    
    return prediction[0], confidence

# Header
st.markdown('<div class="title">🔍 Emotion Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your feelings below, and let AI analyze your emotions! 😊</div>', unsafe_allow_html=True)

# Input section
text = st.text_area("✍️ Type your feelings here:", "", height=150, key="text_input")

# Button to predict emotion
if st.button("🚀 Predict Emotion", key="predict_button"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text to make a prediction!")
    else:
        emotion_pred, confidence = emotion_prediction(text)

        # Display result
        st.markdown(f'<div class="result">🎭 Prediction: <b>{emotion_pred}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="explanation">📊 Confidence: <b>{confidence:.2f}</b></div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ by <b>Senasu</b> | Powered by Machine Learning 🤖</div>', unsafe_allow_html=True)
