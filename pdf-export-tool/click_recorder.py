"""
Captures left mouse clicks and saves the screen coordinates of the cursor position on click, and the 
delay in seconds between each click.

On exiting the program via CTRL + C the captured clicks are output to a python file clicks.py in the local
folder. This file can then be used as a starting point for more advanced RPA processes.
"""

import pyautogui, sys, os, time
import win32con, win32api

def is_mouse_down():
    """
    If left mouse button is clicked add coordinates
    to saved clicks set
    """
    key_code = win32con.VK_LBUTTON
    state = win32api.GetAsyncKeyState(key_code)
    return state != 0


def print_mouse_click_coordinates():
    """
    Prints screen coordinates of a click
    """
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)


def save_mouse_click_coordinates(clicks):
    """
    Captures XY coordinates of click and returns a string
    """
    x, y = pyautogui.position()
    return f"pyautogui.moveTo({x}, {y})#{clicks}"


def transform_set(s):
    """
    Transforms coordinate strings set into a dictionary split on '#'
    and returns a dictionary of key (count number) value (click coordinates)
    pairs. 
    """
    dictionary = {}
    for i in s:
        key = int(i.split('#')[1])
        value = i.split('#')[0]
        dictionary[key] = value

    return dictionary


def output_to_file(clicks_dict, delays):
    """
    Outputs count, click coordinates and time delays between each click
    to a python file named clicks.py in the local directory.
    """
    f = open("clicks.py", "w")
    f.write("import pyautogui, os, time\n\n")

    for i in range(len(clicks_dict)):
        f.write(f"# Click {i + 1}\n")
        f.write(f"{clicks_dict[i]}\n")
        f.write("pyautogui.click()\n")
        f.write(f"time.sleep({delays[i]})\n\n")

    f.close()
    

def main():
    print('Left mouse clicks will record screen coordinates...')
    print(f"Screen size is --> {pyautogui.size()}")
    print('Press Ctrl-C to save clicks to file and quit.')
    coordinates_set = set()
    delays = []
    click = 0
    timer = time.time()

    try:
        while True:
            check = is_mouse_down()

            if check == True:
                print_mouse_click_coordinates()
                coordinates = save_mouse_click_coordinates(click)
                coordinates_set.add(coordinates)
                delays.append(int(round(time.time() - timer, 0)))

                timer = time.time() # reset timer
                click += 1 # increment count
                time.sleep(1) 


    except KeyboardInterrupt:
        results = transform_set(coordinates_set)
        output_to_file(results, delays)
        print("File clicks.py saved in local folder.")
        print('\n')

if __name__ == "__main__":
    main()