import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from playsound import playsound
from googletrans import Translator


assistant =pyttsx3.init("sapi5")
voices = assistant.getProperty("voices")
assistant.setProperty("voices", voices[0].id)

def speak(sound):
    '''
    this function will spek up content and it will read loudly
    '''
    assistant.say(sound)
    assistant.runAndWait()

def greeting():
    time = int(datetime.datetime.now().hour)
    
    if time>=0 and time<12:
        print("Good Morning")
        speak("Good Morning")
    elif time>=12 and time<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    
def order():
    '''
    take speech input from user and convert it into string
    '''
    read = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now. I am listening...")
        read.pause_threshold = 1
        sound = read.listen(source)
    try:
        print("Recognising...")
        problem = read.recognize_google(sound, language='en-in')
        print("I heard:" + problem + "\n")
        
    except Exception:
        print("I am unable to understand. Please speak again")
        return "None"
    return problem

def marathiOrder():
    '''For translating'''
    read = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now. I am listening...")
        read.pause_threshold = 1
        sound = read.listen(source)
    try:
        print("Recognising...")
        problem = read.recognize_google(sound, language='mr')
        print("I heard:" + problem + "\n")
        
    except Exception:
        return "None"
    return problem.lower()

def Tran():
    print("Tell me!")
    speak("Tell me!")
    line = marathiOrder()
    translator = Translator()
    results =translator.translate(line)
    print(results.text)
    speak(results.text)



greeting()
print("How can I help you?")
speak("How can I help you?")

while True:
    problem = order().lower()
    if __name__ == "__main__":
        if "wikipedia" in problem:
            print("Searching on the web... ")
            speak("Searching on the web... ")
            problem = problem.replace("wikipedia" , "")
            result = wikipedia.summary(problem, sentences=2)
            print("Here's what I found:" + result)
            speak("Here's what I found:")
            speak(result)

        elif "open youtube" in problem:
            webbrowser.open("youtube.com")
        elif "open email" in problem:
            webbrowser.open("mail.google.com")
        elif "open google" in problem:
            webbrowser.open("google.com")
        elif "open python documentation" in problem:
            webbrowser.open("pypi.org")
        elif "open stack overflow" in problem:
            webbrowser.open("stackoverflow.com")
        elif "open geeksforgeeks" in problem:
            webbrowser.open("geeksforgeeks.com")
        elif "open classroom" in problem:
            webbrowser.open("https://classroom.google.com/h")

        elif "open vs code" in problem:
            vsCode= "C:\\Users\\atharvtembhurnikar\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCode)
        elif "open word" in problem:
            word= "C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(word)
        elif "open game" in problem:
            game= "C:\\Atharv\\College Material\\Python For Engineers\\HAAAC\\RockPaperScissor.py"
            os.startfile(game)
        
        elif "what day is today" in problem:
            day = int(datetime.datetime.today().weekday())
            weekdays= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            print("Today is", weekdays[day])
            speak("Today is"+ weekdays[day])
        elif "time" in problem:
            strTime = datetime.datetime.now().strftime("%H %M")   
            speak("The time is :" + strTime)
        elif "open translator" in problem:
            Tran()

        elif "set alarm" in problem:
            print("What time sir?")
            time = input(":Enter Time:")
            print("Wake up.")
            playsound('C:\\Atharv\\College Material\\Python For Engineers\\HAAAC\\alarm.mp3')
            print("Alarm Stopped")

        elif "introduce yourself" in problem:
            print("My name is HAAAC. I am your AI Assistant.")
            speak("My name is HACK. I am your AI Assistant.")
        elif "where do you live" in problem:
            print("I live in your heart.")
            speak("I live in your heart.")
        elif "tell me a joke" in problem:
            print("What is computer's favorite beat?")
            speak("What is computer's favorite beat?")
            print()
            print("An Algo-rythm ")
            speak("An Algo - rythm ")
            playsound("C:\\Atharv\\College Material\\Python For Engineers\\HAAAC\\laugh.wav")
        elif "take a break" in problem:
            print("Ok sir. bye.")
            speak("Ok sir, bye. ")
            break