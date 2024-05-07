import tkinter as tk

import pyautogui as pag

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

def takeScreenshot():
    img = pag.screenshot(region=(0, 450, 600, 300))
    img.save('projects\ScreenshotMaker\screenshot.png')

myButton = tk.Button(text="Take screenshot", command=takeScreenshot(), font=10)
canvas.create_window(100, 100, window=myButton)
a = pag.press('myButton')

root.mainloop()