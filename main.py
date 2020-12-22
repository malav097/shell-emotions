import os , time
import psutil
from threading import Thread
import signal
import sys


# Importing frames and Initializing file paths and global state
files   = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
frames  = []
sleepy_frames = []
awake_frames = []
sleepy_ind = [0, 7]
awake_ind = [0, 1, 4, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 5, 6, 7]
state = 0
frames_path = "./assets/frames/"
working_dir = os.path.dirname(__file__)

# Opening files and setting up animation frame arrays
for name in files:
    filepath = frames_path + name
    print(filepath)
    rel_path = os.path.relpath(filepath, working_dir)
    with open(rel_path, "r", encoding="utf8") as f:
        #sabe every line in list "f"
        f = f.readlines()
        #append list f to list frames
        frames.append(f)

for ind in awake_ind: # Setting up Awake frames
    awake_frames.append(frames[ind])

for i in range(5): # Setting up Asleep frames
    for ind in sleepy_ind:
        sleepy_frames.append(frames[ind])


# Method to refresh utilization values
def state_update(thread_name):
    global state
    while True:
        cpu_percent = psutil.cpu_percent(1)
        if (cpu_percent <= 10): # Sleepy Animation
            state = 0
        elif (cpu_percent > 10 and cpu_percent < 30): # Waking Up
            state = 1
        elif (cpu_percent >= 30): # Fully Awake
            state = 2
        time.sleep(5)


# Method to print and update emotion animation
def emote(thread_name):
    while True:
        if (state == 0): # Sleepy Animation
            for frame in sleepy_frames:
                os.system('printf "\033c"')
                print("".join(frame))
                time.sleep(0.2)
        elif (state == 1): # Waking Up
            for frame in frames:
                #clear the shell
                os.system('printf "\033c"') #printf "\033c"') 
                print("".join(frame))
                #print(" TEST ")
                time.sleep(0.2)
                #clear the shell
        elif (state == 2): # Awake
            for frame in awake_frames:
                os.system('printf "\033c"')
                print("".join(frame))
                time.sleep(0.2)


# Method to shutdown program
def shutdown(signum, frame):
    print(" Shutting Down...")
    sys.exit(0)


# Main function to handle signals and start threads
def main():
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    # Starting threads
    util_thread = Thread(target=state_update, args=("UTILIZATION CHECK THREAD",))
    emote_thread = Thread(target=emote, args=("EMOTION PRINT THREAD",))
    util_thread.setDaemon(True)
    emote_thread.setDaemon(True)

    util_thread.start()
    emote_thread.start()
    util_thread.join()
    emote_thread.join()

if __name__ == "__main__":
    main()
