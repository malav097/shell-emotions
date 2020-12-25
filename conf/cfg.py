frames_path = "./assets/frames/" # File path for frames folder
state = 0 # Default starting state
welcome_time = 1 # Time (sec) for welcome message
frame_time = 0.2 # Time (sec) between frames
util_refresh = 5 # Time (sec) before updating utilization stats
cpu_usage_time = 1 # Time (sec) to average CPU usage over
cpu_lvl_1 = 10 # Boundary for low CPU usage
cpu_lvl_2 = 30 # Boundary for medium CPU usage
cpu_lvl_3 = 90 # Boundary for high CPU usage
cpu_temp_bound = 10 # Boundary for high CPU temperature
cpu_temp_sensor = 'coretemp' # Sensor to pull CPU Temps from
mem_bound = 50 # Boundary for high memory usage