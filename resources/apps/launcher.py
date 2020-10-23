import os
from resources.apps.loader import loader


class Launcher:
	def __init__(self):
		self.__programs = loader()["programs"]

	def launch(self, query):
		# inicia el .exe de la ruta en el diccionario
		for word in query:
			if word in self.__programs.keys():
				try: 
					os.startfile(self.__programs[word])
				except:
					pass
