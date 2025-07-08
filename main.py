import pyautogui
import time
import os

# Give the user a moment to prepare
print("Looking for image in 3 seconds...")
time.sleep(3)

# Path to the image
image_path = os.path.join("media", "test.png")

# Locate the image on screen
location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)  # Adjust confidence if needed

if location:
    print(f"Image found at {location}, moving and clicking...")
    pyautogui.moveTo(location, duration=0.5)
    pyautogui.click()
else:
    print("Image not found on screen.")
