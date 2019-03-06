import tkinter as tk
from tkinter import Frame
import calculadora


class ButtonsContainer(Frame):

	def __init__(self , root):
		Frame.__init__(self, root)
		self.parent = root
		self.configure(bg="yellow")



		# Layout ButtonsContainer
		self.grid(row=1 , column=0 , sticky ="nsew")
		self.parent.rowconfigure(1, weight=1)
		self.parent.columnconfigure(0, weight=1)

		# Call ButtonsContainer widgets creation
		self.createWidgets()

		# Binding keyboard inputs events
		for i in range(10):
			self.parent.bind(str(i), self.keysHandler)

		self.parent.bind("/", self.keysHandler)
		self.parent.bind("*", self.keysHandler)
		self.parent.bind("-", self.keysHandler)
		self.parent.bind("+", self.keysHandler)
		self.parent.bind(".", self.keysHandler)
		self.parent.bind(",", self.keysHandler)
		self.parent.bind("<Return>", self.returnKeyHandler)
		self.parent.bind("<BackSpace>", self.bsHandler)



	# Create widgets for ButtonsContainer
	def createWidgets(self):

		button_padx = 15
		button_pady = 15		

		self.button_1 = tk.Button(self, text="1", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(1))
		self.button_2 = tk.Button(self, text="2", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(2))
		self.button_3 = tk.Button(self, text="3", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(3))
		self.button_4 = tk.Button(self, text="4", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(4))
		self.button_5 = tk.Button(self, text="5", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(5))
		self.button_6 = tk.Button(self, text="6", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(6))
		self.button_7 = tk.Button(self, text="7", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(7))
		self.button_8 = tk.Button(self, text="8", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(8))
		self.button_9 = tk.Button(self, text="9", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(9))
		self.button_0 = tk.Button(self, text="0", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(0))

		self.button_open_parens = tk.Button(self, text="(", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber("("))
		self.button_close_parens = tk.Button(self, text=")", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber(")"))


		self.button_dot = tk.Button(self, text=".", padx= button_padx, pady=button_pady, command=lambda: calculadora.pressNumber("."))
		self.button_plus = tk.Button(self, text="+", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber("+"))
		self.button_minus = tk.Button(self, text="-", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber("-"))
		self.button_multiply = tk.Button(self, text="*", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber("*"))
		self.button_divide = tk.Button(self, text="/", padx=button_padx, pady=button_pady, command=lambda: calculadora.pressNumber("/"))
		self.button_equal = tk.Button(self, text="=", padx=button_padx, pady=button_pady, command=calculadora.pressEqual)
		self.button_clear = tk.Button(self, text="CLEAR", padx=button_padx, pady=button_pady, command=calculadora.pressClear)

	# Layout widgets for ButtonsContainer
		self.button_1.grid(row=0, column=0, sticky="nswe")
		self.button_2.grid(row=0, column=1, sticky="nswe")
		self.button_3.grid(row=0, column = 2, sticky="nswe")
		self.button_4.grid(row=1, column=0, sticky="nswe")
		self.button_5.grid(row=1, column=1, sticky="nswe")
		self.button_6.grid(row=1, column=2, sticky="nswe")
		self.button_7.grid(row=2, column=0, sticky="nswe")
		self.button_8.grid(row=2, column=1, sticky="nswe")
		self.button_9.grid(row=2, column=2, sticky="nswe")

		self.button_open_parens.grid(row=3, column=0, sticky="nswe")
		self.button_close_parens.grid(row=3, column=2, sticky="nswe")

		self.button_0.grid(row=3, column=1, sticky="nswe")
		self.button_dot.grid(row=4, column=2, sticky="nswe")
		self.button_plus.grid(row=0 , column=3, sticky="nswe")
		self.button_minus.grid(row=1 , column=3, sticky="nswe")
		self.button_multiply.grid(row=2 , column=3, sticky="nswe")
		self.button_divide.grid(row=3 , column=3, sticky="nswe")

		self.button_equal.grid(row=4 , column=3, sticky="nswe")
		self.button_clear.grid(row=4 , columnspan=2, sticky="nswe")

		for x in range(0,5):
			self.rowconfigure(x, weight=1)

		for i in range(0, 4):
			self.columnconfigure(i, weight=1)

	# Handler: keyboard events
	def keysHandler(self, event):
		if event.char == ",":
			calculadora.pressNumber(".")
		else:
			calculadora.pressNumber(event.char)

	# Handler: Return key
	def returnKeyHandler(self, event):
		calculadora.pressEqual()

	# Handler: BackSpace key
	def bsHandler(self,event):
		calculadora.pressBS()
		





