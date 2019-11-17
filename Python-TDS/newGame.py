from functions import *
from tkinter import *


root=Tk()
root.wm_title("Truth And Dare")
roundNumber=0
name=" "
TorD="It's your truth or your dare"
root.geometry("1200x800")
Truth=["Truth 1","Truth 2","Truth 3","Truth 4","Truth 5","Truth 6","Truth 7","Truth 8","Truth 9","Truth 10","Truth 11","Truth 12"]
Dare=["Dare 1","Dare 2","Dare 3","Dare 4","Dare 5","Dare 6","Dare 7","Dare 8","Dare 9","Dare 10","Dare 11","Dare 12"]

def addDare():
    addDarePopup = Tk()
    addDarePopup.wm_title("Add Player")
    label = Label(addDarePopup, text="Enter Dare in the TextBox").grid(row=0, column=0)
    namee = Entry(addDarePopup)
    namee.grid(row=1, column=0)
    add = Button(addDarePopup, text="ADD", command=lambda: d(namee))
    add.grid(row=0, column=4)
    close = Button(addDarePopup, text="Close", command=addDarePopup.destroy)
    close.grid(row=1, column=4)
    addDarePopup.mainloop()

def d(namee):
    Dare.append(namee.get())

def addTruth():
    addTruthPopup = Tk()
    addTruthPopup.wm_title("Add Player")
    label = Label(addTruthPopup, text="Enter Truth in the TextBox").grid(row=0, column=0)
    nameee = Entry(addTruthPopup)
    nameee.grid(row=1, column=0)
    add = Button(addTruthPopup, text="ADD", command=lambda: t(nameee))
    add.grid(row=0, column=4)
    close = Button(addTruthPopup, text="Close", command=addTruthPopup.destroy)
    close.grid(row=1, column=4)
    addTruthPopup.mainloop()

def t(nameee):
    Truth.append(nameee.get())

def dares():
    dLen=len(Dare)
    num=random.randint(0,dLen-1)
    truthOrDare.config(text=Dare[num])

def truths():
    tLen=len(Truth)
    num=random.randint(0,tLen-1)
    truthOrDare.config(text=Truth[num])

def show():
    #Y=500
    #for i in range(playerCount+1):
    #   Y = Y + 20
    #    Label(root, text=" ", font='Helvetica 13').place(width=100, x=100, y=Y)
    #    Label(root, text=" ", font='Helvetica 13').place(width=100, x=230, y=Y)
    Y = 450
    shw = 'SELECT Name, Score From players;'
    cursor.execute(shw)
    result=cursor.fetchall()
    for row in result:
        Y = Y + 20
        Label(root,text=row[0],font='Helvetica 11').place(width=100,x=100,y=Y)
        Label(root, text=row[1], font='Helvetica 11').place(width=100, x=230, y=Y)

def donee():
    don='UPDATE players SET Score=Score+1 Where Name="%s";' % (name)
    cursor.execute(don)
    plG()

def plG():
    global roundNumber
    global name
    name=playerGenerator()
    playerN.config(text=name)
    roundNumber=roundNumber+1
    count.config(text=roundNumber)
    show()

#Game Console:

#Player Label
pl=Label(root,text="It's Your Turn ;)",font='Helvetica 18')
pl.place(width=200,x=250,y=50)

#Player Name Label
playerN=Label(root,text="Player's Name",font='Helvetica 18 bold')
playerN.place(width=200,x=250,y=100)

#TruthOrDare Label
truthOrDare=Label(root,text=TorD,font='Helvetica 18')
truthOrDare.place(width=300,x=200,y=175)

#Truth Button
truth=Button(root,text="Truth",command=lambda: truths())
truth.place(width=200,height=60,x=125,y=250)

#Dare Button
dare=Button(root,text="Dare",command=lambda: dares())
dare.place(width=200,height=60,x=400,y=250)

#Forfeit Button
forfeit=Button(root,text="Forfeit",font="15",command=lambda:plG())
forfeit.place(width=200,height=60,x=125,y=350)

#Done Button
forfeit=Button(root,text="Done",font="15",command=lambda:donee())
forfeit.place(width=200,height=60,x=400,y=350)


#ScoreBoard :

#Score Label
score=Label(root,text="Score-",font='Helvetica 14')
score.place(width=200,x=0,y=450)


#Side Console:

#Round Label
round=Label(root,text="Round",font='Helvetica 15')
round.place(width=100,x=900,y=50)

#Round Count Label
count=Label(root,text=roundNumber,font='Helvetica 15 bold')
count.place(width=100,x=1000,y=50)

#AddDare Button
addDaree=Button(root,text="Add Dare",command=lambda: addDare())
addDaree.place(width=100,height=60,x=800,y=200)

#AddTruth Button
addTruthh=Button(root,text="Add Truth",command=lambda: addTruth())
addTruthh.place(width=100,height=60,x=1000,y=200)

#AddPlayer Button
addPlayer=Button(root,text="Add Player",command=lambda:addPlayers())
addPlayer.place(width=100,height=60,x=800,y=350)

#DeletePlayer Button
deletePlayer=Button(root,text="Delete Player",command=lambda:deletePlayers())
deletePlayer.place(width=100,height=60,x=1000,y=350)

#NewGame Button
#newGame=Button(root,text="New Game")
#newGame.place(width=100,height=60,x=800,y=500)

#Close Button
closeGame=Button(root,text="Close",command=root.destroy)
closeGame.place(width=200,height=60,x=850,y=500)

root.mainloop()