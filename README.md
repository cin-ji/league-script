# league-script

## Description

This is a script that will move Yuumi to a desired x, y coordinates of your mouse and press W for Yuumi to attach to ally.
This is a script that runs in the background and start/stop the application using a macro key (of your choice).

## Setup
To set up and use LoLScript: find your coordinates, set your desired coordinates, create a macro, create a shortcut, then run the shortcut.

## Create and set mouse coordinates
1. Run mouse.py
2. Move your mouse to an ally pic (above minimap)
3. Write those coordinates 
4. Modify get_coordinates.py (x and y)

## Create macro
1. Create a macro key
2. Remap key. For exmaple: ctrl+alt+shift+f12

## Create shortcut
1. Right-click on an empty space on your desktop or in a folder in File Explorer, and click on `New` -> `Shortcut`
2. In the "Create Shortcut" window:
- Replace `C:\Python311\pythonw.exe` for example: C:\Python311\pythonw.exe "C:\Users\myPC\Desktop\League Script\background_app.py"
3. Click "Next" and give your shortcut a name, such as "LoLScript"
4. Click "Finish" to create the shortcut
5. Double click shortcut to run script
6. Press macro to start/stop the app





