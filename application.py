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
		self.decimal_separator = False
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
		print(f'decimal_separator: {self.decimal_separator}')
		print(f'Current OPERATOR: {self.operator}')
		print(f'first_number value: {self.first_number}')
		print(f'second_number value: {self.second_number}')
		print(f'first_number_status: {self.first_number_status}')
		print(f'TOTAL: {self.total}')
		print('--------------------------------------------------')

	def key_handler(self, event):
		if event.char.isdigit():
			numerical_char = event.char
			self.put_char_on_display(numerical_char)
			self.debugger()

		elif event.char in self.operators:
			operator_char = event.char
			self.operators_handler(operator_char)

		elif event.char == '=':
			if self.first_number_status == False:
				self.first_number = self.get_values_from_aggregator()
				self.resolve_handler()

			else:
				self.second_number = self.get_values_from_aggregator()
				self.resolve_handler()

		elif event.char == ',' or event.char =='.':
			if self.decimal_separator == False:

				if self.new_entry:
					zeropoint_char = '0.'
					self.put_char_on_display(zeropoint_char)
					self.decimal_separator = True
					self.debugger()
				else:
					decimal_char = '.'
					self.put_char_on_display(decimal_char)
					self.decimal_separator = True
					self.debugger()



	def buttons_handler(self, button):
		if button in range(10):
			numerical_char = str(button)
			self.put_char_on_display(numerical_char)
			self.debugger()

		elif button in self.operators:
			operator_char = str(button)
			self.operators_handler(operator_char)

		elif button == '=':
			if self.first_number_status == False:
				self.first_number = self.get_values_from_aggregator()
				self.resolve_handler()
			else:
				self.second_number = self.get_values_from_aggregator()
				self.resolve_handler()

		elif button == '.':
			if self.decimal_separator == False:

				if self.new_entry:
					zeropoint_char = '0.'
					self.put_char_on_display(zeropoint_char)
					self.decimal_separator = True
					self.debugger()
				else:
					decimal_char = '.'
					self.put_char_on_display(decimal_char)
					self.decimal_separator = True
					self.debugger()


	def put_char_on_display(self, char):
		if self.new_entry == True:
			self.aggregator = []
			self.aggregator.append(char)
			self.text.set(self.aggregator)
			self.aggregator_status = 'Active'
			self.new_entry = False
		else:
			self.aggregator.append(char)
			self.text.set(self.aggregator)
			self.aggregator_status = 'Active'

	def operators_handler(self, char):
		# Assingn the first_number
		if self.first_number_status == False:
			self.first_number = self.get_values_from_aggregator()
			self.first_number_status = True
			self.operator = char
			self.new_entry = True
			self.decimal_separator = False
			self.aggregator_status = 'Inactive'

			self.debugger()
		else:
			# Handles user changing the operators
			if (self.first_number_status == True and
					self.aggregator_status == 'Inactive'):
					if char != self.operator:
						self.operator = char

						self.debugger()
			else:
				self.second_number = self.get_values_from_aggregator()
				self.operator = char
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
				result = self.first_number / self.second_number
			except ZeroDivisionError as error:
				self.error = error
				self.conclude_operation(0)
			else:
				self.conclude_operation(result)


	def conclude_operation(self, result):

		self.total = result
		self.text.set(f'{self.total}')
		self.aggregator = [str(self.total)]
		self.aggregator_status = 'Inactive'
		self.new_entry = True
		self.decimal_separator = False
		self.first_number_status = False
		self.last_value = self.second_number  #remove or in use?

		if isinstance(self.error, ZeroDivisionError):
			self.set_to_default()
			self.text.set("Zero Division Error")

		self.debugger()



	def set_to_default(self):
		self.text.set(0)
		self.aggregator = []
		self.operator = None
		self.decimal_separator = False
		self.total = 0
		self.error = None
		self.first_number = 0
		self.second_number = 0
		self.first_number_status = False
		self.new_entry = True
		self.aggregator_status = 'Inactive'

		self.debugger()

	def press_equal(self):
		if self.first_number_status == False:
			self.first_number = self.get_values_from_aggregator()
			self.resolve_handler()		
		else:
			self.second_number = self.get_values_from_aggregator()
			self.resolve_handler()


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
		self.parent = parent

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
					command=lambda n=i: self.parent.buttons_handler(n)
					).grid(row=3, column=1, sticky='nsew')
			else:
				tkinter.Button(
					self,
					text=i,
					padx=pad, pady=pad,
					command=lambda n=i: self.parent.buttons_handler(n)
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
					command=self.parent.set_to_default
					).grid(row=i[1], column=i[2], columnspan=4, sticky='nsew')
			elif i[0] == '=':
				tkinter.Button(
					self,
					text=i[0],
					padx=pad,
					pady=pad,
					command=self.parent.press_equal
					).grid(row=i[1], column=i[2], sticky='nsew')
			else:
				tkinter.Button(
					self,
					text=i[0],
					padx=pad, pady=pad,
					command=lambda n=i[0]: self.parent.buttons_handler(n)
					).grid(row=i[1], column=i[2], sticky='nsew')



	def foo(self):
		pass


