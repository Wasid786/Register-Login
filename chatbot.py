from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root 
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")



if __name__=="__main__":
    root =Tk()
    obj = ChatBot(root)
    root.mainloop()
