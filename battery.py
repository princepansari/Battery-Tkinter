import tkinter as tk
import subprocess
import time

window = tk.Tk()
window.title('Battery')

canvas = tk.Canvas(window, width = 300, height = 300)
canvas.pack()

rect1 = canvas.create_rectangle(000, 00, 300, 300, fill = "black")
rect2 = canvas.create_rectangle(110, 80, 190, 250, fill = "white")
rect3 = canvas.create_rectangle(120, 90, 180, 240, fill = "black")
#rect4 = canvas.create_rectangle(125, 95, 175, 235, fill = "white")
rect5 = canvas.create_rectangle(138, 66, 162,  79, fill = "white")

def updateGUI():
    info = subprocess.Popen("acpi", shell=True, stdout=subprocess.PIPE).communicate()[0]
    info = info.decode('ascii')
    info = list(map(str, info.split()))
    rect4 = canvas.create_rectangle(125, 95, 175, 235, fill = "black")
    if "Dis" in info[2]:
        percentage = info[3].replace("%", "")
        percentage = percentage.replace(",", "")
        percentage = int(percentage)
        desired = 235 - (percentage * 1.4)
        if 0 <= percentage <= 15:
            rect4 = canvas.create_rectangle(125, desired, 175, 235, fill = "red")
        elif 16 <= percentage <= 79:
            rect4 = canvas.create_rectangle(125, desired, 175, 235, fill = "yellow")
        else:
            rect4 = canvas.create_rectangle(125, desired, 175, 235, fill = "green")
    else:
        for i in range(20, 101, 20):
            info1 = subprocess.Popen("acpi", shell=True, stdout=subprocess.PIPE).communicate()[0]
            info1 = info1.decode('ascii')
            info1 = list(map(str, info1.split()))
            if "Dis" in info1[2]:
                break
            desired = 235 - (i*1.4)
            rect4 = canvas.create_rectangle(125, desired , 175, 235, fill = "green")
            window.update()
            time.sleep(1)
    window.after(100, updateGUI)

updateGUI()
window.mainloop()
