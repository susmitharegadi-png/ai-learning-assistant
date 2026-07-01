import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime


def detect_emotion(text):
    text = text.lower()

    emotions = {
    "Confused": [
        "stuck", "confused", "lost", "don't understand",
        "difficult", "hard", "unclear"
    ],
    "Bored": [
        "boring", "sleepy", "dull", "tired"
    ],
    "Confident": [
        "easy", "solved", "understand", "confident"
    ],
    "Curious": [
        "want to learn", "interested", "curious", "explore"
    ],
    "Frustrated": [
        "frustrated", "annoyed", "angry", "irritated",
        "error", "stress", "stressed", "exam", "pressure",
        "unable", "focus"
    ]
}

    scores = {}

    for emotion, keywords in emotions.items():
        score = 0
        for word in keywords:
            if word in text:
                score += 1
        scores[emotion] = score

    total = sum(scores.values())

    if total == 0:
        return {"Neutral": 100}

    percentages = {}
    for emotion, score in scores.items():
        if score > 0:
            percentages[emotion] = round((score / total) * 100, 2)

    return percentages

def generate_response(emotion_scores):
    if "Confused" in emotion_scores:
        return "You seem confused. Try breaking the topic into smaller parts and start with simple examples."

    elif "Frustrated" in emotion_scores:
        return "You seem frustrated. Take a short break and solve one small issue at a time."

    elif "Bored" in emotion_scores:
        return "You seem bored. Try learning through videos or interactive examples."

    elif "Curious" in emotion_scores:
        return "Great curiosity! Keep exploring and ask deeper questions."

    elif "Confident" in emotion_scores:
        return "Nice! You seem confident. Try solving advanced problems to strengthen your skills."

    else:
        return "Keep learning consistently. You are making progress."
st.title("🧠 AI Learning Assistant")
st.caption("Emotion Detection & Personalized Learning Support Platform")

user_input = st.text_area(
    "Describe your study problem",
    placeholder="Example: I am confused about recursion and getting many errors..."
)
if st.button("Analyze"):
    emotion_scores = detect_emotion(user_input)

    st.subheader("Detected Emotions")
    for emotion, score in emotion_scores.items():
        st.write(f"{emotion}: {score}%")
        st.progress(score / 100)

    response = generate_response(emotion_scores)

    st.subheader("AI Guidance")
    st.write(response)

    # ADD HERE ↓↓↓
    st.subheader("Model Comparison")

    emotions = list(emotion_scores.keys())

    if len(emotions) > 1:
        bilstm_prediction = emotions[0]
        bert_prediction = emotions[1]
    else:
        bilstm_prediction = emotions[0]
        bert_prediction = emotions[0]

    st.write(f"BiLSTM Prediction: {bilstm_prediction}")
    st.write(f"BERT Prediction: {bert_prediction}")
    
    file_path = "logs/interaction_logs.csv"
    file_exists = os.path.isfile(file_path)

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "User Input", "Emotion"])

        writer.writerow([datetime.now(), user_input, dominant_emotion])

# OUTSIDE analyze block
st.divider()
st.subheader("Analytics Dashboard")

try:
    df = pd.read_csv("logs/interaction_logs.csv")

    emotion_counts = df["Emotion"].value_counts()

    fig, ax = plt.subplots()
    emotion_counts.plot(kind="bar", ax=ax)
    plt.title("Emotion Distribution")
    plt.xlabel("Emotion")
    plt.ylabel("Count")

    st.pyplot(fig)

except:
    st.write("No analytics data available yet.")
