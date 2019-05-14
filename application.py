import tkinter


class Calculator(tkinter.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		self.text = tkinter.StringVar()
		self.text.set('0')
		self.aggregator = ''

		self.place_frames()

	def place_frames(self):
		pass


class DisplayContainer(tkinter.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

		tkinter.Label(
			self,
			background='grey',
			relief='ridge',
			border=5,
			textvariable=self.parent.text,
			).pack(fill='both', expand=1)

class ButtonsContainer(tkinter.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		for x in range(0, 5):
			self.rowconfigure(x, weight=1)
			if x < 4:
				self.columnconfigure(x, weight=1)

		self.create_buttons()

	def create_buttons(self):
		pad=15
		row = 0
		column = 0
		for i in range(10):
			if i==0:
				tkinter.Button(
					self,
					text=i,
					padx=pad,
					pady=pad,
					).grid(row=3, column=1, sticky='nsew')
			else:
				tkinter.Button(
					self,
					text=i,
					padx=pad,
					pady=pad
					).grid(row=row, column=column, sticky='nsew')
				if column == 2:
					column = 0
					row += 1
				else:
					column += 1



