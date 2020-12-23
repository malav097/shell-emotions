import time
import sys
from lib import emotions
from lib import statemanager



class animation:
    
    def run(self):
        def animate(emotion):
            for frame in emotion:
                print('\033c')
                print("".join(frame))
                time.sleep(0.2)
        emotion = emotions.emotions()
        
        while True:
            if (statemanager.state == 0): # Sleepy Animation
                animate(emotion.sleepy)

            elif (statemanager.state == 1): # Waking Up
                animate(emotion.frames)

            elif (statemanager.state == 2): # Awake
                animate(emotion.awake)

            elif (statemanager.state == 3): # Rage

                animate(emotion.rage)
