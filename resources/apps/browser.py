import webbrowser
import json

from resources.apps.loader import loader
from resources.apps.recognizer import recognizer
from resources.apps.speaker import speaker
from resources.apps.gsearch import gsearch

class browser():
    def __init__(self):
        # instancias de dependencias
        self.__recognizer = recognizer()
        self.__speaker = speaker()
        self.__gsearch = gsearch()
        self.urls = loader()["urls"]

    # función abrir en el navegador
    def open_url(self, url):
        try:
            webbrowser.open(url)
        except webbrowser.Error:
            self.__speaker.say("Error")

    # función que comprueba si en query hay una palabra 
    # asignada a una url, en caso positivo ejecuta la función
    # abrir en el navegador
    def check_urls(self, query):
        for keys in self.urls.keys():
            if keys in query:
                self.open_url(self.urls[keys])
                self.__speaker.say("Abriendo {}".format(keys))
                return True
        return False

    # función que pregunta qué página se desea abrir
    def ask_browse(self):
        self.__speaker.say("Qué página desea abrir")
        return self.__recognizer.hear()

    def yn_question(self):
        if "sí" in self.__recognizer.hear():
            return True
        else:
            return False

    def browse(self, query):

        # comprueba si se dijo una palabra que este asignada a una url
        # si es afirmativo la url se abre directamente, sino continúa
        # al filtro siguiente
        if self.check_urls(query):
            pass
        #
        else:
            while True:
                # pregunta que página desea abrir,
                # compruebo si en la respuesta se dijeron urls,
                # query ahora es la nueva respuesta
                # como en la comprobación anterior, si se encuentra una url
                # esta se abre directamente
                query = self.ask_browse()
                if self.check_urls(query):
                    break
                else:
                    # si la etapa anterior no funcionó pregunta si debe buscar 
                    # en google los términos escuchados
                    self.__speaker.say("No existe u erre ele asignada a ese término, debería buscarlo en google?")
                    # si la respuesta es si, genero una frase con las palabras
                    # escuchadas en la etapa inmediatamente anterior, 
                    # si es una sola palabra, se genera una frase que
                    # contenga solo esta palabra, esto no afecta a la 
                    # búsqueda en sí
                    if self.yn_question():
                        self.__gsearch.search(self.__gsearch.phraser(query))
                        break
                    # si la respuesta es no, pregunto si desea repetir la 
                    # página a abrir o si desea salir
                    else:
                        self.__speaker.say("Desea repetir la página?")
                        if self.yn_question():
                            pass
                        else:
                            break