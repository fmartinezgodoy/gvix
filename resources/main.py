from resources.apps.wakeup import Waker
from resources.apps.off import off
from resources.apps.beep import beep
from resources.apps.loader import loader
from resources.apps.recognizer import Recognizer
from resources.apps.speaker import Speaker
from resources.apps.browser import Browser
#from resources.apps.gsearch import Gsearch
from resources.apps.websearch import Wsearch
from resources.apps.launcher import Launcher
from resources.apps.wiki import Wiki
from resources.apps.discord import Discord


class Apps:
	# instancias y parámetros
	def __init__(self):
		self.master = loader()["settings"]["master"]
		self.slave = loader()["settings"]["slave"]

		self.waker = Waker()
		self.recognizer = Recognizer()
		self.speaker = Speaker()
		self.browser = Browser()
		#self.gsearch = Gsearch()
		self.wsearch = Wsearch()
		self.launcher = Launcher()
		self.wiki = Wiki()
		self.discord = Discord()

		self.commands = {
			"abrir": self.browse,
			"buscar": self.search,
			"iniciar": self.launch,
			"wikipedia": self.wikipedia,
			"salir": self.off,
			"discord": self.discord_commands
		}

	def off(self, query):
		off()
	
	def wakeup(self):
		(check, query) = self.waker.wake()
		print(query)
		if check:
			(check, command) = self.waker.checkcat(query, self.commands.keys())
			if check:
				self.commands[command](query)

	# hacer sonido
	def beep(self):
		beep()

	# escucha y devulve una lista de palabras que escuchó
	def hear(self):
		query = self.recognizer.hear()
		return query

	# tts [what]
	def say(self, what):
		self.speaker.say(what)
		
	# abrir en el navegador
	def browse(self, query):
		self.browser.browse(query)

	# buscar en google
	def search(self, query):
		#self.gsearch.searcher(query)
		self.wsearch.search(query)

	# iniciar programa
	def launch(self, query):
		self.launcher.launch(query)

	def wikipedia(self, query):
		self.wiki.wiki()

	# toggles discord
	def discord_commands(self, query):
		self.discord.do(query)
