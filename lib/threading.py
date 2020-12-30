import time, psutil, sys
from conf.cfg import *
from sys import platform


def get_cpu_temp():
    if (platform == "linux" or platform == "linux2"):
        try:
            temp = psutil.sensors_temperatures()[cpu_temp_sensor]
            temp_list = []
            for i in range(len(temp)):
                temp_list.append(temp[i].current)
            avg_cpu_temp = sum(temp_list)/len(temp_list)
        except:
            avg_cpu_temp = 0
        return avg_cpu_temp
    elif (platform == "win32"):
        try:
            w = wmi.WMI(namespace=r'root\wmi')
            temp = w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature
            cpu_temp = (temp / 10) - 273.15
        except:
            cpu_temp = 0
        return cpu_temp
    else:
        return 0


# Method to refresh utilization values
def state_update(thread_name, emotions):
    global state
    disable_cpu_temp = False
    if (platform == "win32"):
        try:
            import wmi
        except:
            disable_cpu_temp = True
    while True:
        cpu_percent = psutil.cpu_percent(cpu_usage_time)
        mem_percent = psutil.virtual_memory().percent
        if (disable_cpu_temp):
            cpu_temp = 0
        else:
            cpu_temp = get_cpu_temp()
        if (cpu_temp > cpu_temp_bound):
            state = emotions["embarrassed"].id
        else:
            if (cpu_percent <= cpu_lvl_1): # Sleep
                state = emotions["sleep"].id
            elif (cpu_percent > cpu_lvl_1 and cpu_percent <= cpu_lvl_2): # Waking
                state = emotions["waking"].id
            elif (cpu_percent > cpu_lvl_2 and cpu_percent <= cpu_lvl_3): # Awake
                if (mem_percent > mem_bound):
                    state = emotions["reading"].id
                else:
                    state = emotions["awake"].id
            elif (cpu_percent > cpu_lvl_3): # Rage
                state = emotions["rage"].id
        time.sleep(util_refresh)


# Method to print and update emotion animation
def emote(thread_name, emotions):
    while True:
        for key, val in emotions.items():
            if (state == val.id):
                emotions[key].play(frame_time)
