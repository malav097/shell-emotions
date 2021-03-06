import os, signal, sys
from threading import Thread
from lib.animation import Animation
from lib.threading import *
from lib.welcome import print_welcome
from conf.cfg import *


# Method to shutdown program
def shutdown(signum, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" Shutting Down...")
    sys.exit(0)


# Main function to handle signals and start threads
def main():
    # Catching SIGINT and SIGTERM signals
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    # Loading emotions and frames into emotions dictionary
    emotions = {}
    emotion_names = os.listdir(frames_path)
    for i in range(len(emotion_names)):
        emotions.update({emotion_names[i] : Animation(emotion_names[i], i, frames_path)})

    print_welcome()
    time.sleep(welcome_time)

    # Starting threads
    util_thread = Thread(target=state_update, args=("STATE UPDATE THREAD", emotions))
    emote_thread = Thread(target=emote, args=("EMOTION PRINT THREAD", emotions))
    util_thread.setDaemon(True)
    emote_thread.setDaemon(True)

    util_thread.start()
    emote_thread.start()

    # Keeping main thread active for signal handling
    try:
        while True:
            signal.pause()
    except AttributeError: # Windows lacks .pause()
        while True:
            time.sleep(1)


if __name__ == "__main__":
    main()
