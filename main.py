import pyautogui
import threading
import keyboard
import math
import time

screenSize = pyautogui.size()


radius = 50  
center_x = screenSize[0] // 2
center_y = screenSize[1] // 2 
angle = 0
running = True  


def moveMouse():
    global angle, running
    while running:
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        pyautogui.moveTo(x, y, duration=0.1)
        
        angle += 0.1 

        time.sleep(0.05)

def stopMovement():
    global running
    running = False


def main():
    move_thread = threading.Thread(target=moveMouse)
    move_thread.start()

    keyboard.on_press(lambda _: stopMovement()) 

    move_thread.join()
    print("Stopped by user.")

if __name__ == "__main__":
    main()
