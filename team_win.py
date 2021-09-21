import tkinter as tk
from tkinter import ttk
import player_manager


class TeamWin:

	def __init__(self):
		self.manager = player_manager.PlayerManager(player="p1")
		self.team_win = tk.Toplevel()
		self.team_win.geometry("750x250")
		self.team_win.resizable(False, False)
		# title will have the player name as a variable passed to the teamwin init
		self.team_win.title(f"p1's team")
		self.team_frame = tk.Frame(self.team_win)
		self.team_frame.grid(row=0, column=0)
		self.team = self.loadTeam()
		self.team_win.mainloop()


	#TODO updating needs to be fixed when the mon is moved
	def getInfo(self, mon):
		self.manager.monInfo(mon, master_win=self, data_container_label="Team")

	def loadTeam(self):
		team = self.manager.getTeam()
		if len(team) == 0:
			return
		mon_icons = []
		for i in range(len(team)):
			mon_frame = tk.Frame(self.team_frame, highlightbackground="black",
			                     highlightthickness=2.5, width=100, height=100)
			mon_frame.grid(row=0, column=i, padx=10, pady=10)
			mon_img = tk.PhotoImage(master=mon_frame, file=f"./mons/{team[i][0]}.png")
			mon_btn = tk.Button(mon_frame, image=mon_img,
			                    command=lambda mon=team[i][0]: self.getInfo(mon))
			mon_icons.append([mon_btn, mon_img])
			mon_btn.grid(row=0, column=0, padx=5, pady=5)
			mon_route = tk.Label(mon_frame, text=f"{team[i][1]}", font=("Arial", 10, "bold"))
			mon_route.grid(row=1, column=0)
		return mon_icons

	def rebuild(self):
		self.team_frame.destroy()
		self.team_frame = tk.Frame(self.team_win)
		self.team_frame.grid(row=0, column=0)
		self.team = self.loadTeam()

