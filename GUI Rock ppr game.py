import random
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Rock Paper Pencil Scissor Game')

tuple_game=("Rock","Paper",'Pencil','Scissor')
score = 0
score_list = [0]
high_score = max(score_list)

e = Entry(root,font=50)
e1 = Entry(root,font=50)
e2 = Entry(root,font=50)
e3 = Entry(root,font=50)
e4 = Entry(root,font=50)

e.grid(row=1,column=1)
e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
e3.grid(row=4,column=1)
e4.grid(row=5,column=1)

e.insert(0,"I'm smarter than You")
e1.insert(0,"Click on something")
e2.insert(0,"Game not started")
e3.insert(0,"0")
e4.insert(0,high_score)

label_heading = Label(root,text="Rock Paper Pencil Scissor Game",font=('Helvitica',30))
label_computer = Label(root,text="Computer's Move",font=50)
label_user = Label(root,text="Your Move",font=50)
label_result = Label(root,text="Results",font=50)
label_score = Label(root,text="Score",font=50)
label_high_score = Label(root,text="High Score",font=50)

label_heading.grid(row=0,column=0,padx=5,pady=5,columnspan=2)
label_computer.grid(row=1,column=0,padx=5,pady=5)
label_user.grid(row=2,column=0,padx=5,pady=5)
label_result.grid(row=3,column=0,padx=5,pady=5)
label_score.grid(row=4,column=0,padx=5,pady=5)
label_high_score.grid(row=5,column=0,padx=5,pady=5)

def button_click(string):
    global user
    global score
    global high_score
    global score_list
    user = string
    random_num = random.randint(0, 3)
    computer = tuple_game[(random_num - 1)]

    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

    if user == "Rock" and computer == "Paper":
        e2.insert(0,"You Lost!")
        score-=10
    elif user == "Rock" and computer == "Pencil":
        e2.insert(0,"You Won! \n")
        score+=20
    elif user == "Rock" and computer == "Scissor":
        e2.insert(0,"You Won! \n")
        score+=20
    elif user == "Pencil" and computer == "Paper":
        e2.insert(0,"You Won! \n")
        score+=20
    elif user == "Pencil" and computer == "Rock":
        e2.insert(0,"You Lost! \n")
        score-=10
    elif user == "Pencil" and computer == "Scissor":
        e2.insert(0,"You Lost! \n")
        score-=10
    elif user == "Paper" and computer == "Rock":
        e2.insert(0,"You Won! \n")
        score+=20
    elif user == "Paper" and computer == "Pencil":
        e2.insert(0,"You Lost! \n")
        score-=10
    elif user == "Paper" and computer == "Scissor":
        e2.insert(0,"You Lost! \n")
        score-=10
    elif user == "Scissor" and computer == "Rock":
        e2.insert(0,"You Lost! \n")
        score-=10
    elif user == "Scissor" and computer == "Paper":
        e2.insert(0,"You Won! \n")
        score+=20
    elif user == "Scissor" and computer == "Pencil":
        e2.insert(0,"You Lost! \n")
        score-=10
    elif user==computer:
        e2.insert(0,"Its a Tie \n")

    score_list.append(score)
    high_score = max(score_list)

    e.insert(0,computer)
    e1.insert(0,user)
    e3.insert(0,score)
    e4.insert(0,high_score)
    
def reset_game():
    global score 
    score = 0
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

    e.insert(0,"I'm smarter than You")
    e1.insert(0,"Click on something")
    e2.insert(0,"Game not started")
    e3.insert(0,"0")

def open():
    top = Toplevel()
    top.title('Credits')
    top_label1 = Label(top,text="App Developed by Rishabh Bhat",font=80).pack()

    top_btn = Button(top,text="Close",font=40,command=top.destroy).pack()

def open_rules():
    top2 = Toplevel()
    top2.title('Game Rules')
    top2_label1 = Label(top2,text="Game Rule Book",font=('Helvitica',30)).pack()
    top2_label2 = Label(top2,text="+20 Points for Winning a Round",bg="green",width=28,font=80).pack()
    top2_label3 = Label(top2,text="-10 Points for Losing a Round",bg="red",width=28,font=80).pack()

button_rock = Button(root,text="Rock",font=80,width=17,height=5,command=lambda:button_click("Rock"))
button_paper = Button(root,text="Paper",font=80,width=17,height=5,command=lambda:button_click("Paper"))
button_pencil = Button(root,text="Pencil",font=80,width=17,height=5,command=lambda:button_click("Pencil"))
button_scissor = Button(root,text="Scissor",font=80,width=17,height=5,command=lambda:button_click("Scissor"))
button_reset = Button(root,text="New Game",font=60,width=10,height=1,command=reset_game)
button_credits = Button(root,text="Credits",font=60,width=10,height=1,command=open)
button_quit = Button(root,text="Quit",font=60,width=10,height=1,command=root.destroy)
button_game_rules = Button(root,text="Game Rules",font=60,width=10,height=1,command=open_rules)

button_rock.grid(row=6,column=0,padx=5,pady=5)
button_paper.grid(row=6,column=1,padx=5,pady=5)
button_pencil.grid(row=7,column=0,padx=5,pady=5)
button_scissor.grid(row=7,column=1,padx=5,pady=5)
button_reset.grid(row=8,column=0,padx=5,pady=5)
button_credits.grid(row=8,column=1,padx=5,pady=5)
button_quit.grid(row=9,column=0,padx=5,pady=5)
button_game_rules.grid(row=9,column=1,padx=5,pady=5)

mainloop()