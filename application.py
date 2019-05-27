import tkinter


class Calculator(tkinter.Frame):
	operators = ['+', '-', '*', '/']
	def __init__(self, parent):
		super().__init__(parent)
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)
		self.focus_set()

		self.text = tkinter.StringVar()
		self.text.set(0)
		self.aggregator = []
		self.operator = None
		self.total = 0
		self.error = None
		self.first_number = 0
		self.second_number = 0
		self.first_number_status = False
		self.new_entry = True
		self.aggregator_status = 'Inactive'

		self.place_frames()
		self.bind("<Key>", self.key_handler)
		self.debugger()		# DEBUGGER

	def place_frames(self):
		display_frame = DisplayContainer(self
			).grid(row=0, column=0, sticky='nsew')
		buttons_frame = ButtonsContainer(self
			).grid(row=1, column=0, sticky='nsew')

	def debugger(self):
		print(f'AGGREGATOR current content: {self.aggregator}')
		print(f'AGGREGATOR current status: {self.aggregator_status}')
		print(f'new_entry: {self.new_entry}')
		print(f'Current OPERATOR: {self.operator}')
		print(f'first_number value: {self.first_number}')
		print(f'second_number value: {self.second_number}')
		print(f'first_number_status: {self.first_number_status}')
		print(f'TOTAL: {self.total}')
		print('--------------------------------------------------')

	def key_handler(self, event):
		if event.char.isdigit():
			self.put_char_on_display(event)
			self.debugger()

		if event.char in self.operators:
			self.operators_handler(event)

		if event.char == '=':
			if self.first_number_status == False:
				self.first_number = self.get_values_from_aggregator()
				self.resolve_handler()

			else:
				self.second_number = self.get_values_from_aggregator()
				self.resolve_handler()

	def put_char_on_display(self, event):
		if self.new_entry == True:
			self.aggregator = []
			self.aggregator.append(event.char)
			self.text.set(self.aggregator)
			self.aggregator_status = 'Active'
			self.new_entry = False
		else:
			self.aggregator.append(event.char)
			self.text.set(self.aggregator)
			self.aggregator_status = 'Active'

	def operators_handler(self, event):
		# Assingn the first_number
		if self.first_number_status == False:
			self.first_number = self.get_values_from_aggregator()
			self.first_number_status = True
			self.operator = event.char
			self.new_entry = True
			self.aggregator_status = 'Inactive'

			self.debugger()
		else:
			# Handles user changing the operators
			if (self.first_number_status == True and
					self.aggregator_status == 'Inactive'):
					if event.char != self.operator:
						self.operator = event.char

						self.debugger()
			else:
				self.second_number = self.get_values_from_aggregator()
				#self.second_number_status = True
				self.operator = event.char
				self.aggregator_status = 'Inactive'
				self.resolve_handler()
		# If user press any operator after typing the second value
		# the value on display will be assingned in second_number
		# variable and resolve_handler() will be called.

	def get_values_from_aggregator(self):
		values = ''.join(self.aggregator)
		return float(values)

	def resolve_handler(self):
		if self.operator == '+':
			result = self.first_number + self.second_number
			self.conclude_operation(result)

		elif self.operator == '-':
			result = self.first_number - self.second_number
			self.conclude_operation(result)

		elif self.operator == '*':
			result = self.first_number * self.second_number
			self.conclude_operation(result)

		elif self.operator == '/':
			try:
				self.first_number / self.second_number

			except ZeroDivisionError as error:
				self.error = error
			else:
				result = self.resolve_division()

			finally:
				self.conclude_operation(result)


	def conclude_operation(self, result):

		self.total = result
		self.text.set(f'{self.total}')
		self.aggregator = [str(self.total)]
		self.aggregator_status = 'Inactive'
		self.new_entry = True
		self.first_number_status = False
		self.last_value = self.second_number

		if isinstance(self.error, ZeroDivisionError):
			self.text.set(self.error.args)
			self.set_to_default()

		self.debugger()

	def set_to_default(self):
		self.aggregator = []
		self.operator = None
		self.total = 0
		self.error = None
		self.first_number = 0
		self.second_number = 0
		self.first_number_status = False
		self.new_entry = True
		self.aggregator_status = 'Inactive'

		self.debugger()



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
					padx=pad, pady=pad,
					).grid(row=3, column=1, sticky='nsew')
			else:
				tkinter.Button(
					self,
					text=i,
					padx=pad, pady=pad
					).grid(row=row, column=column, sticky='nsew')
				if column == 2:
					column = 0
					row += 1
				else:
					column += 1

		for i in [
			['+', 0, 3], ["-", 1, 3],
			['*', 2, 3], ['/', 3, 3],
			['.', 3, 0], ['=', 3, 2],
			['CLEAR', 4, 0]]:
			if i[0] == 'CLEAR':
				tkinter.Button(
					self,
					text=i[0],
					padx=pad, pady=pad,
					command=self.clear
					).grid(row=i[1], column=i[2], columnspan=4, sticky='nsew')
			elif i[0] == '=':
				tkinter.Button(
					self,
					text=i[0],
					padx=pad,
					pady=pad,
					command=self.equal
					).grid(row=i[1], column=i[2], sticky='nsew')
			else:
				tkinter.Button(
					self,
					text=i[0],
					padx=pad, pady=pad,
					command=self.foo
					).grid(row=i[1], column=i[2], sticky='nsew')


	def clear(self):
		pass

	def equal(self):
		pass
	def foo(self):
		pass


