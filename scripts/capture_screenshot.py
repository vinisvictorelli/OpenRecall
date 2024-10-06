import threading
import time
import cv2
import numpy as np
import pyscreenshot as ImageGrab
from Xlib import display

import os
import datetime

# Take screenshot
def take_screenshot():
    # Take a screenshot of the main monitor
    screenshot = ImageGrab.grab()  # bbox=(x1, y1, x2, y2)
    # Convert screenshot to a NumPy array (compatible with OpenCV)
    screenshot_np = np.array(screenshot)

    # Convert RGB to BGR format (OpenCV uses BGR format)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    return screenshot_np
def save_screenshot(screenshot):
    # Create a timestamped filename
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
    filepath = f"capture/{filename}"
    #Save image
    cv2.imwrite(filepath, screenshot)
    print(f"Screenshot saved: {filename}")

def compare_screenshots(prev_screenshot, curr_screenshot):
    # Convert to grayscale for comparison
    prev_gray = cv2.cvtColor(prev_screenshot, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_screenshot, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between screenshots
    diff = cv2.absdiff(prev_gray, curr_gray)
    diff_percentage = (np.sum(diff > 50)/diff.size) * 100
    return diff_percentage

# Main function
def main_screenshot_function():
    prev_screenshot = take_screenshot()
    save_screenshot(prev_screenshot)
    print(f'Screenshot saved')
    while True:
        time.sleep(3)
        curr_screenshot = take_screenshot()
        diff = compare_screenshots(prev_screenshot,curr_screenshot)
        print(f'Difference percentage: {diff}%')
        if diff > 5:
            save_screenshot(curr_screenshot)
            print(f'Screenshot saved')
            #Update de current screenshot
            prev_screenshot = curr_screenshot


