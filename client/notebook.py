from tkinter import *

class notebook:
	
	# initialization. receives the master widget
	# reference and the notebook orientation
	def __init__(self, master, side=LEFT, select_color = 'gray', select_bg = 'gray'):
		
		self.active_fr = None
		self.count = 0
		self.choice = IntVar(0)
		self.number_of_screens=0
		self.select_color = select_color
		self.select_bg = select_bg

		# allows the TOP and BOTTOM
		# radiobuttons' positioning.
		if side in (TOP, BOTTOM):
			self.side = LEFT
		else:
			self.side = TOP

		# creates notebook's frames structure
		self.rb_fr = Frame(master, borderwidth=2, relief=RIDGE)
		self.rb_fr.pack(side=side, fill=BOTH)
		self.screen_fr = Frame(master, borderwidth=2, relief=RIDGE)
		self.screen_fr.pack(fill=BOTH)

	# return a master frame reference for the external frames (screens)
	def __call__(self):
		return self.screen_fr	

	# add a new frame (screen) to the (bottom/left of the) notebook
	def add_screen(self, fr, title):

		b = Radiobutton(self.rb_fr, text=title, indicatoron=0, \
			variable=self.choice, value=self.count, \
			command=lambda: self.display(fr),height=6, width=13, selectcolor=self.select_color, bg=self.select_bg, font=("Calibri", 16))

		b.grid(row=self.number_of_screens,column=0, sticky="nsew")
		self.rb_fr.rowconfigure(self.number_of_screens, weight=1)
		self.number_of_screens+=1
		''
		
		# ensures the first frame will be
		# the first selected/enabled
		if not self.active_fr:
			fr.pack(fill=BOTH, expand=1)
			self.active_fr = fr

			self.count += 1

		# returns a reference to the newly created
		# radiobutton (allowing its configuration/destruction)         
		return b

	# hides the former active frame and shows 
	# another one, keeping its reference
	def display(self, fr):
		
		self.active_fr.forget()
		fr.pack(fill=BOTH, expand=1)
		self.active_fr = fr
