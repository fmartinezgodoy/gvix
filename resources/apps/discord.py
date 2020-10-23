from fuzzywuzzy import process
from pynput.keyboard import Key, Controller

keyboard = Controller()


class Discord:
	def __init__(self):
		self.__disc_commands = {
			"micro" : "p",
			"auri" : "o"
		}
		# self.keyboard = Controller()

	def ctrl_hotkey(self, key):
		with keyboard.pressed(Key.ctrl):
			keyboard.press(key)
			keyboard.release(key)

	def do(self, query):
		# función que activa el bind ctrl + [key]
		for words in query:
			phrase = ""
			for words in query:		
				phrase += words
				phrase += " "
			category = process.extractOne(phrase, list(self.__disc_commands.keys()))[0]
			self.ctrl_hotkey(self.__disc_commands[category])
