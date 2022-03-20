"""Copy from vim to Codecademy"""
"""This script assumes:
    - Alt+Tab moves from Vim to Codecademy.
    - When Codecademy is the focus, it is fullscreen.
    - The code field is in the middle of the screen.
You can change these by modifying the script."""

import pyautogui as pag
import time

# Codecademy code field location, which is assumed to be mid-screen
halfx, halfy = (x/2 for x in pag.size())

def main():
    pag.hotkey('alt', 'tab') # Switch to Codecademy
    time.sleep(0.25)
    pag.click(halfx, halfy) # Click the Codecademy code field
    pag.hotkey('ctrl', 'a')
    pag.hotkey('ctrl', 'v')
    pag.hotkey('ctrl', 'enter')

main()
