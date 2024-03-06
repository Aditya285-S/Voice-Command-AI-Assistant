import datetime
from playsound import playsound


print("What time sir?")
time = input(":Enter Time:")
while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if time == now:
        print("Wake up.")
        playsound('C:\\Atharv\\College Material\\Python For Engineers\\HAAAC\\alarm.mp3')
        print("Alarm Stopped")
        break
    elif time < now:
        break