import os , time, psutil, signal, sys
from threading import Thread
from lib.animation import Animation


# Importing frames and Initializing file paths and global state
emotion_names = ["sleep", "waking", "awake", "rage"]
emotions = {}
state = 0
frames_path = "./assets/frames/"


# Method to refresh utilization values
def state_update(thread_name):
    global state
    while True:
        cpu_percent = psutil.cpu_percent(1)
        if (cpu_percent <= 10): # Sleep
            state = emotions["sleep"].id
        elif (cpu_percent > 10 and cpu_percent <= 30): # Waking
            state = emotions["waking"].id
        elif (cpu_percent > 30 and cpu_percent <= 90): # Awake
            state = emotions["awake"].id
        elif (cpu_percent > 90): # Rage
            state = emotions["rage"].id
        time.sleep(5)


# Method to print frames given a key
def print_frames(key):
    frames = emotions[key].frames
    for frame in frames:
        os.system('printf "\033c"')
        print("".join(frame))
        time.sleep(0.2)


# Method to print and update emotion animation
def emote(thread_name):
    while True:
        for key, val in emotions.items():
            if (state == val.id):
                print_frames(key)


# Method to shutdown program
def shutdown(signum, frame):
    print(" Shutting Down...")
    sys.exit(0)


# Main function to handle signals and start threads
def main():
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    for i in range(len(emotion_names)):
        emotions.update({emotion_names[i] : Animation(emotion_names[i], i, frames_path)})

    util_thread = Thread(target=state_update, args=("STATE UPDATE THREAD",))
    emote_thread = Thread(target=emote, args=("EMOTION PRINT THREAD",))
    util_thread.setDaemon(True)
    emote_thread.setDaemon(True)

    util_thread.start()
    emote_thread.start()
    util_thread.join()
    emote_thread.join()


if __name__ == "__main__":
    main()
