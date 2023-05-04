import pyautogui
import keyboard
import time
import threading

stop_flag = False
# get x and y coordinates
def print_mouse_coordinates():
    global stop_flag
    while not stop_flag:
        x, y = pyautogui.position()
        position_str = f'X: {x} Y: {y}'
        print(position_str, end='\r')
        time.sleep(0.1)

# stop the script
def stop_script():
    global stop_flag
    stop_flag = True

if __name__ == '__main__':
    try:
        print("Press the Space key to stop.")
        keyboard.add_hotkey('space', stop_script)
        print_mouse_coordinates()
    except KeyboardInterrupt:
        print("\nStopped.")
