"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import tkinter as tk
from tkinter import Entry
from tkinter import StringVar
import time
import sys
import os

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


class Bubblesort:
    x = 100
    y = 200

    def __init__(self):
        self.root = tk.Tk()

        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.configure(bg="light goldenrod yellow")
        self.root.title("Bubblesort")

        """
        self.v = StringVar()
        self.e = Entry(self.root2, textvariable=self.v)
        self.e.pack()
        self.v.set("a default value")
        self.s = self.v.get()
        """

        self.canvas = tk.Canvas(self.root, bg="light goldenrod yellow", highlightthickness=0)
        self.canvas.config(width=self.x, height=self.y)
        self.canvas.grid(row=1, column=1)
        self.button = tk.Button(self.root, text='Sort', command=self.callback)
        self.button.grid(row=2, column=1)
        self.button_restart = tk.Button(self.root, text='Restart', command=self.restart_program,
                                        bd=0, bg="light goldenrod yellow",  highlightcolor="red")
        self.button_restart.grid(row=2, column=3)

        self.button_exit = tk.Button(self.root, text='Exit', command=self.exit,
                                     bd=0, bg="light goldenrod yellow",  highlightcolor="red")
        self.button_exit.grid(row=2, column=4)

        self.root.mainloop()

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def exit(self):
        sys.exit()

    def callback(self):
        count = 5
        count_2 = 5
        a_list = [5, 192, 21, 2, 1, 93, 4, 7, 1, 22, 8, 3, 12, 1]
        for i in range(len(a_list)):
            self.canvas.create_line(count, self.y, count, self.y - a_list[i],
                                    fill="RoyalBlue1", activefill="tomato")

            self.canvas.update()
            count += 5

        for j in range(len(a_list)):
            print(a_list[j])
            # x0, y0, x1, y1,
            time.sleep(0.1)


def main():
    b1 = Bubblesort()
    b1.mainloop()


if __name__ == '__main__':
    main()
