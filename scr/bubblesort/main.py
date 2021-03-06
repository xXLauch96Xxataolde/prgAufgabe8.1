"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import tkinter as tk
import tkinter.messagebox as mb
import time
import sys
import os
import re

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


class Bubblesort:
    x = 100
    y = 220
    a_list = []
    values = []
    wait = 0.1
    pause = False
    state = 0

    def __init__(self):
        self.user_question()

        self.root = tk.Tk()

        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.configure(bg="light goldenrod yellow")
        self.root.title("Bubblesort")

        self.canvas = tk.Canvas(self.root, bg="light goldenrod yellow", highlightthickness=0)
        self.canvas.config(width=self.x, height=self.y)
        self.canvas.grid(row=1, column=2)
        self.button_sort = tk.Button(self.root, text='Sort', command=self.callback)
        self.button_sort.grid(row=2, column=1)
        self.button_restart = tk.Button(self.root, text='Restart', command=self.restart_program,
                                        bd=0, bg="light goldenrod yellow", highlightcolor="red")
        self.button_restart.grid(row=2, column=2)

        self.button_exit = tk.Button(self.root, text='Exit', command=self.exit,
                                     bd=0, bg="light goldenrod yellow", highlightcolor="red")
        self.button_exit.grid(row=2, column=3)
        
        self.button_exit = tk.Button(self.root, text='Pause', command=self.pause_button,
                                     bd=0, bg="light goldenrod yellow", highlightcolor="red")
        self.button_exit.grid(row=2, column=4)
        
        for element in range(0, len(self.a_list)):
            self.canvas.create_line(element * 5, self.y, element * 5, self.y - self.a_list[element],
                                    fill="Black", activefill="tomato", width=2)

            self.canvas.update()

        self.root.mainloop()

    def x_axis_check(self):
        temp = self.a_list[0]
        for i in self.a_list:
            if (temp < int(i)):
                temp = int(i)

        return(temp)

    def value_validator(self):
        entry_string = self.entry_1.get()
        list_a = entry_string.split(",")
        for entry in list_a:
            while(True):
                try:
                    self.a_list.append(int(entry))
                    break
                except ValueError:
                    break


        if (len(self.a_list) == 0):
            mb.showerror("Empty or non valid entries", "No sorting for you, fam", icon=mb.ERROR)
            sys.exit()
        elif(len(self.a_list) > 20):
            self.x = (150 / 30) * len(self.a_list)
            self.wait = 0.02
        
        x_axis_max = self.x_axis_check()
        if (x_axis_max >= self.y and x_axis_max <= 800):
            self.y = x_axis_max
        elif(x_axis_max > 800):
            mb.showwarning(
                "Entries too big", "Some of the entries wont fit inside the y axis", icon=mb.WARNING)
        self.user_entry.destroy()

    def user_question(self):
        self.user_entry = tk.Tk()
        self.user_entry.attributes("-topmost", True)  # put the root to foreground
        self.user_entry.configure(bg="light goldenrod yellow")
        self.user_entry.title("Bubblesort")

        self.label_1 = tk.Label(
            self.user_entry, text="Pleaser enter comma separated integer values to sort:", bg="light goldenrod yellow")
        self.label_1.grid(row=0)

        self.entry_1 = tk.Entry(self.user_entry)
        self.entry_1.grid(row=1)
        self.button_1 = tk.Button(self.user_entry, text="Sort", command=self.value_validator)
        self.button_1.grid(row=2)

        self.user_entry.mainloop()

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def exit(self):
        sys.exit()

    def clear(self, element):
        self.canvas.create_line((element * 5), self.y, (element * 5), 0,
                                fill="light goldenrod yellow", activefill="green", width=2)
        self.canvas.update()
        self.canvas.create_line(((element + 1) * 5), self.y, ((element + 1) * 5), 0,
                                fill="light goldenrod yellow", activefill="green", width=2)
        self.canvas.update()

    def fill_two_bars(self, element):
        time.sleep(self.wait)
        y0 = self.y - self.a_list[element]
        self.canvas.create_line(element * 5, y0, element * 5, self.y,
                                fill="red", activefill="green", width=2)
        self.canvas.update()
        y0 = self.y - self.a_list[element + 1]
        self.canvas.create_line((element + 1) * 5, y0, (element + 1) * 5, self.y,
                                fill="red", activefill="green", width=2)
        self.canvas.update()

    def mark_two_bars(self, element):
        time.sleep(self.wait)
        y0 = self.y - self.a_list[element]
        self.canvas.create_line(element * 5, y0, element * 5, self.y,
                                fill="green", activefill="green", width=2)
        self.canvas.update()
        y0 = self.y - self.a_list[element + 1]
        self.canvas.create_line((element + 1) * 5, y0, (element + 1) * 5, self.y,
                                fill="green", activefill="green", width=2)
        self.canvas.update()
        self.fill_two_bars(element)
    
    def pause_button(self):
        if (self.state ==0):
            self.pause = True
            self.state = 1
            print("pause")
        elif(self.state == 1):
            self.pause = False
            self.state =0
            
    
    def callback(self):
        list_sorted = False
        while not list_sorted:
            list_sorted = True
            for element in range(0, len(self.a_list) - 1):
                self.mark_two_bars(element)
                if self.a_list[element] > self.a_list[element + 1]:
                    list_sorted = False
                    self.a_list[element], self.a_list[element +
                                                      1] = self.a_list[element + 1], self.a_list[element]
                    self.clear(element)
                    self.fill_two_bars(element)
            if self.pause:
                time.sleep(0.5)
        # print(self.a_list)


def main():
    b1 = Bubblesort()
    b1.mainloop()


if __name__ == '__main__':
    main()
