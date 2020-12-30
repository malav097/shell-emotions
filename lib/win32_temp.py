import clr, time


def init_open_hwd_mon():
    file = 'OpenHardwareMonitorLib'
    try:
        clr.AddReference(file)
        from OpenHardwareMonitor import Hardware
        handle = Hardware.Computer()
        handle.CPUEnabled = True
        handle.Open()
        return handle
    except:
        print("WARNING: %s.lib NOT FOUND (Temps will be disabled)" % file)
        time.sleep(1)
        return None


def get_cpu_pkg_temp(handle):
    cpu_pkg_temp = []
    for dev in handle.Hardware:
        dev.Update()
        for sensor in dev.Sensors:
            if (sensor.Name == "CPU Package"):
                cpu_pkg_temp.append(sensor.Value)
    return min(cpu_pkg_temp)