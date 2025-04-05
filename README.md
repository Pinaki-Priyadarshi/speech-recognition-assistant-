# speech-recognition-assistant-

# 🗣️ Voice-Controlled Assistant using Python

This is a fun and functional mini-project where I built a **voice assistant** that listens to your commands and plays YouTube videos—all using Python!

---

## 🎯 What It Does

- Listens to voice input using your system microphone
- Converts speech to text using Google Speech Recognition
- Detects trigger keywords like "play" or custom words like "peepee"
- Plays the requested song on YouTube using pywhatkit
- Gives voice feedback using pyttsx3

---

## 🧰 Technologies Used

- `speech_recognition` – Speech-to-text
- `pyttsx3` – Text-to-speech (offline)
- `pywhatkit` – Opens YouTube and plays requested video
- `pyaudio` – For accessing the microphone

---

## 🛠️ How to Run

1. Clone the repo  
2. Install dependencies  
3. Run the script

```bash
git clone https://github.com/yourusername/speech-recognition-assistant.git
cd speech-recognition-assistant
pip install -r requirements.txt
python voice_assistant.py
