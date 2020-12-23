import os , time
import psutil
from threading import Thread
import signal
import sys


class emotions:

    def __init__(self):
        # Importing frames and Initializing file paths and global state
        self.files   = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        self.frames  = []
        self.sleepy = []
        self.awake = []
        self.rage = []
        self.sleepy_ind = [0, 7]
        self.awake_ind = [0, 1, 4, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 5, 6, 7]
        self.frames_path = "./assets/frames/"
        self.working_dir = os.path.dirname(__file__)
        print(self.working_dir)

        for name in self.files:
            filepath = self.frames_path + name
            print(filepath)
            rel_path = filepath# os.path.relpath(filepath, working_dir)
            with open(rel_path, "r", encoding="utf8") as f:
                #sabe every line in list "f"
                f = f.readlines()
                #append list f to list frames
                self.frames.append(f)

        for i in range(18):
            filepath = self.frames_path + "rage/" + str(i)
            print(filepath)
            rel_path = filepath#os.path.relpath(filepath, working_dir)
            with open(rel_path, "r", encoding="utf8") as f:
                #sabe every line in list "f"
                f = f.readlines()
                #append list f to list frames
                self.rage.append(f)

        for ind in self.awake_ind: # Setting up Awake frames
            self.awake.append(self.frames[ind])

        for i in range(5): # Setting up Asleep frames
            for ind in self.sleepy_ind:
                self.sleepy.append(self.frames[ind])

