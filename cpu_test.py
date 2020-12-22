import psutil

cpu_percent = psutil.cpu_percent(interval=0.5)
print(cpu_percent)