import pyautogui
import time
import os


CONFIDENCE = 0.8
INTERVAL = 1


def locate_image(image):
    """
    Finds an image based on its file name and returns its position.
    args:
    - image: file name without extension
    """
    image_path = os.path.join('media', image + '.png')
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=CONFIDENCE)
    except pyautogui.ImageNotFoundException as e:
        location = None
    
    return location


def wait_for_image(image):
    """
    Keeps searching for the image until it is found on the screen.
    Returns the position as soon as it appears.
    args:
    - image: file name without extension
    """
    location = None
    while location == None:
        location = locate_image(image)
    
    return location


def wait_for_image_and_click(image):
    """
    Keeps searching for the image until it is found on the screen.
    double clicks it as soon as it appears.
    args:
    - image: file name without extension
    """
    location = None
    while location == None:
        location = locate_image(image)
    
    pyautogui.doubleClick(location)
    