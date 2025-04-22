from flask import Flask, render_template, request, jsonify
import openai
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return "Sorry, I couldn't connect to ChatGPT."

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run_assistant", methods=["POST"])
def run_assistant():
    command = request.form.get("command").lower()

    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        return jsonify({"response": f'Playing {song}'})
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return jsonify({"response": f'Current time is {time}'})
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        return jsonify({"response": info})
    elif 'joke' in command:
        return jsonify({"response": pyjokes.get_joke()})
    elif 'chat' in command or 'question' in command:
        prompt = command.replace('chat', '').replace('question', '')
        response = ask_chatgpt(prompt)
        return jsonify({"response": response})
    else:
        return jsonify({"response": 'Sorry, I didn’t catch that. Can you repeat?'})

if __name__ == "__main__":
    app.run(debug=True)
