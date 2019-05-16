import tkinter


class Calculator(tkinter.Frame):
	operators = ['+', '-', '*', '/']
	def __init__(self, parent):
		super().__init__(parent)
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		self.text = tkinter.StringVar()
		self.text.set(0)
		self.aggregator = ''
		self.result = [0.0]
		self.operator_counter = 0

		self.place_frames()
		self.bind("<Key>", self.key_handler)
		self.focus_set()

	def place_frames(self):
		display_frame = DisplayContainer(self
			).grid(row=0, column=0, sticky='nsew')
		buttons_frame = ButtonsContainer(self
			).grid(row=1, column=0, sticky='nsew')

	def put_char(self, event):
		self.aggregator += event.char
		self.text.set(self.aggregator)

	def resolve(self):
		if self.result[1] == '+':
			self.result.pop(1)
			final_result = sum(self.result)
			self.result = final_result
			self.text.set(str(final_result))
			self.operator_counter = 0
		elif self.result[1] == '-':
			pass


	def key_handler(self, event):
		if event.char.isdigit():
			self.put_char(event)
			print(f'Tecla pressionada: {event.char}')
			print(f'Status atual de AGGREGATOR: {self.aggregator}')
			print(f'Status atual de RESULT: {self.result}')
			print('---------------------------------------')

		if event.char in self.operators:
			self.operators_handler(event)

	def operators_handler(self, event):
		if self.operator_counter == 0:
			if isinstance(self.result[-1], float):
				self.result.append(event.char)
				self.result.append(float(self.aggregator))
				self.aggregator = ''
				self.operator_counter = 1
				print(f'Tecla pressionada: {event.char}')
				print(f'Status atual de AGGREGATOR: {self.aggregator}')
				print(f'Status atual de RESULT: {self.result}')
		else:
			pass
			# resolve result


class DisplayContainer(tkinter.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

		tkinter.Label(
			self,
			background='lightgrey',
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



