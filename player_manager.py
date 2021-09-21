import pandas as pd
import tkinter as tk


class PlayerManager:

	# touch up this player stuff, its a mess
	def __init__(self, player=None):
		self.player = player
		self.players = ["p1", "p2", "p3"]
		self.others = [player for player in self.players if player != self.player]

	# temp mon, type, route maybe make pokemon object in the future
	# check index_col
	def addMon(self, mon, type, route):
		new_mon = pd.DataFrame({"mon": [mon], "type": [type], "route": [route]})
		team = pd.read_csv(f"playerdata/teams/{self.player}Team.csv")
		if team.size != 18:
			team = team.append(new_mon, ignore_index=True).set_index("mon")
			team.to_csv(f"playerdata/teams/{self.player}Team.csv")
		else:
			PC = pd.read_csv(f"playerdata/PCs/{self.player}PC.csv")
			PC = PC.append(new_mon, ignore_index=True).set_index("mon")
			PC.to_csv(f"playerdata/PCs/{self.player}PC.csv")

	# TODO could probably mix these two functions into 1 with an arg specifying the container
	def getPC(self):
		PC = pd.read_csv(
			f"playerdata/PCs/{self.player}PC.csv")
		listofmons = []
		for mon in PC.itertuples(index=False):
			listofmons.append([mon.mon, mon.route])
		return listofmons

	def getTeam(self):
		team = pd.read_csv(f"playerdata/teams/{self.player}Team.csv")
		listofmons = []
		for mon in team.itertuples(index=False):
			listofmons.append([mon.mon, mon.route])
		return listofmons

	def monInfo(self, mon, master_win, data_container_label):
		# show name, type, route
		# and mons it is paired with
		not_container = ["PC", "Team"]
		not_container.remove(data_container_label)
		mon_win = tk.Toplevel()
		mon_win.geometry("300x300")
		mon_win.title(mon)
		container_file = pd.read_csv(f"playerdata/{data_container_label}s/{self.player}{data_container_label}.csv")
		not_container_file = pd.read_csv(f"playerdata/{not_container[0]}s/{self.player}{not_container[0]}.csv")

		# TODO add route as an accessible variable here, its used quite a bit

		# TODO fix these functions, the double set_index seems inefficient, must be a way to search by route immediately
		def moveMon():
			route = container_file.set_index("mon").loc[mon]["route"]
			# TODO using only my file, need to read player specific file
			for player in self.players:
				player_container = pd.read_csv(
				f"playerdata/{data_container_label}s/{player}{data_container_label}.csv").set_index("route", drop=False)
				not_player_container = pd.read_csv(
				f"playerdata/{not_container[0]}s/{player}{not_container[0]}.csv").set_index("route", drop=False)
				mon_to_move = player_container.loc[route]
				# TODO add check if moving to team to see if team is full, if full error box
				not_player_container = not_player_container.append(mon_to_move)
				player_container = player_container.drop(route)
				player_container = player_container.set_index("mon")
				not_player_container = not_player_container.set_index("mon")
				player_container.to_csv(f"playerdata/{data_container_label}s/{player}{data_container_label}.csv")
				not_player_container.to_csv(f"playerdata/{not_container[0]}s/{player}{not_container[0]}.csv")
			master_win.rebuild()

		# TODO after PC and Team have been merged implement this
		def swapMon():
			pass

		def removeMon():
			route = container_file.set_index("mon").loc[mon]["route"]
			for player in self.players:
				player_container = container_file.set_index("route", drop=False)
				player_container = player_container.drop(route)
				player_container = player_container.set_index("mon")
				player_container.to_csv(f"playerdata/{data_container_label}s/{player}{data_container_label}.csv")
			master_win.rebuild()

		mon_img = tk.PhotoImage(master=mon_win, file=f"mons/{mon}.png")
		mon_lbl = tk.Label(mon_win, image=mon_img)
		mon_lbl.grid(row=0, column=0, padx=20, pady=20)
		info_panel = tk.Frame(mon_win)
		mon_actions = tk.Frame(mon_win)
		name_lbl = tk.Label(info_panel, text=mon)
		type_lbl = tk.Label(info_panel, text=container_file.set_index("mon").loc[mon]["type"])
		route_lbl = tk.Label(info_panel, text=container_file.set_index("mon").loc[mon]["route"])

		move_btn = tk.Button(info_panel, text=f"Move to {not_container[0]}", command=moveMon)
		swap_btn = tk.Button(info_panel, text=f"Swap from {not_container[0]}", command=swapMon)
		remove_btn = tk.Button(info_panel, text=f"Remove trio from game", command=removeMon)
		move_btn.grid(row=0, column=0, pady=5)
		swap_btn.grid(row=1, column=0, pady=5)
		remove_btn.grid(row=2, column=0, pady=5)

		name_lbl.grid(row=0, column=0)
		type_lbl.grid(row=1, column=0)
		route_lbl.grid(row=2, column=0)

		linked_mon_imgs = []
		c = 0
		link_container = tk.Frame(mon_win)
		pair_label = tk.Label(link_container, text="Paired With:")
		pair_label.grid(row=0, column=0, columnspan=2)
		for player in self.others:
			link_frame = tk.Frame(link_container)
			# can shorten this line below
			player_container = pd.read_csv(
				f"playerdata/{data_container_label}s/{player}{data_container_label}.csv").set_index(
				"route")
			# TODO Find desired route beforehand instead of doing this mess each time below
			linked_mon = player_container.loc[container_file.set_index("mon").loc[mon]["route"]]["mon"]
			linked_img = tk.PhotoImage(master=link_frame, file=f"mons/{linked_mon}.png")
			linked_mon_imgs.append(linked_img)
			linked_mon_lbl = tk.Label(link_frame, image=linked_img)
			linked_player = tk.Label(link_frame, text=player)
			mon_name = tk.Label(link_frame, text=linked_mon)
			linked_mon_lbl.grid(row=0, column=0)
			linked_player.grid(row=1, column=0)
			mon_name.grid(row=2, column=0)
			link_frame.grid(row=2, column=c)
			c = c + 1
		link_container.grid(row=3, column=0, columnspan=2)
		info_panel.grid(row=0, column=1)

		mon_win.mainloop()

	def get_type_count(self):
		def getTypes(player):
			team = pd.read_csv(f"playerdata/Teams/{player}Team.csv")
			listoftypes = []
			for mon in team.itertuples(index=False):
				listoftypes.append(mon.type)
			return listoftypes

		type_count = {"Bug": 0,
		              "Dark": 0,
		              "Dragon": 0,
		              "Electric": 0,
		              "Fighting": 0,
		              "Fire": 0,
		              "Flying": 0,
		              "Ghost": 0,
		              "Grass": 0,
		              "Ground": 0,
		              "Ice": 0,
		              "Normal": 0,
		              "Poison": 0,
		              "Psychic": 0,
		              "Rock": 0,
		              "Steel": 0,
		              "Water": 0}
		for player in self.players:
			types = getTypes(player)
			for type in types:
				type_count[type] = type_count[type] + 1
		return type_count

	def getTrios(self):
		trios = {}
		for player in self.players:
			PC = pd.read_csv(f"playerdata/PCs/{player}PC.csv")
			for trio in PC.itertuples():
				if trio.route in trios:
					trios[trio.route][trio.type] = trio.mon
				else:
					trios[trio.route] = {}
					trios[trio.route][trio.type] = trio.mon
		return trios


# used for testing purposes
