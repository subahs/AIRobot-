import tkinter as tk
from tkinter.constants import GROOVE, RIDGE, TOP
from typing import Text, TextIO
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import os
from tkinter import Button, ttk
import time
import face
import audio
class assistant :
    def __init__(self, root):
        
        self.check1 = tk.StringVar()
        self.check2 = tk.StringVar()
        self.textDisplay = tk.StringVar()
        self.textDisplay = ''
        self.root = root
        self.root.title('Nepal College of Information Technology')
        self.root.geometry("1350x700+0+0")
        title = tk.Label(self.root, text="AI Reception Assistant", font=('times new roman', 40, 'bold'), bg = 'blue', fg = 'black', bd = 10, relief= GROOVE)
        title.pack(side =  TOP, fill = 'x')
        mainFrame = tk.Frame(self.root, bd = 4, relief = RIDGE, bg = 'gray')
        mainFrame.place(x=20, y=100, width = 1310, height = 570 )
        self.render = ImageTk.PhotoImage(Image.open('download.jpg'))
        img = tk.Label(mainFrame, image = self.render)
        img.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'w' )
        welcomeText = tk.Label(mainFrame, text = 'Welcome to NCIT', font = ('times new roman', 20, 'bold'), bg = 'gray', fg = 'black')
        welcomeText.grid(row = 1, column = 0, padx = 40, pady = 20, sticky = 'w') 
        self.searchCombo = ttk.Combobox(mainFrame, width = 20, font=('times new roman', 20, 'bold'), state='readonly')
        self.searchCombo['values'] = ('College staff', 'Visitor')
        self.searchCombo.set('Please select one')
        self.searchCombo.grid(row=2 ,column = 0, padx = 10, pady = 20, sticky= 'w')
        self.submitButton = Button(mainFrame, text='SUBMIT', width = 6, command = self.checkChoice).grid(row = 3, column = 0, pady = 5, padx = 90, sticky = 'w')
        displayFrame = tk.Frame(mainFrame,bd = 4, relief = RIDGE, bg = 'gray')
        displayFrame.place(x = 400, y = 30 , width = 800, height = 500)
        displayText = tk.Label(displayFrame, text = self.textDisplay, font = ('times new roman', 20, 'bold'), bg = 'gray', fg = 'black')
        displayText.grid(row = 0, column = 0, sticky = 'w', padx = 50, pady = 20)
        print(self.textDisplay)
        
        

    def checkChoice(self):
            if self.searchCombo.get() == 'College staff' :
                print('Staff')

                face.faceRec()
                

            elif self.searchCombo.get() == 'Visitor' :
                print('Visitor')
                audio.sound()
                
                    
            else :
                print('None')
            self.searchCombo.set('Please select one')
root = tk.Tk()
ob = assistant(root)
root.mainloop()