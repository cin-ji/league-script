import pyautogui
import time

# Replace these coordinates with your desired location
desired_x = 3693
desired_y = 539

# Move the mouse to the desired location
pyautogui.moveTo(desired_x, desired_y, duration=1)

# Perform a left click
pyautogui.click()

# Add a delay between the click and the press
time.sleep(0.5)

# Press the 'W' key
pyautogui.press('w')
