import pyttsx3
from playsound import playsound

assistant =pyttsx3.init("sapi5")
voices = assistant.getProperty("voices")
assistant.setProperty("voices", voices[0].id)

def speak(sound):
    '''
    this function will spek up content and it will read loudly
    '''
    assistant.say(sound)
    assistant.runAndWait()

if __name__ == "__main__":
    print("What is computer's favorite beat?")
    speak("What is computer's favorite beat?")
    print()
    print("An Algo-rythm ")
    speak("An Algo - rythm ")
    playsound("C:\\Atharv\\College Material\\Python For Engineers\\HAAAC\\laugh.wav")