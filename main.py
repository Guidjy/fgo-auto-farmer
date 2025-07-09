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
        pyautogui.moveTo(1098, 670, 0.1)
        pyautogui.click()
        pyautogui.moveTo(1421, 822, 0.1)
        pyautogui.click()


class Master:
    def use_skill(skill_number):
        pyautogui.moveTo(1776, 468, 0.3)
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
        
    def order_change():
        """
        changes the position of servant1 and servant2
        """
        # dis prolly the worst code ive ever written since connect 4 in assembly
        pyautogui.moveTo(1776, 468, 0.3)
        pyautogui.click()
        pyautogui.moveTo(1644, 469, 0.2)
        pyautogui.click()
        pyautogui.moveTo(969, 511, 0.2)
        pyautogui.click()
        pyautogui.moveTo(1242, 511, 0.2)
        pyautogui.click()
        pyautogui.moveTo(1096, 852, 0.2)
        pyautogui.click()
        pyautogui.click()
        wait_for_image('master_icon')
        time.sleep(2)
        

def find_support_servant(servant):
    if servant == 'koyanskaya':
        wait_for_image_and_click('assassin_icon')
        wait_for_image_and_click('10_10_10_koyan')
        #time.sleep(2)
        #wait_for_image_and_click('quest_start_button')
        
def end_quest():
    quest_end_button = None
    pyautogui.moveTo(1815, 651)
    while quest_end_button == None:
        pyautogui.click()
        quest_end_button = locate_image('quest_end_button')
    pyautogui.moveTo(quest_end_button)
    time.sleep(0.3)
    pyautogui.click()
    
    wait_for_image_and_click('quest_redo_button')
    time.sleep(1)
    
    golden_apple = locate_image('golden_apple')
    if golden_apple:
        pyautogui.moveTo(golden_apple)
        time.sleep(0.3)
        pyautogui.click()
        pyautogui.moveTo(1356, 763, 0.3)
        pyautogui.click()


if __name__ == '__main__':
    time.sleep(5)
    nodes_farmed = 0
    while True:
        
        if pyautogui.position() == (0, 0):
            print(f'nodes_farmed: {nodes_farmed}')
            break
        
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
        
        wait_for_image('master_icon')
        time.sleep(0.5)
        
        # wave 2
        koyan1.use_skill(1, True)
        koyan2.use_skill(7, True)
        
        kukulkan.use_skill(4)
        kukulkan.use_np()
        
        wait_for_image('master_icon')
        time.sleep(3)
        
        # wave 3
        Master.order_change()
        Master.use_skill(1)
        
        oberon.use_skill(7)
        oberon.use_skill(8, True)
        oberon.use_skill(9, True)
        
        kukulkan.use_skill(5, True)
        kukulkan.use_np()
        
        time.sleep(0.5)
        end_quest()
        
        nodes_farmed += 1
    
    