import pyttsx3


class Speaker:
	# instancia y parámetros encapsulados para tts
	def __init__(self):
		self.__tts = pyttsx3.init()
		self.__tts.setProperty("rate", 130)
		self.__tts.setProperty("volume", 1.0)

	def say(self, what):
		self.__tts.say(what)
		self.__tts.runAndWait()
