import window


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
		total = str(eval(agregator))
		result = total

	except:
		pass



