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
		self.aggregator = ['0']
		self.values = [0.0]
		self.operator_counter = 0
		self.operator = None
		self.total = 0
		self.error = None

		self.place_frames()
		self.bind("<Key>", self.key_handler)
		self.focus_set()

		self.debugger()		# DEBUGGER



	def debugger(self):
		print(f'Status atual de AGGREGATOR: {self.aggregator}')
		print(f'OPERADOR atual: {self.operator}')
		print(f'Contador de Operator:{self.operator_counter}')
		print(f'Status atual de VALUES: {self.values}')
		print(f'O valor de TOTAL: {self.total}')
		print('---------------------------------------')

	def place_frames(self):
		display_frame = DisplayContainer(self
			).grid(row=0, column=0, sticky='nsew')
		buttons_frame = ButtonsContainer(self
			).grid(row=1, column=0, sticky='nsew')

	def put_char_on_display(self, event):
		if self.aggregator[0] == '0':
			self.aggregator.pop(0)
			self.aggregator.append(event.char)
			self.text.set(self.aggregator)
		else:
			self.aggregator.append(event.char)
			self.text.set(self.aggregator)

	def get_values_from_aggregator(self):
		values = ''.join(self.aggregator)
		return float(values)

	def conclude_operation(self, result):

		self.total = result
		self.text.set(f'{result}')
		self.aggregator = ['0']
		self.operator = None
		self.operator_counter = 0
		self.values = [result]

		if self.error is ZeroDivisionError:
			self.text.set('Error: Division By Zero')


		self.debugger()


	def resolve_sum(self):
		last_aggregator_value = self.get_values_from_aggregator()
		self.values.append(last_aggregator_value)
		return sum(self.values)

	def resolve_subtraction(self):
		last_aggregator_value = self.get_values_from_aggregator()
		self.values.append(last_aggregator_value)
		# Removing zeros from values list
		new_values_list = [value for value in self.values if value > 0]
		a, b = new_values_list
		return a - b

	def resolve_multiplication(self):
		last_aggregator_value = self.get_values_from_aggregator()
		self.values.append(last_aggregator_value)
		# Removing zeros from values list
		new_values_list = [value for value in self.values if value > 0]
		a, b = new_values_list
		return a * b

	def resolve_division(self):
		# Removing zeros from values list
		new_values_list = [value for value in self.values if value > 0]
		last_aggregator_value = self.get_values_from_aggregator()
		new_values_list.append(last_aggregator_value)
		a, b = new_values_list

		try:
			a / b
		except ZeroDivisionError as error:
			self.error = error
			print(self.error)
			return 0
		else:
			return a / b
	



	def resolve(self):
		if self.operator == '+':
			result = self.resolve_sum()
			self.conclude_operation(result)
		elif self.operator == '-':
			result = self.resolve_subtraction()
			self.conclude_operation(result)
		elif self.operator == '*':
			result = self.resolve_multiplication()
			self.conclude_operation(result)
		elif self.operator == '/':
			result = self.resolve_division()
			self.conclude_operation(result)


	def key_handler(self, event):
		if event.char.isdigit():
			self.put_char_on_display(event)
			self.debugger()

		if event.char in self.operators:
			self.operators_handler(event)

	def operators_handler(self, event):
		if self.operator_counter == 0:
			self.operator = event.char
			self.values.append(self.get_values_from_aggregator())
			self.aggregator = ['0']
			self.operator_counter = 1
			self.debugger()
			# make button change color to indicate
			# it is active and is the option
		else:
			self.resolve()
			# resolve values


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



