import pyautogui
import time
import os


class Servant:
    def __init__(self, name, position, is_kukulkan=False):
        self.name = name
        self.position = position
        self.is_kukulkan = is_kukulkan
    
    def use_skill(skill_number, targetable=False, target=1):
        print('servant skill!')


class Master:
    def use_skill(skill_number):
        print('master skill!')
        
    def order_change(servant1, servant2):
        """
        changes the position of servant1 and servant2
        """
        print('order change')
        

def find_support_servant(servant):
    if servant == 'koyansakaya':
        print('0-0')
        


if __name__ == '__main__':
    #time.sleep(2)
    for i in range(1):
        time.sleep(3)
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})")