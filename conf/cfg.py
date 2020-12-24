frames_path = "./assets/frames/" # File path for frames folder
emotions = {} # DO NOT MODIFY: This is the global emotion dict
state = 0 # Default starting state
frame_time = 0.2 # Time (sec) between frames
util_refresh = 5 # Time (sec) before updating utilization stats
cpu_lvl_1 = 10 # Boundary for low CPU usage
cpu_lvl_2 = 30 # Boundary for medium CPU usage
cpu_lvl_3 = 90 # Boundary for high CPU usage