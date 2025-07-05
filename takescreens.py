# Using venv (Recommended):
# 1. Navigate to your project directory:
# Open your terminal and use the cd command to navigate to the directory where your project files will be located.
# 2. Create the virtual environment:
# Run the command "python3 -m venv .venv". This will create a folder named .venv in your project directory, containing the virtual environment.
# 3. Activate the virtual environment:
# Use the command "source .venv/bin/activate". This will activate the virtual environment, and your terminal prompt will usually change to indicate the active environment. 
# 4. To deactivate the virtual environment:
# Simply type deactivate in the terminal. 

import time
import pyautogui
import datetime
import keyboard


def capture_screenshot():
    # Define the coordinates of the top-left corner and the width and height of the area
    x = 547  # x-coordinate of the top-left corner
    y = 210  # y-coordinate of the top-left corner
    width = 696  # width of the area
    height = 893  # height of the area

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    # filename = f"screenshot_{timestamp}.png"
    filename = f"screenshot_{timestamp}.pdf"
    # screenshot = pyautogui.screenshot()
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.convert('RGB')
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")



if __name__ == "__main__":
    time.sleep(10)

    while True:
        capture_screenshot()
        pyautogui.press('down', presses=20)
        time.sleep(10)
 
        