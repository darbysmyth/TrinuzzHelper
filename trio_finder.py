import player_manager
import tkinter as tk

class TrioFinder:

	def __init__(self):
		self.manager = player_manager.PlayerManager(player="p1")
		self.finder_win = tk.Toplevel()
		self.finder_win.geometry("730x600")
		self.finder_win.title("Find a trio")
		self.team_type_count = self.manager.get_type_count()
		self.pc_trios = self.manager.getTrios()
		self.restricted_types = [mon_type for mon_type, count in self.team_type_count.items() if count == 2]
		self.background_frame = tk.Frame(self.finder_win)
		self.background_frame.grid(row=0, column=0)
		self.available_trios = self.loadTrios()
		self.finder_win.mainloop()

	def findTrios(self):
		trios = {}
		for trio in self.pc_trios:
			if not any(mon_type in self.pc_trios[trio] for mon_type in self.restricted_types):
				trio_mons = []
				for mon_type, mon in self.pc_trios[trio].items():
					trio_mons.append(mon)
				trios[trio] = trio_mons
		return trios

	# def trioInfo(self):
	# 	self.manager.trioInfo()

	def loadTrios(self):
		trios = self.findTrios()
		if len(trios) == 0:
			return
		mon_icons = []
		c = len(trios)
		for route, mon_list in trios.items():
			trio_frame = tk.Frame(self.background_frame, highlightbackground="black", highlightthickness=2.5, width=100, height=300)
			trio_frame.grid(row=0, column=c, padx=15, pady=15)
			img_frame = tk.Frame(trio_frame)
			img_frame.grid(column=0, row=0)
			for player in self.manager.players:
				player_label = tk.Label(img_frame, text=player, padx=10)
				player_label.grid(column=0, row=self.manager.players.index(player))
			for mon in mon_list:
				mon_img = tk.PhotoImage(master=img_frame, file=f"./mons/{mon}.png")
				mon_icons.append(mon_img)
				mon_label = tk.Label(master=img_frame, image=mon_img)
				mon_label.grid(column=1, row=mon_list.index(mon))

			info_frame = tk.Frame(trio_frame)
			info_frame.grid(column=0, row=1)

			route_label = tk.Label(info_frame, text=route)
			route_label.grid(column=0, row=0)

			c = c + 1
		return mon_icons

