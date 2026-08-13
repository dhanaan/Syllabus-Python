import time
import datetime
import pygame
import take_input as inp

def set_alarm(alarm_time, sound_file, msg="ALARM RINGS"):
    print(f"Alarm set for {alarm_time}")
    sound_file = sound_file

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f'\r{current_time}', end="", flush=True)
        time.sleep(1)
        if current_time == alarm_time:
            print(f"\n{msg}")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            inp.take_input("Enter to turn off the alarm: ")
            pygame.mixer.music.stop()
            break
            

if __name__ == "__main__":
    alarm_time = inp.take_input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time, sound_file = "Attack of the Killer Queen.mp3", msg = "Wake up!!!")