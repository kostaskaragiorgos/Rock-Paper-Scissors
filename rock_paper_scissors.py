from tkinter import Menu, Button, StringVar, OptionMenu, messagebox as msg, Tk, Label
from tkinter import simpledialog, scrolledtext, WORD
from random import choice
import logging

class RockPaperScissors():
    def __init__(self, master):
        self.master = master
        self.master.title("ROCK PAPER SCISSORS")
        self.master.geometry("250x300")
        self.master.resizable(False, False)
        self.score = [0, 0]
        self.choices = ["", ""]
        self.numberofrounds = 0

        self.roundslabel = Label(self.master, text="Number of rounds: " +str(self.numberofrounds))
        self.roundslabel.pack()

        self.scorelabel = Label(self.master,
                                text="Score: "+str(self.score[0])+"-"+str(self.score[1]))
        self.scorelabel.pack()


        self.category_list = list(["Rock", "Paper", "Scissors"])
        self.var_cat_list = StringVar(master)
        self.var_cat_list.set(self.category_list[0])
        self.popupcatlistmenu = OptionMenu(self.master, self.var_cat_list, *self.category_list)
        self.popupcatlistmenu.pack()

        self.playb = Button(self.master, text="Play", state='disabled', command=self.play)
        self.playb.pack()

        self.log_area = scrolledtext.ScrolledText(self.master,
                                                  wrap=WORD,
                                                  width=40,
                                                  height=10,
                                                  font=("Times New Roman", 15))
        self.log_area.configure(state='disabled')
        self.log_area.pack()

        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New Game", accelerator='Ctrl+O', command=self.newgame)
        self.file_menu.add_command(label="Load Game")
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())

    
    def play(self):
        self.choices[0] = self.var_cat_list.get()
        self.choices[1] = choice(self.category_list)
        self.numberofrounds -= 1
        if self.choices[0] == self.choices[1]:
            msg.showinfo("Tie", "Tie")
        elif self.choices[0] == "Rock" and self.choices[1] != "Paper":
            self.score[0] += 1
            msg.showinfo("User", "User")
        elif self.choices[0] == "Paper" and self.choices[1] == "Rock":
            self.score[0] += 1
            msg.showinfo("User", "User")
        elif self.choices[0] == "Scissors" and self.choices[1] == "Paper":
            self.score[0] += 1
            msg.showinfo("User", "User")
        else:
            self.score[1] += 1
            msg.showinfo("Computer", "Computer")
        logging.basicConfig()
        logger1 = logging.getLogger('logger1')
        logger1.setLevel(logging.INFO)
        #self.log_area.configure(state='normal')
        #self.log_area.insert("insert",chars = logger1.info("Round"+ str(self.numberofrounds) + "Player" + str(self.score[0]) + "Computer" + str(self.score[1])))
        #self.log_area.configure(state='disabled')
        self.scorelabel['text'] = "Score: "+str(self.score[0])+"-"+str(self.score[1])
        self.roundslabel['text'] = "Number of rounds: " +str(self.numberofrounds)
        if self.numberofrounds == 0:
            self.playb.configure(state='disabled')
            if self.score[0] > self.score[1]:
                msg.showinfo("User is the winner", "User is the winner")
            elif  self.score[0] < self.score[1]:
                msg.showinfo("Computer is the winner", "Computer is the winner")
            else:
                msg.showinfo("Tie", "Tie")


    def newgame(self):
        self.numberofrounds = simpledialog.askinteger("Number of rounds",
                                                      "Enter the number of rounds",
                                                      parent=self.master,
                                                      minvalue=1)
        while self.numberofrounds == 0 or self.numberofrounds is None:
            self.numberofrounds = simpledialog.askinteger("Number of rounds",
                                                          "Enter the number of rounds",
                                                          parent=self.master,
                                                          minvalue=1)
        self.roundslabel['text'] = "Number of rounds: " +str(self.numberofrounds)
        self.score[0] = 0
        self.score[1] = 0
        self.scorelabel['text'] = "Score: "+str(self.score[0])+"-"+str(self.score[1])
        self.playb.configure(state='normal')
        

    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

def main():
    root = Tk()
    RockPaperScissors(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()