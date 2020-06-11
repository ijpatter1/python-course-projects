# Your script will also include a function that, when it is called, will invoke
# a dialog modal which will allow users the ability to select a folder directory
# from their system. Finally, your script will show the user’s selected
# directory path in the text field.
# Requirements:
# Your script will need to use Python 3 and the Tkinter module.
# Your script will need to use the askdirectory() method from the Tkinter module.
# Your script will need to have a function linked to the button widget
# so that once the button has been clicked, the user’s selected file path
# will be retained by the askdirectory() method and printed within your GUI’s text widget.

from tkinter import *
import tkinter as tk
from tkinter import filedialog

import GUI_challenge_main
import GUI_challenge_gui


def browse(self):
    filePath = filedialog.askdirectory()
    self.entry1.insert(0,filePath)


if __name__ == "__main__":
    pass
