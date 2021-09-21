import tkinter as tk
from tkinter import ttk
import add_win
import PC_win
import team_win
import player_manager
import trio_finder

main_win = tk.Tk()
main_win.title("Trinuzz Helper")
main_win.geometry("700x400")

#TODO after implementing main functionality style project better, frames, borders, backgrounds, etc

#TODO maybe create all managers here and pass them down through each window created


#TODO Merge team and PC into one window MUCH MUCH MUCH easier to do everything

#TODO Death Box
#TODO Evolutions
#TODO PC pages? for when theres more than 30
#TODO Keep track of which routes we've done

def addtrio():
	addwin = add_win.AddWin()

def findTrio():
	findwin = trio_finder.TrioFinder()


# Need individual buttons for each players PC
# add 3 sections in teh window layout for each player
def lookatpc():
	pcwin = PC_win.PcWin()

def lookatteam():
	teamwin = team_win.TeamWin()


# Buttons

add_trio = tk.Button(text="Add Trio", command=addtrio)
pc = tk.Button(text="Look at PC", command=lookatpc)
team = tk.Button(text="Look at Team", command=lookatteam)
find_trio = tk.Button(text="Find available trio", command=findTrio)

add_trio.grid(row=0, column=0, padx=50)
pc.grid(row=0, column=1, padx=50)
team.grid(row=0, column=2, padx=50)
find_trio.grid(row=0, column=3, padx=50)
main_win.mainloop()
