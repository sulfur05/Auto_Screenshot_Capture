import pyautogui
import time
import os

INTERVAL = 2
SAVE_DIR = "lecture_ss"

os.makedirs(SAVE_DIR, exist_ok=True)

count = 0 
while True:
    ss = pyautogui.screenshot()
    filename = f"{SAVE_DIR}/slide_{count}.png"
    ss.save(filename)
    print(f"Saved {filename}")
    count += 1
    time.sleep(INTERVAL)