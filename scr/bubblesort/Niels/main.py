"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import tkinter as tk
from tkinter import messagebox
import time
import sys
import os
import re

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "niels.heissel@stud.uni-frankfurt.de"


class Bubblesort():
    a_list = []
    values = []

    def __init__(self):
        """The Constructor

        Called from the main.py, contructiong the root, which is the basis for the window.
        In the constructor we bind every widget to its belonging root window
        """

        self.rectangles = []

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+950+50')  # sets the default window position
        self.root.geometry('320x525')
        self.root.title("Bubblesort")

        self.pause = False
        self.sorted_completely = True
        self.i = 0
        self.entries = []

        self.entry_box = tk.Entry(self.root)
        self.entry_box.insert(0, "300, 260, 10, 230, 140, 80, 70, 45, 190, 25")
        self.entry_box.pack()
        self.confirm = tk.Button(self.root, text="Confirm", command=self.confirm_input)
        self.confirm.pack()
        self.lw = tk.Canvas(self.root, bg="grey", width=200, height=400)
        self.lw.pack()
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_continue_switch)
        self.pause_button.pack()
        self.help_button = tk.Button(self.root, text="Help", command=self.help)
        self.help_button.pack()

        self.root.mainloop()

    def pause_continue_switch(self):
        if self.pause is True:
            self.pause_button.config(text="Pause")
            self.pause = False
            self.sorting_algorithm()
        else:
            self.pause = True
            self.pause_button.config(text="Continue")

    def help(self):
        """Shows a help-box with useful information."""

        messagebox.showinfo("Bubblsort Help", "Welcome, \nto start the sorting algorithm simply "
                                              "type in a random amount of numbers all separated "
                                              "by a comma. Then click confirm. "
                                              "The program will then sort the "
                                              "numbers and show a visualization on a canvas. "
                                              "\nWrong Input is ignored.")

    def continue_setter(self):
        if self.pause is True:
            self.pause = False
            self.sorting_algorithm()

    def pause_setter(self):
        if self.pause is False:
            self.pause = True

    def confirm_input(self):
        """This procedure validates and parses the input."""
        self.entries = self.entry_box.get()
        self.entries = self.entries.split(",")

        i = 0
        to_delete = []
        for entry in self.entries:
            try:
                self.entries[i] = int(entry)
            except ValueError:
                to_delete.append(entry)
            i += 1
        for entry in to_delete:
            self.entries.remove(entry)

        print(self.entries)
        self.clear_canvas()
        self.create_rect_heigth()
        self.root.after(1000, self.sorting_algorithm)

    def clear_canvas(self):
        self.lw.delete("all")
        self.rectangles = []

    def sorting_algorithm(self):
        """Sorting Algorithm

        Is a while loop (through recursion) which runs until it is not called anymore by loop_slower
        """
        if self.entries != []:
            self.sorted_completely = True
            self.i = 0

            self.update_change()

            print(self.entries)
            print(self.sorted_completely)

            self.root.after(1000, self.loop_slower)

    def loop_slower(self):
        """Slows loop to allow a real comparison for sorted_completely."""
        if self.sorted_completely is False and self.pause is False:
            self.sorting_algorithm()
        else:
            print("done")
            self.update_rect()

    def update_change(self):
        """This procedure really sorts the numbers."""
        print(self.sorted_completely)
        print(self.i)
        if self.entries[self.i] > self.entries[self.i + 1]:
            self.entries[self.i], self.entries[self.i + 1] = self.entries[self.i + 1], self.entries[self.i]
            self.sorted_completely = False
            print("bigger")
        self.update_rect()
        if self.i < len(self.entries) - 2:
            self.i += 1
            self.root.after(100, self.update_change)

    def create_rect_heigth(self):
        """Initial rectangle constructor. Dynamic Width and Height."""
        i = 1
        rect_width = 200 / len(self.entries) - 3

        for m in self.entries:
            y = 400 - m
            rect = self.lw.create_rectangle(i, 400, i + rect_width, y, fill="red")
            i += rect_width + 3
            self.rectangles.append(rect)

    def update_rect(self):
        """Updated the position of the rectangles."""
        i = 0
        rect_number = 0
        rect_width = 200 / len(self.entries) - 3
        for m in self.entries:
            y = 400 - m
            self.lw.coords(self.rectangles[rect_number], i, 400, i + rect_width, y)
            i += rect_width + 3
            rect_number += 1


def main():
    b1 = Bubblesort()


if __name__ == '__main__':
    main()
