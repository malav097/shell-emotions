import os , time
files   = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
frames  = []
k = 1
frames_path = "./assets/frames/"
working_dir = os.path.dirname(__file__)

for name in files:
    filepath = frames_path + name
    print(filepath)
    rel_path = os.path.relpath(filepath, working_dir)
    with open(rel_path, "r", encoding="utf8") as f:
        #sabe every line in list "f"
        f = f.readlines()
        #append list f to list frames
        frames.append(f)

while k == 1:

    for frame in frames:
        #clear the shell
        os.system('printf "\033c"') #printf "\033c"') 
        print("".join(frame))
        #print(" TEST ")
        time.sleep(0.2)
        #clear the shell
        
   
