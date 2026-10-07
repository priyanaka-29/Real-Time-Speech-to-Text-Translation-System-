# Speech-to-Text Translation System

## 📌 Project Overview

This project is a Speech-to-Text Translation application that converts spoken audio into text and translates the recognized speech into another language.

The system uses **Whisper** for speech recognition and **Transformer-based models** for translation. A **FastAPI** backend is used to connect the AI processing pipeline with the application.

## 🚀 Features

- 🎤 Convert speech/audio into text
- 🌐 Translate the recognized text into another language
- 🤖 Uses Whisper for speech recognition
- 🔄 Uses Transformer models for translation
- ⚡ FastAPI-based backend
- 🌍 Supports multilingual speech processing
- 📊 Uses Pandas for data processing

## 🛠️ Technologies Used

- **Python**
- **Whisper**
- **Transformer Models**
- **Hugging Face**
- **PyTorch**
- **Pandas**
- **FastAPI**

## 🔄 Workflow

```text
Audio Input
    ↓
Speech Recognition using Whisper
    ↓
Generated Text
    ↓
Translation using Transformer Model
    ↓
Translated Text
    ↓
Output
```

## 📂 Project Structure

```text
Speech-to-Text-Translation/
│
├── app/
│   ├── main.py
│   └── ...
│
├── models/
│   └── ...
│
├── requirements.txt
├── README.md
└── ...
```

> The project structure may vary depending on the implementation.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/speech-to-text-translation.git
cd speech-to-text-translation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

## 🧠 How It Works

1. The user provides an audio file or speech input.
2. Whisper processes the audio and converts speech into text.
3. The generated text is passed to a Transformer-based translation model.
4. The translation model converts the text into the target language.
5. The translated output is returned through the application.

## 🎯 Applications

- Multilingual communication
- Voice-based translation
- Educational applications
- Accessibility solutions
- Language learning
- Speech processing applications

## 🔮 Future Improvements

- Add support for more languages.
- Add real-time microphone input.
- Improve translation quality.
- Add a user-friendly web interface.
- Deploy the application to a cloud platform.

## 👩‍💻 Author

**Podugu Priyanka**

MCA – Artificial Intelligence & Machine Learning

GitHub: https://github.com/priyanaka-29
