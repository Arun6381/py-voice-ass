import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recon = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening......")
        audio = recon.listen(source)

        data = " "

        try:
            data = recon.recognize_google(audio)
            print("you said: " + data)

        except sr.UnknownValueError:
            print("Assistant could not understand.")

        except sr.RequestError as ex:
            print("Request Error from Google: " + str(ex))

        return data

def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)

def call(text):
    action_call = "a"

    text = text.lower()

    if action_call in text:
        return True

    return False

def today_data():
    now = datetime.datetime.now()
    date_now = now.date()
    week_now = calendar.day_name[now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    ordinals = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
        "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
        "24", "25", "26", "27", "28", "29", "30", "31"
    ]

    return f'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.'

def say_hello(text):
    greet = ["hi", "hello", "greeting", "hey", "what's good"]
    response = ["hi", "hello", "greeting", "hey", "what's good"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


while True:
    try:
        text = rec_audio()
        speak = " "
        if call(text):
            speak += say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_data()
                speak += " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meriden = "p.m" if now.hour >= 12 else "a.m"

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)

                speak += " " + f"It is {now.hour}:{minute} {meriden}."

            elif "wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    try:
                        wiki = wikipedia.summary(person, sentences=2)
                        speak += " " + wiki
                    except wikipedia.exceptions.DisambiguationError as e:
                        speak += " " + f"There is a disambiguation for {person}. Please be more specific."
                    except wikipedia.exceptions.PageError as e:
                        speak += " " + f"Sorry, I couldn't find information about {person}."
                    except Exception as e:
                        speak += " " + f"An error occurred: {str(e)}"

            elif "who are you " in text or "define yourself" in text:
                speak = speak + " hello, I am assistant. your assistant."

            elif "your name" in text:
                speak = speak + "my name is a"

            elif "who am i" in text:
                speak = speak + "you must probably be a human"

            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secret"

            elif "how are you" in text:
                speak = speak + "i am fine, thank you"
                speak = speak +"\nhow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "it's good to know that you are fine"

            response(speak)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        talk("I don't know that")
