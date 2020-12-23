# shell-emotions
Command line animations based on the state of the system

![](assets/docs/example_eyes.gif)

## Workflow for getting the ascii frames

- Use https://ezgif.com/split to split desired gif animation into frames

- Use https://www.text-image.com/convert/ to create ascii frames based on previously created image frames

- Locate the images and ascii frames in assets directory

## Adding Animations

 - Take ascii frames numbered from 0-n
 - Place ascii frames in filepath `assets/frames/[insert_animation_name]`
 - Create loop from 0-n that concates filepath with `i` and appends frames to frame array
 - Add state value to represent emotion in `state_update(thread_name):`
 - Add conditional run of animation in `emote(thread_name):` using new frame array

## Requirements

 - Python 2 or 3
 - psutil
 - bash/fish shell (Powershell will NOT work as of now)

## clean.sh

Use clean.sh file for cleaning undesired characters from the ascii frames

## main.py

### Functions

```
state_update(thread_name):
```

The state update thread is a daemon that queries system stats through psutil and updates `global state`.

```
emote(thread_name):
```

The emote thread is a daemon that runs the correct animation based on `state` continuously.

```
shutdown(signum, frame):
```

The shutdown function handles clean shutdown of the program with "Shutting down..." printout.

```
main():
```

The main function deals with signal handling and starts both state update and emote threads.