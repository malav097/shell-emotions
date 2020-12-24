# shell-emotions
Command line animations based on the state of the system for Linux or Windows 10

![](assets/docs/eyes_example.gif)

**NOTE: If you are using Powershell on Windows 10 you MUST use `Ctrl-BREAK` to terminate the application**

**The ascii animations were created using a modified version of [Joedang's converter](https://github.com/Joedang/termimation)**

## Workflow for getting the ascii frames

- Use https://ezgif.com/split to split desired gif animation into frames

- Use https://www.text-image.com/convert/ to create ascii frames based on previously created image frames

- Locate the images and ascii frames in assets directory

## Adding Animations

 - Create ascii frames using above workflow or modified Termimium from https://github.com/avanishsubbiah/termimation-save-frames
 - Move ascii frames named 0-N to `./assets/frames/<insert_emotion_name>`
 - Add conditional in `state_update()` in lib.threading that sets `state = emotions["<insert_emotion_name>"].id`

## Requirements

 - Python 2 or 3
 - psutil
 - Bash, Fish, or Powershell

## Configuration

Configurable Parameters in ./conf/cfg.py:

 - `frames_path` | This is the path of the frames folder where individual folders for each emotion is kept (Default "./assets/frames/")
 - `state` | This is the starting state of the program (Default 0)
 - `frame_time` | The time before printing next frame (Default 0.2)
 - `util_refresh` | Time inbetween utilization stat refreshes (Default 5)
 - `cpu_lvl_1` | Boundary for low CPU usage (Default 10)
 - `cpu_lvl_2` | Boundary for medium CPU usage (Default 30)
 - `cpu_lvl_3` | Boundary for high CPU usage (Default 90)

## clean.sh

Use clean.sh file for cleaning undesired characters from the ascii frames

## main.py

### Functions

```
shutdown(signum, frame):
```

The shutdown function handles clean shutdown of the program with "Shutting down..." printout.

```
main():
```

The main function deals with signal handling and starts both state update and emote threads.

## threading.py

### Functions

```
state_update(thread_name):
```

The state update thread is a daemon that queries system stats through psutil and updates `global state`.

```
emote(thread_name):
```

The emote thread is a daemon that runs the correct animation based on `state` continuously.

## animation.py

### Classes

```
class Animation:
```

The `Animation` class has the properties `name`, `id`, `file_path`, and `frames`. 
It will fill `frames` list upon initialization using input `file_path` and `name`.