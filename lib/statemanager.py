import psutil, time

def init():
    global state
    state = 0

class statemanager:
    def state_update(self, thread_name):
        while True:
            cpu_percent = psutil.cpu_percent(1)
            if (cpu_percent <= 10): # Sleepy Animation
                state = 0
                print("0")
            elif (cpu_percent > 10 and cpu_percent <= 30): # Waking Up
                state = 1
                print("1")
            elif (cpu_percent > 30 and cpu_percent <= 90): # Fully Awake
                state = 2
                print("2")
            elif (cpu_percent > 90): # Rage
                state = 3
                print("3")
            time.sleep(5)