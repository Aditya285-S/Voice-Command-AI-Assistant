import os
import speech_recognition as sr

def takeinput():
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        a.pause_threshold=1
        audio=a.listen(source)

    try:
        print("Recognizing...")
        problem= a.recognize_google(audio, language="en-in")
        print(problem)

    except Exception:
        print("Sir please say that again...")
        return "None"
    return problem

while True:
     
    wake_up=takeinput()

    if "wake up" in wake_up:
        os.startfile("C:\\Atharv\\College Material\\Python For Engineers\\HAAAC\\haaac.py")

    else:
        print("None...")