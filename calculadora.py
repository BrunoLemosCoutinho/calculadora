
agregator = ""
result = ""


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

	except ZeroDivisionError:

		window.visor.updateTextDisplay("Erro: Divisão por zero")
		agregator = ""

	except:
		
		window.visor.updateTextDisplay("Error")
		agregator = ""


def pressClear():

	global agregator
	agregator = ""
	window.visor.updateTextDisplay("Clear")



import window