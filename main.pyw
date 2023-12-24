from tkinter import *
from tkinter.ttk import Progressbar

import pharama


root = Tk()

# Set the size and position of the window in the center of the screen
height = 430
width = 530
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Remove the window border and set the background color
root.overrideredirect(True)
root.config(background='#1B3D81')

# Create a heading label and add an image
heading = Label(root, text='Pharma store', bg='#1B3D81', font=('Comic Sans MS', 25, 'bold'))
heading.place(x=160, y=3)

bg = PhotoImage(file='images\\pharma.png')
bg_image = Label(root, image=bg, bg='#1B3D81', activebackground='#1B3D81')
bg_image.place(x=100, y=70)

# Add a progress bar and a label
progress_label = Label(root, text='Please wait...', bg='#1B3D81', font=('Comic Sans MS', 15, 'bold'))
progress_label.place(x=15, y=350)

progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)

# Define the load function to update the progress bar

i = 0


def load():
    global i

    if i <= 10:
        txt = 'Please wait... ' + (str(10 * i) + '%')
        progress_label.config(text=txt)
        progress_label.after(100, load)
        progress['value'] = 10 * i
        i += 1


# Call the load function to start the progress bar
load()


def new_window():
    pharama.Restore(root)
    root.withdraw()


root.after(2500, new_window)

# Start the GUI event loop
root.mainloop()
