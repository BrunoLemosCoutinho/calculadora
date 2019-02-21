
class Calculadora:

	agregator = ""
	result = "bbmp"

	# Function to update agregator variable
	# and display text

	@classmethod
	def pressNumber(cls, num):

		Calculadora.agregator = Calculadora.agregator + str(num)
		Calculadora.result = Calculadora.agregator


		print(num)

	@classmethod
	def pressEqual(cls):

		try:
			total = str(eval(Calculadora.agregator))
			Calculadora.result = total

		except:
			pass



