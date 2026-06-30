# Environment Setup

## Overview

This document explains how to set up the development environment for the **Emotion Detection & Learning Support Engine** project.

---

## 1. Install Python

Install **Python 3.9 or above**.

Official Download:
https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

---

## 2. Create a Virtual Environment

Create a virtual environment to isolate project dependencies.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Required Libraries

Install all required dependencies using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

## 4. Install Streamlit

If Streamlit is not included in `requirements.txt`, install it manually.

```bash
pip install streamlit
```

Official Documentation:

https://docs.streamlit.io/library/get-started/installation

---

## 5. Verify Model and Dataset Files

Ensure the following folders exist in the project.

```text
project/
│
├── data/
├── models/
│   ├── bilstm/
│   └── bert_emotion_model_final/
```

The project requires:

- BiLSTM model files
- BERT model weights
- Tokenizer
- Dataset files

---

## 6. Configure Gemini API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Generate your API key from:

https://aistudio.google.com/

---

## 7. Recommended Development Tools

The following IDEs are recommended:

- Visual Studio Code
- PyCharm Community Edition

These tools provide:

- Python debugging
- Virtual environment support
- Code completion
- Project navigation
- Git integration

---

## 8. Verify Installation

Run the Streamlit application.

```bash
streamlit run app.py
```

If the application opens successfully in your browser, the environment setup is complete.

---

## Project Structure

```text
Emotion-Detection-Learning-Support-Engine/
│
├── app.py
├── requirements.txt
├── .env
├── data/
├── models/
│   ├── bilstm/
│   └── bert_emotion_model_final/
├── utils/
└── logs/
```

## Conclusion

After completing these steps, the development environment is ready for model loading, emotion prediction, Gemini AI integration, and execution of the Streamlit application.
