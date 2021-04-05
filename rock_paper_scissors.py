from tkinter import Menu, Button, StringVar, OptionMenu, messagebox as msg, filedialog, Tk, Label
from tkinter import simpledialog

class RockPaperScissors():
    def __init__(self, master):
        self.master = master
        self.master.title("ROCK PAPER SCISSORS")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        self.score = [0,0]
        self.numberofrounds = 0


        category_list = list(["Rock", "Paper", "Scissors"])
        self.var_cat_list = StringVar(master)
        self.var_cat_list.set(category_list[0])
        self.popupcatlistmenu = OptionMenu(self.master, self.var_cat_list, *category_list)
        self.popupcatlistmenu.pack()

        self.playb = Button(self.master, text="Play", command=self.play)
        self.playb.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff = 0)
        self.file_menu.add_command(label="New Game", accelerator='Ctrl+O', command=self.newgame)
        self.file_menu.add_command(label="Load Game")
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command = self.exitmenu)
        self.menu.add_cascade(label = "File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff = 0)
        self.about_menu.add_command(label = "About", accelerator= 'Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff = 0)
        self.help_menu.add_command(label = "Help", accelerator = 'Ctrl+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())

    
    def play(self):
        pass

    def newgame(self):
        self.numberofrounds = simpledialog.askinteger("Number of rounds",
                                                          "Enter the number of rounds",
                                                          parent=self.master,
                                                          minvalue=1)
        while self.numberofrounds == 0:
            self.numberofrounds = simpledialog.askinteger("Number of rounds",
                                                          "Enter the number of rounds",
                                                          parent=self.master,
                                                          minvalue=1)
        
        self.roundslabel = Label(self.master, text="Number of rounds: " +str(self.numberofrounds))
        self.roundslabel.pack()

        self.scorelabel = Label(self.master, text="Score: "+str(self.score[0])+"-"+str(self.score[1]))
        self.scorelabel.pack()

    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

def main():
    root=Tk()
    RockPaperScissors(root)
    root.mainloop()
    
if __name__=='__main__':
    main()