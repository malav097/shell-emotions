import time, psutil, sys
from conf.cfg import *
from sys import platform
disable_cpu_temp = False
handle = None
if (platform == "win32"):
    try:
        import clr
        from lib.win32_temp import *
        handle = init_open_hwd_mon()
    except:
        disable_cpu_temp = True
    if (handle == None):
        disable_cpu_temp = True


def get_cpu_temp(handle):
    if (platform == "linux" or platform == "linux2"):
        try:
            temp = psutil.sensors_temperatures()[cpu_temp_sensor]
            temp_list = []
            for i in range(len(temp)):
                temp_list.append(temp[i].current)
            avg_cpu_temp = sum(temp_list)/len(temp_list)
        except:
            avg_cpu_temp = cpu_temp_default
        return avg_cpu_temp
    elif (platform == "win32"):
        cpu_temp = get_cpu_pkg_temp(handle)
        return cpu_temp
    else:
        return cpu_temp_default


# Method to refresh utilization values
def state_update(thread_name, emotions):
    global state
    while True:
        cpu_percent = psutil.cpu_percent(cpu_usage_time)
        mem_percent = psutil.virtual_memory().percent
        if (disable_cpu_temp):
            cpu_temp = cpu_temp_default
        else:
            cpu_temp = get_cpu_temp(handle)
        if (cpu_percent <= cpu_lvl_1): # Sleep
            state = emotions["sleep"].id
        elif (cpu_percent > cpu_lvl_1 and cpu_percent <= cpu_lvl_2): # Waking
            state = emotions["waking"].id
        elif (cpu_percent > cpu_lvl_2 and cpu_percent <= cpu_lvl_3): # Awake
            if (cpu_temp > cpu_temp_bound):
                if (mem_percent > mem_bound): # Hot Variant
                    state = emotions["reading_hot"].id
                else:
                    state = emotions["awake_hot"].id
            else:
                if (mem_percent > mem_bound):
                    state = emotions["reading"].id
                else:
                    state = emotions["awake"].id
        elif (cpu_percent > cpu_lvl_3): # Rage
            if (cpu_temp > cpu_temp_bound): # Hot Variant
                state = emotions["rage_hot"].id
            else:
                state = emotions["rage"].id
        time.sleep(util_refresh)


# Method to print and update emotion animation
def emote(thread_name, emotions):
    while True:
        for key, val in emotions.items():
            if (state == val.id):
                val.play(frame_time)
