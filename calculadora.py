


agregator = ""
result = "bbmp"


def pressNumber(num):

	global agregator
	global result

	agregator = agregator + str(num)
	result = agregator

	window.visor.updateTextDisplay(result)


def pressEqual():

	try:
		global agregator

		total = str(eval(agregator))

		window.visor.updateTextDisplay(total)
		agregator = ""

	except:
		
		window.visor.updateTextDisplay("Error")
		agregator = ""



import window