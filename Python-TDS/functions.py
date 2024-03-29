from tkinter import *
from database import *
import random

playerCount=0

def addPlayers():
    addPlayerPopup=Tk()
    addPlayerPopup.wm_title("Add Player")
    label=Label(addPlayerPopup,text="Enter Player's Name in the TextBox").grid(row=0,column=0)
    name=Entry(addPlayerPopup)
    name.grid(row=1,column=0)
    add=Button(addPlayerPopup,text="ADD",command=lambda: addPlayer(name))
    add.grid(row=0,column=4)
    close = Button(addPlayerPopup, text="Close",command=addPlayerPopup.destroy)
    close.grid(row=1,column=4)
    addPlayerPopup.mainloop()

def addPlayer(name):
    global playerCount
    add='INSERT INTO players(Name,Score) VALUES("%s",0);' % (name.get())
    cursor.execute(add)
    playerCount=playerCount+1
    show()
    

def playerGenerator():
    global playerCount
    num=random.randint(1,playerCount)
    pl_name=("SELECT Name From players Where ID='%d';" % (num))
    cursor.execute(pl_name)
    results = cursor.fetchall()
    for row in results:
        return row[0]

def deletePlayers():
    deletePlayerPopup=Tk()
    deletePlayerPopup.wm_title("Delete Player")
    label=Label(deletePlayerPopup,text="Enter Player's Name in the TextBox").grid(row=0,column=0)
    namee=Entry(deletePlayerPopup)
    namee.grid(row=1,column=0)
    delete=Button(deletePlayerPopup,text="DELETE",command=lambda: deletePlayer(namee))
    delete.grid(row=0,column=4)
    close = Button(deletePlayerPopup, text="Close",command=deletePlayerPopup.destroy)
    close.grid(row=1,column=4)
    deletePlayerPopup.mainloop()


def deletePlayer(namee):
    global playerCount
    delt='DELETE FROM players WHERE Name="%s";' % (namee.get())
    cursor.execute(delt)
    if(playerCount-1):
        playerCount=playerCount-1
    show()
