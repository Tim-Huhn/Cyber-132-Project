########################################
# name: 
# date: 
# description: 
########################################
from Tkinter import *

# the main GUI
class Chessboard(Frame, Canvas):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="grey")
        parent.attributes("-fullscreen", True)
        self.setupGUI()

    # sets up the GUI
    def setupGUI(self):
        for i in [1, 2, 3, 4, 5, 6, 7, 8]:
            for j in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                self.Tiles(i, j)
        # pack the GUI
        self.pack(fill=BOTH, expand=1)

    def Tiles(self, i, j):
        """ tiles need to be implemented """
         
##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("Chess")
# generate the GUI
p = Chessboard(window)
# display the GUI and wait for user interaction
window.mainloop()
