import speech_recognition as sr
import openai
from dotenv import load_dotenv
import os
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  # Adjust speech rate
load_dotenv()  
openai.api_key = os.getenv("OPENAI_API_KEY")  


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
        print(f"Error connecting to ChatGPT: {e}")
        return "Sorry, I couldn't connect to ChatGPT."


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"Command interpreted: {command}")  # Debugging line
            if 'whisper' in command:
                command = command.replace('whisper', '')
                print(command)
    except Exception as e:
        print(f"Error: {e}")
        return ''
    return command


def run_whisper():
    command = take_command()
    if not command:
        return  # Skip if no command is recognized
    
    print(f"Received command: {command}")

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time_str = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time_str)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry, I have a headache')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'chat' in command or 'question' in command:
        prompt = command.replace('chat', '').replace('question', '')
        response = ask_chatgpt(prompt)
        print(response)
        talk(response[:200])

    # AI ITINERARY AND LIFE PLANNER
    elif 'plan my trip' in command or 'trip itinerary' in command:
        prompt = command.replace('plan my trip', 'Plan a detailed travel itinerary').replace('trip itinerary', '')
        response = ask_chatgpt(prompt)
        print(response)
        talk(response[:200])  
    
    elif 'plan my week' in command:
        prompt = "Plan my week, I have university on Monday, Wednesday, and Friday, work on Tuesday and Thursday, and I need time for studying, exercise, and personal care."
        response = ask_chatgpt(prompt)
        print(response)
        talk(response[:200])
    
    elif 'plan my day' in command:
        prompt = "Plan my day. I have university from 9 AM to 5 PM, work out at 6 PM, and need time for studying, eating, and personal time."
        response = ask_chatgpt(prompt)
        print(response)
        talk("Here's your schedule for the day: " + response[:200])  
    
    elif 'give me a schedule' in command:
        prompt = "Give me a schedule for today based on my tasks and personal goals. I have university in the morning, work in the afternoon, and need time to relax."
        response = ask_chatgpt(prompt)
        print(response)
        talk("Here's your schedule: " + response[:200])  
    
    elif 'plan my week with goals' in command:
        prompt = "Plan my week considering that I need to focus more on studying for my exams and less on work."
        response = ask_chatgpt(prompt)
        print(response)
        talk("Here's your week plan based on your goals: " + response[:200])


    # AI STUDY BUDDY 
    elif 'teach me' in command or 'explain' in command:
        prompt = "Explain like a tutor: " + command
        response = ask_chatgpt(prompt)
        print(response)
        talk(response[:200])

    elif 'quiz me on' in command:
        topic = command.replace('quiz me on', '')
        prompt = f"Give me a 3-question multiple choice quiz on {topic}. Include answers."
        response = ask_chatgpt(prompt)
        print(response)
        talk("Here's your quiz. " + response[:200])

    # AI THERAPIST
    elif 'i feel' in command or 'i am feeling' in command:
        prompt = "I'm your compassionate therapist. Respond to this kindly: " + command
        response = ask_chatgpt(prompt)
        print(response)
        talk(response[:200])

    elif 'give me an affirmation' in command:
        response = ask_chatgpt("Give me a positive affirmation for today.")
        talk(response)

    # AI FITNESS TRACKER
    elif 'fitness plan' in command or 'workout' in command:
        prompt = "Create a 7-day fitness plan with home exercises and diet tips."
        response = ask_chatgpt(prompt)
        print(response)
        talk("Here’s your fitness plan.")
    
    elif 'track my fitness' in command or 'fitness goal' in command:
        prompt = "Track my fitness goal: " + command
        response = ask_chatgpt(prompt)
        print(response)
        talk(response[:200])

    else:
        talk('Please say the command again.')


while True:
    run_whisper()
    time.sleep(1)  # Adding a small delay to prevent fast consecutive calls
