import pyautogui
import time

def print_mouse_coordinates():
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {x} Y: {y}'
        print(position_str, end='\r')
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        print("Press Ctrl-C to stop.")
        print_mouse_coordinates()
    except KeyboardInterrupt:
        print("\nStopped.")
