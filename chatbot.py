from ast import Raise
from tkinter import *
from tkinter import ttk
from turtle import right, title
from PIL import Image, ImageTk
from numpy import imag

class ChatBot:
    def __init__(self, root):
        self.root = root 
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")

        main_frame = Frame(self.root, bd=4, bg='powder blue',width=610)
        main_frame.pack()

        img_chat = Image.open('chatbot.png')
        img_chat = img_chat.resize((200, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730,compound=LEFT, image=self.photoimg, text='Chat Me',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        # ========= text area ==========

        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20,bd=3, relief=RAISED, font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()






if __name__=="__main__":
    root =Tk()
    obj = ChatBot(root)
    root.mainloop()
