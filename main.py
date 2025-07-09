import pyautogui
import time
from utils import *


SKILL_INTERVAL = 2


class Servant:
    def __init__(self, name, is_kukulkan=False):
        self.name = name
        self.is_kukulkan = is_kukulkan
    
    def use_skill(self, skill_number, targetable=False, target=2):
        match skill_number:
            case 1:
                pyautogui.moveTo(411, 795, 0.1)
            case 2:
                pyautogui.moveTo(520, 795, 0.1)
            case 3:
                pyautogui.moveTo(632, 795, 0.1)
            case 4:
                pyautogui.moveTo(806, 795, 0.1)
            case 5:
                pyautogui.moveTo(907, 795, 0.1)
            case 6:
                pyautogui.moveTo(1011, 795, 0.1)
            case 7:
                pyautogui.moveTo(1182, 795, 0.1)
            case 8:
                pyautogui.moveTo(1292, 795, 0.1)
            case 9:
                pyautogui.moveTo(1395, 795, 0.1)
                
        pyautogui.click()
        
        if self.is_kukulkan:
            pyautogui.moveTo(1530, 599, 0.1)
            pyautogui.click()
                
        if targetable:
            match target:
                case 1:
                    pyautogui.moveTo(731, 560, 0.1)
                case 2:
                    pyautogui.moveTo(1105, 560, 0.1)
                case 3:
                    pyautogui.moveTo(1477, 560, 0.1)
        pyautogui.click()
                    
        pyautogui.click()
        wait_for_image('master_icon')
        time.sleep(0.3)
    
    
    def use_np(self):
        pyautogui.moveTo(1711, 822, 0.1)
        pyautogui.click()
        pyautogui.moveTo(1098, 345, 0.5)
        pyautogui.click()
        pyautogui.moveTo(1098, 670, 0.3)
        pyautogui.click()
        pyautogui.moveTo(1421, 822, 0.3)
        pyautogui.click()
        
        wait_for_image('master_icon')
        time.sleep(0.5)


class Master:
    def use_skill(skill_number):
        pyautogui.moveTo(1711, 822, 0.3)
        pyautogui.click()
        match skill_number:
            case 1:
                pyautogui.moveTo(1432, 465, 0.1)
            case 2:
                pyautogui.moveTo(1540, 468, 0.1)
            case 3:
                pyautogui.moveTo(1644, 469, 0.1)
        pyautogui.click()
        pyautogui.click()
        wait_for_image('master_icon')
        time.sleep(0.5)
        
    def order_change(servant1, servant2):
        """
        changes the position of servant1 and servant2
        """
        print('order change')
        

def find_support_servant(servant):
    if servant == 'koyanskaya':
        wait_for_image_and_click('assassin_icon')
        wait_for_image_and_click('10_10_10_koyan')
        time.sleep(2)
        wait_for_image_and_click('quest_start_button')


if __name__ == '__main__':
    find_support_servant('koyanskaya')
    wait_for_image('master_icon')
    pyautogui.click()
    time.sleep(3)
    
    koyan1 = Servant('Koyanskaya')
    kukulkan = Servant('Kukulkan', is_kukulkan=True)
    koyan2 = Servant('Koyanskaya')
    oberon = Servant('Oberon')
    
    # wave 1
    koyan1.use_skill(2, True)
    koyan1.use_skill(3, True)
    
    koyan2.use_skill(8, True)
    koyan2.use_skill(9, True)
    
    kukulkan.use_skill(4)
    kukulkan.use_skill(5, True)
    kukulkan.use_skill(6)
    kukulkan.use_np()
    
    # wave 2
    koyan1.use_skill(1, True)
    koyan2.use_skill(7, True)
    
    kukulkan.use_skill(4)
    kukulkan.use_np()
    
    # wave 3
    
    