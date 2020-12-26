import tkinter
import random
from playsound import playsound

root = tkinter.Tk()
root.geometry('400x300')
root.title('RIs Dice')

label = tkinter.Label(root, text='', font=('Helvetica', 200))


def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    playsound("Shake And Roll Dice.mp3")
    label.configure(text=f'{random.choice(dice)}', bg="light green",foreground="red")
    label.pack()


button = tkinter.Button(root, text='Click To Roll Dice', bg='green', command=roll_dice,foreground="white",activebackground='light blue').pack()
root.configure(bg="light green")
root.mainloop()
