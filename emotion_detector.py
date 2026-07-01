import csv
import os
from datetime import datetime

def detect_emotion(text):
    text = text.lower()

    emotions = {
        "Confused": ["stuck", "confused", "lost", "don't understand"],
        "Bored": ["boring", "sleepy", "dull"],
        "Confident": ["easy", "solved", "understand", "confident"],
        "Curious": ["want to learn", "interested", "curious", "explore"],
        "Frustrated": ["frustrated", "annoyed", "angry", "irritated", "error"]
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


#user_input = input("Enter your problem: ")
#emotion_scores = detect_emotion(user_input)

#print("Detected Emotions:")
#for emotion, score in emotion_scores.items():
#   print(f"{emotion}: {score}%")

# Save to CSV
file_path = "logs/interaction_logs.csv"
file_exists = os.path.isfile(file_path)

with open(file_path, mode="a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Timestamp", "User Input", "Emotion"])

    writer.writerow([datetime.now(), user_input, emotion])

print("Saved to logs successfully!")
