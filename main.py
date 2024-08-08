import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()
speak("hi iam praga, what i can do for u")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 0.5)
    print("Listening....")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("arun:", text)
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

if "what" and "about" and "you" in text:
    speak("i am  good")
speak("what can i do for you")