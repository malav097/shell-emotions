import os , time
import psutil
from threading import Thread

# Importing frames and Initializing file paths
files   = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
frames  = []
sleepy_frames = []
awake_frames = []
sleepy_ind = [0, 7]
awake_ind = [0, 1, 4, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 5, 6, 7]
cpu_percent = 0
flag_busy = 0
frames_path = "./assets/frames/"
working_dir = os.path.dirname(__file__)

for name in files:
    filepath = frames_path + name
    print(filepath)
    rel_path = os.path.relpath(filepath, working_dir)
    with open(rel_path, "r", encoding="utf8") as f:
        #sabe every line in list "f"
        f = f.readlines()
        #append list f to list frames
        frames.append(f)

for ind in awake_ind:
    awake_frames.append(frames[ind])

for i in range(5):
    for ind in sleepy_ind:
        sleepy_frames.append(frames[ind])

# Method to refresh utilization values
def check_usage(thread_name):
    global cpu_percent
    while True:
        flag_busy = 1
        cpu_percent = psutil.cpu_percent(1)
        flag_busy = 0
        time.sleep(5)

# Method to print and update emotion animation
def emote(thread_name):
    prev_state = 0
    while True:
        if (flag_busy == 1):
            state = prev_state
        else:
            if (cpu_percent <= 10): # Sleepy Animation
                state = 0
            elif (cpu_percent > 10 and cpu_percent < 20): # Waking Up
                state = 1
            elif (cpu_percent >= 30):
                state = 2
        
        if (state == 0): # Sleepy Animation
            for frame in sleepy_frames:
                os.system('printf "\033c"')
                print("".join(frame))
                time.sleep(0.2)
            prev_state = 0
        elif (state == 1): # Waking Up
            for frame in frames:
                #clear the shell
                os.system('printf "\033c"') #printf "\033c"') 
                print("".join(frame))
                #print(" TEST ")
                time.sleep(0.2)
                #clear the shell
            prev_state = 1
        elif (state == 2):
            for frame in awake_frames:
                os.system('printf "\033c"')
                print("".join(frame))
                time.sleep(0.2)
            prev_state = 2

# Starting threads
util_thread = Thread(target=check_usage, args=("UTILIZATION CHECK THREAD",))
emote_thread = Thread(target=emote, args=("EMOTION PRINT THREAD",))

util_thread.start()
emote_thread.start()
util_thread.join()
emote_thread.join()

