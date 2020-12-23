import os, time, psutil, signal, sys
from threading import Thread
from lib.animation import Animation
from lib.threading import *
from conf.cfg import *


# Method to shutdown program
def shutdown(signum, frame):
    print(" Shutting Down...")
    sys.exit(0)


# Main function to handle signals and start threads
def main():
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    emotion_names = os.listdir(frames_path)
    for i in range(len(emotion_names)):
        emotions.update({emotion_names[i] : Animation(emotion_names[i], i, frames_path)})

    # Starting threads
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
