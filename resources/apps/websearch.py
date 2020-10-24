import webbrowser
from fuzzywuzzy import process

from resources.apps.loader import loader
from resources.apps.speaker import Speaker
from resources.apps.recognizer import Recognizer


class Wsearch:
    def __init__(self):
        self.searchers = loader()["searchs"]
        self.speaker = Speaker()
        self.recognizer = Recognizer()

        self.cleanlist = [
            "buscar",
            "en"
        ]

    def phraser(self, query):
        phrase = ""
        for words in query:
            phrase += words + " "
        return phrase

    def cleaner(self, query):
        for words in query:
            (word, ratio) = process.extractOne(words, self.cleanlist)
            if ratio > 75:
                query.remove(words)
                return query
        return query

    def search(self, query):
        for words in query:
            if words in list(self.searchers.keys()):
                query = query[query.index(words)+1:]
                print(words)
                # query.remove(words)
                query = self.cleaner(query)
                webbrowser.open(self.searchers[words] + self.phraser(query))
