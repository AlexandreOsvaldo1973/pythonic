from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Uma janelinha para o Python")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.mudarTexto
        self.sair.pack ()

    def mudarTexto(self):
        if self.msg["text"] == "Uma janelinha para o Python":
            self.msg["text"] = "Python é fodão!"
        else:
            self.msg["text"] = "Uma janelinha para o Python"

root = Tk()
Application(root)
root.mainloop()
