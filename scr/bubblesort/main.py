"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import tkinter as tk

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


class Bubblesort:

    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.configure(bg="light goldenrod yellow")
        self.canvas = tk.Canvas(self.root, bg="light goldenrod yellow")
        self.canvas.pack()
        self.button = tk.Button(self.root, text='Sort', command=self.callback)
        self.button.pack()
        self.root.mainloop()

    def callback(self):
        for i in range(50):
            self.canvas.create_line(5, i * 5, i * 5, 200,
                                    fill="RoyalBlue1", activefill="tomato")


def main():
    b1 = Bubblesort()
    b1.mainloop()


if __name__ == '__main__':
    main()
