import pyautogui
import keyboard

def run_script():
    # Replace these coordinates with your desired mouse location
    x = 3693
    y = 539

    # Moves the mouse to the desired location
    pyautogui.moveTo(x, y)

    # Performs a left click
    pyautogui.click()

    # Presses the 'W' key
    keyboard.press('w')
    keyboard.release('w')
