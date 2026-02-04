from mss import mss
from datetime import datetime
import cv2
import numpy as np
import time
import os

SAVE_DIR = "meet_slides"
INTERVAL = 3
THRESHOLD = 50000

os.makedirs(SAVE_DIR, exist_ok=True)

prev_gray = None
count = 0

current_date = None
day_dir = None

with mss() as sct:
    monitor = sct.monitors[1]

    while True:
        img = np.array(sct.grab(monitor))  # BGRA
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            diff = cv2.absdiff(prev_gray, gray)
            non_zero = np.count_nonzero(diff)

            if non_zero > THRESHOLD:
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")

                if date_str != current_date:
                    current_date = date_str
                    day_dir = os.path.join(SAVE_DIR, current_date)
                    os.makedirs(day_dir, exist_ok=True)

                filename = os.path.join(day_dir, f"{now.strftime('%H-%M-%S-%f')}.png")
                cv2.imwrite(filename, frame)
                print(f"Slide changed → saved {filename}")
                count += 1

        prev_gray = gray
        time.sleep(INTERVAL)