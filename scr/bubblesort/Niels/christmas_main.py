"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import tkinter as tk
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
        self.root.geometry('+900+50')  # sets the default window position
        self.root.geometry('320x500')
        self.root.title("Bubblesort")

        self.entry_box = tk.Entry(self.root)
        self.entry_box.insert(0, "300, 260, 10, 230, 140, 80, 70, 45, 190, 25")
        self.entry_box.pack()
        self.confirm = tk.Button(self.root, text="Confirm", command=self.confirm_input)
        self.confirm.pack()

        self.lw = tk.Canvas(self.root, bg="grey", width=200, height=400)
        self.lw.pack()

        self.root.mainloop()

    def confirm_input(self):
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
        self.create_tree()
        self.sorting_algorithm()

    def clear_canvas(self):
        self.lw.delete("all")
        self.rectangles = []

    def sorting_algorithm(self):

        sorted_completely = True
        i = 0
        for element in self.entries[:-1]:
            print(self.entries[i])
            print(self.entries[i + 1])
            if self.entries[i] > self.entries[i + 1]:
                print("bigger")
                self.entries[i], self.entries[i + 1] = self.entries[i + 1], self.entries[i]
                print(self.entries)
                sorted_completely = False
            i += 1
            #self.update_rect()
        print(self.entries)
        if sorted_completely is False:
            #self.root.after(500, self.sorting_algorithm)
            None

    def create_tree(self):
        rect_width = 200 / len(self.entries)
        height = 5
        i = 0
        for m in self.entries:
            y = 400 - 5 - m % 10
            rect = self.lw.create_rectangle(i + 3, 400, i + rect_width - 3, y, fill="brown")
            for q in range(m // 10):
                triangle = self.lw.create_polygon(i, y, i + rect_width, y, i + rect_width / 2, y - 10, fill="green")
                y -= 10
            i += rect_width
            self.rectangles.append(rect)

    def update_rect(self):
        i = 0
        rect_number = 0
        for m in self.entries:
            rect_width = 200 / len(self.entries)
            y = 400 - m
            self.lw.coords(self.rectangles[rect_number], i, 400, i + rect_width, y)
            i += rect_width + rect_width / 8
            rect_number += 1


def main():
    b1 = Bubblesort()


if __name__ == '__main__':
    main()
