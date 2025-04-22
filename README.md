# 🔊 WhisprAI: Voice Assistant with ChatGPT Integration

WhisprAI is a sleek, voice-activated assistant powered by OpenAI's GPT-3.5. It listens to your commands, responds intelligently, and performs a range of tasks from playing music to planning your day — all through voice.

---

## ✨ Features

- 🎙️ **Voice Command Recognition** — Understands and responds to spoken commands.
- 🤖 **GPT-3.5 Intelligence** — Integrated with ChatGPT for smart, conversational replies.
- 🎵 **Music Playback** — Plays music on YouTube using `pywhatkit`.
- 😂 **Joke Teller** — Brightens your day with jokes from the `pyjokes` library.
- 🕐 **Real-time Info** — Tells the time, date, and Wikipedia summaries.
- 🧠 **Study Assistant** — Explains concepts, quizzes you, and makes study plans.
- 🌿 **Mental Wellness Support** — Sends positive affirmations and gentle encouragement.
- 💪 **Fitness Tracker** — Generates personalized fitness routines and goals.
- 🌍 **AI Travel Planner** — Plans your day or week, including custom itineraries.

---

## 🧰 Tech Stack

| Purpose             | Library / API         |
|---------------------|------------------------|
| Voice to Text       | `speech_recognition`   |
| Text to Voice       | `pyttsx3`              |
| Music Playback      | `pywhatkit`            |
| Jokes               | `pyjokes`              |
| Info Summaries      | `wikipedia`            |
| AI Conversations    | `openai`               |
| Environment Variables| `python-dotenv`        |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/arshitadewan7/whisprAI.git
cd whisprAI
2. Install Dependencies
pip install -r requirements.txt
3. Set Your OpenAI API Key
Create a .env file in the root directory:

OPENAI_API_KEY=your-openai-api-key-here
✅ Be sure to add .env to .gitignore to keep your key secure.
4. Run the Assistant
python main.py
Now speak the word "Whisper" followed by your command!

🧠 Example Commands

“Whisper, play Coldplay on YouTube.”
“Whisper, what’s the time?”
“Whisper, tell me a joke.”
“Whisper, help me study math.”
“Whisper, plan my trip to Melbourne.”
⚠️ Known Issues

📱 Mobile support is limited; The mobile-friendly version of the app is still in progress and is not fully functional for all devices.
🎤 Speech recognition may vary based on mic quality/environment.
💡 Ideas or Contributions?

Pull requests and issues are welcome! Let’s make WhisperAI even better together.

📄 License

MIT License — feel free to fork and build upon it.

🤝 Connect with Me

GitHub: @arshitadewan7
