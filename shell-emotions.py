import os , time
import psutil
from threading import Thread
import signal
import sys
from lib import animation, emotions, statemanager

# Method to shutdown program
def shutdown(signum, frame):
    print(" Shutting Down...")
    sys.exit(0)

# Main function to handle signals and start threads
def main():
    statemanager.init()
    st = statemanager.statemanager
    anim = animation.animation
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    # Starting threads
    util_thread = Thread(target=st.state_update, args=(st.state_update, "STATE UPDATE THREAD",))
    emote_thread = Thread(target=anim.run, args=(anim.run, ))
    util_thread.setDaemon(True)
    emote_thread.setDaemon(True)

    util_thread.start()
    emote_thread.start()
    util_thread.join()
    emote_thread.join()

if __name__ == "__main__":
    main()
