from __future__ import print_function
from io import open
import os, time


# Class for animation objects
class Animation:
    def __init__(self, name, id, file_path):
        self.name = name
        self.id = id
        self.file_path = file_path + name + "/"
        self.frames = []

        for i in range(len(os.listdir(self.file_path))):
            iter_path = self.file_path + str(i)
            #print(iter_path)
            with open(iter_path, "r", encoding="utf8") as f:
                #sabe every line in list "f"
                f = f.readlines()
                #append list f to list frames
                self.frames.append(f)

    def play(self, frame_time):
        for frame in self.frames:
            print('\033c', end="")
            print("".join(frame))
            time.sleep(frame_time)
