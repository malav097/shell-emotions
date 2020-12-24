from conf.cfg import *
import time
import psutil

# Method to refresh utilization values
def state_update(thread_name):
    global state
    while True:
        cpu_percent = psutil.cpu_percent(1)
        if (cpu_percent <= cpu_lvl_1): # Sleep
            state = emotions["sleep"].id
        elif (cpu_percent > cpu_lvl_1 and cpu_percent <= cpu_lvl_2): # Waking
            state = emotions["waking"].id
        elif (cpu_percent > cpu_lvl_2 and cpu_percent <= cpu_lvl_3): # Awake
            state = emotions["awake"].id
        elif (cpu_percent > cpu_lvl_3): # Rage
            state = emotions["rage"].id
        time.sleep(util_refresh)


# Method to print frames given a key
def print_frames(key):
    frames = emotions[key].frames
    for frame in frames:
        print('\033c')
        print("".join(frame))
        time.sleep(frame_time)


# Method to print and update emotion animation
def emote(thread_name):
    while True:
        for key, val in emotions.items():
            if (state == val.id):
                print_frames(key)
