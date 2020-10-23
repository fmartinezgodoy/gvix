import wikipedia

from resources.apps.speaker import Speaker
from resources.apps.recognizer import Recognizer
from resources.apps.browser import Browser

wikipedia.set_lang("es")


class Wiki:
    def __init__(self):
        self.speaker = Speaker()
        self.recognizer = Recognizer()
        self.browser = Browser()

    # función que ejecuta la busqueda en sí
    def wikisearch(self, what):
        search = wikipedia.page(what)
        print("Esto es lo que encontré en wikipedia sobre {}, {}".format(search.title, search.summary))
        # self.speaker.say("Esto es lo que encontré en wikipedia sobre {}, {}".format(search.title, search.summary))
        self.speaker.say("Desea que abra la página en el navegador?, señor")
        if self.browser.yn_question():
            self.browser.open_url(search.url)
            self.speaker.say("Abriendo wikipedia")
        else:
            self.speaker.say("Finalizando wikisearch")

    # genera una frase o palabra a partir de un array
    def phraser(self, query):
        phrase = ""
        if len(query) > 1:
            for words in query:
                phrase = "{} {}".format(phrase, words)
            return phrase
        else:
            return query[0]

    # genera una frase o palabra a partir de un array
    def phraser(self, query):
        phrase = ""
        if len(query) > 1:
            for words in query:
                phrase = "{} {}".format(phrase, words)
            return phrase
        else:
            return query[0]

    def yn_question(self):
        if "sí" in self.__recognizer.hear():
            return True
        else:
            return False

    def wiki(self):
        self.speaker.say("Que desea buscar en wikipedia?")
        # paso la respuesta por phraser y despues la envío a wikisearch
        try: 
            self.wikisearch(self.phraser(self.recognizer.hear()))

        except wikipedia.exceptions.PageError:
            self.speaker.say("Ese término no corresponde a una página de wikipedia.")