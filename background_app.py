import keyboard
import time
from mouse import run_script

is_running = False

def toggle_script():
    global is_running
    is_running = not is_running
    if is_running:
        run_script()

if __name__ == "__main__":
    # create macro key
    keyboard.add_hotkey('ctrl+alt+shift+f12', toggle_script)

    print("Press macro key to start/stop script.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
