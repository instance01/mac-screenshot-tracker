# Simple Mac Screenshot Tracker

<p float="left">
  <img src=".github/screen1.png" width="49%" />
  <img src=".github/screen2.png" width="49%" /> 
</p>

Become more productive by reviewing what you've been working on. This application runs in the background and creates low-resolution screenshots every 60 or so (can be changed) seconds. After a tough day full of work you can then watch what you've been doing. Maybe you find that you waste a surprisingly huge amount of time on random things.

Why did I create this? It's a completely free alternative to the many screenshot trackers out there. It is very simple and hackable. It gets the job done!

Dependencies:
* ffmpeg (e.g. `brew install ffmpeg`)

Usage:
```
python3 track.py track
python3 track.py watch
```

For scrolling through all captured screenshots I use: https://github.com/torum/Image-viewer

TODO:
* Support for Linux, Windows. Should be trivial with ffmpeg, simply change the -f parameter (https://trac.ffmpeg.org/wiki/Capture/Desktop). Pull requests are welcome.
* More options, flesh it out. This is more for hackers who want to tinker with it.
* Statistics based on the [application in the foreground](https://stackoverflow.com/questions/373020/finding-the-current-active-window-in-mac-os-x-using-python). However, this will require PyObjC, a substantial dependency.
