from tkinter import *
import random
import time
import threading


game_state = 'stopped'
arrows = {('Up','\u2191','Down'), ('Down','\u2193','Up'), ('Right','\u2192','Left'), ('Left','\u2190','Right')}
pressed_arrow = None


def start():
    global game_state, pressed_arrow
    if game_state == 'stopped':
        game_state = 'started'
        score = 0
        current_arrow = ()
        score_label.config(text="your score\n 0")
        instruction_label.config(text="")
        for i in range(3,0,-1):
            arrow_label.config(text=str(i))
            time.sleep(1)
        while game_state == 'started':
            current_arrow = random.choice(tuple(arrows-{current_arrow}))
            arrow_label.config(text=current_arrow[1])
            root.update()
            time.sleep(0.5)
            if pressed_arrow == current_arrow[2]:
                score += 1
                score_label.config(text=f"your score\n {score}")
                root.update()
                pressed_arrow = None
            else:
                arrow_label.config(text="GAME OVER")
                game_state = 'stopped'
                root.update()
                instruction_label.config(text='press spacebar to start')


def arrow_pressed(key):
    global pressed_arrow
    if game_state == 'started' and pressed_arrow is None:
        pressed_arrow = key.keysym


root = Tk()

root.title("Press the opposite")
root_w = 500
root_h = 300
root_x = int(root.winfo_screenwidth()/2-root_w/2)
root_y = int(root.winfo_screenheight()/2-root_h/2)
root.geometry(f"{root_w}x{root_h}+{root_x}+{root_y}")

Label(root,text="press the opposite key in 0.5 second", font=("Arial",10),pady=12).pack()

arrow_label = Label(root,text="",font=("Arial", 32), pady=20)
arrow_label.pack()

score_label = Label(root,text="your score\n 0",font=("Arial", 20))
score_label.pack()

instruction_label = Label(root, text="press spacebar to start", pady=50)
instruction_label.pack()

root.bind("<space>", lambda e: threading.Thread(target=start).start())

root.bind("<Up>",arrow_pressed)
root.bind("<Down>",arrow_pressed)
root.bind("<Left>",arrow_pressed)
root.bind("<Right>",arrow_pressed)

root.mainloop()