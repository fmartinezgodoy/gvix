import webbrowser

from resources.apps.loader import loader
from resources.apps.speaker import Speaker
from resources.apps.recognizer import Recognizer


class Gsearch:

	def __init__(self):
		self.__slave = loader()["settings"]["slave"]
		self.__speaker = Speaker()
		self.__recognizer = Recognizer()

	# buqueda de [this] en google
	def search(self, this):
		webbrowser.open("https://www.google.com/search?q={}".format(this))

	# genera una frase o palabra a partir de un array
	def phraser(self, query):
		try:
			phrase = ""
			if len(query) > 1:
				for words in query:
					phrase = "{} {}".format(phrase, words)
				return phrase
			else:
				return query[0]
		except:
			return ""

	# limpia el query de palabras como slave y google
	def cleaner(self, query):
		for words in [self.__slave,
			"google",
			"buscar",
			"en"
			]:
			while words in query:
				query.remove(words)

	# funcion principal de busqueda
	def searcher(self, query):
		# ejecuta el cleaner para filtrar el query
		self.cleaner(query)

		# si quedan palabras en query busca
		# el resultado de phraser, ya sea una 
		# palabra o una frase completa
		if len(query) > 0:
			self.search(self.phraser(query))
		# si el query quedo vacío entonces pregunta
		# que se desa buscar en google
		else:
			self.__speaker.say("Qué deseas buscar en google?")
			# pasa la respuesta de hear por phrase y por search
			self.search(self.phraser(self.__recognizer.hear()))
