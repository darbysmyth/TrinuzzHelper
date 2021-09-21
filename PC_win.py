import tkinter as tk
import player_manager

# TODO need to pass this object to monInfo window, not sure how
class PcWin:
	# player="p1" is temp

	def __init__(self):
		self.manager = player_manager.PlayerManager(player="p1")
		self.pc_win = tk.Toplevel()
		self.pc_win.geometry("730x600")
		self.pc_win.title("PC")
		self.pc_frame = tk.Frame(self.pc_win)
		self.pc_frame.grid(row=0, column=0)
		self.pc_mon = self.loadPC()
		self.pc_win.mainloop()

		#TODO this is a tricky function, not sure how to continue it after the infobox closes
	def getInfo(self, mon):
		self.manager.monInfo(mon, master_win=self, data_container_label="PC")

	# need to throw error when PC is empty
	def loadPC(self):
		mons = self.manager.getPC()
		if len(mons) == 0:
			return
		mon_icons = []
		for r in range(5):
			for c in range(6):
				mon_frame = tk.Frame(self.pc_frame, highlightbackground="black", highlightthickness=2.5, width=100, height=100)
				mon_frame.grid(row=r, column=c, padx=10, pady=10)
				mon_img = tk.PhotoImage(master=mon_frame, file=f"./mons/{mons[c + r * 6][0]}.png")
				mon_btn = tk.Button(mon_frame, image=mon_img,
				                    command=lambda mon=mons[c + r * 6][0]: self.getInfo(mon))
				mon_icons.append([mon_btn, mon_img])
				mon_btn.grid(row=0, column=0, padx=5, pady=5)
				mon_route = tk.Label(mon_frame, text=f"{mons[c + r * 6][1]}", font=("Arial", 10, "bold"))
				mon_route.grid(row=1, column=0)
				if len(mon_icons) == len(mons):
					return mon_icons

	def rebuild(self):
		self.pc_frame.destroy()
		self.pc_frame = tk.Frame(self.pc_win)
		self.pc_frame.grid(row=0, column=0)
		self.pc_mon = self.loadPC()

