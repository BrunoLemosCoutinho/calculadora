import tkinter as tk
from tkinter import Frame
from tkinter import StringVar

class DisplayContainer(Frame):


	def __init__(self, root):
		Frame.__init__(self, root)
		self.parent = root
		self.configure(bg="cyan", height=5)

		self.text_display = StringVar()
		
		# Layout DisplayContainer
		self.grid(row=0 , column=0 , sticky="nwe")
		self.parent.columnconfigure(0, weight=1)

		# Call DisplayContainer widgets creation
		self.createWidgets()

	

	# Create widgets for DisplayContainer
	def createWidgets(self):

		self.label_display = tk.Label(self)
		self.label_display.configure(textvariable=self.text_display)
		self.label_display["font"] = 15
		self.label_display["bg"] = "#bebebe"
		self.label_display["relief"] = "groove"
		self.label_display["bd"] = 5
		self.label_display["height"] = 5


	# Layout widgets for DisplayContainer
		self.label_display.grid(row=0 , column=0 , sticky="nswe")
		self.columnconfigure(0, weight=1)



	def updateTextDisplay(self, text):

		self.text_display.set(text)
