from fuzzywuzzy import process
from resources.apps.off import off
from resources.apps.beep import beep
from resources.apps.loader import loader
from resources.apps.recognizer import recognizer
from resources.apps.speaker import speaker
from resources.apps.browser import browser
from resources.apps.gsearch import gsearch
from resources.apps.launcher import launcher
from resources.apps.wiki import wiki
from resources.apps.discord import discord

class apps():
	# instancias y parámetros
	def __init__(self):
		self.master = loader()["settings"]["master"]
		self.slave = loader()["settings"]["slave"]

		self.recognizer = recognizer()
		self.speaker = speaker()
		self.browser = browser()
		self.gsearch = gsearch()
		self.launcher = launcher()
		self.wiki = wiki()
		self.discord = discord()

		self.commands = {
			"abrir" : self.browse,
			"buscar en google" : self.search,
			"iniciar" : self.launch,
			"wikipedia" : self.wikipedia,
			"salir" : self.off,
			"discord" : self.discord_commands
		}

	def off(self, query):
		off.off()

	# hacer sonido
	def beep(self):
		beep()

	# escucha y devulve una lista de palabras que escuchó
	def hear(self):
		query = self.recognizer.hear()
		return query

	def categorize(self, query):
		phrase = ""
		for words in query:		
			phrase += words
			phrase += " "
		category = process.extractOne(phrase, list(self.commands.keys()))
		return category[0]

	# tts [what]
	def say(self, what):
		self.speaker.say(what)



	# abrir en el navegador
	def browse(self, query):
		self.browser.browse(query)

	# buscar en google
	def search(self, query):
		self.gsearch.searcher(query)

	# iniciar programa
	def launch(self, query):
		self.launcher.launch(query)

	def wikipedia(self, query):
		self.wiki.wiki()

	# toggles discord
	def discord_commands(self, query):
		self.discord.do(query)