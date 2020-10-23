import speech_recognition
from fuzzywuzzy import process, fuzz

from resources.apps.loader import loader


class Waker:
    def __init__(self):
        # instancias de speech recognition
        self.mic = speech_recognition.Microphone()
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.energy_threshold = 400 
        self.recognizer.dynamic_energy_threshold = False
        self.recognizer.pause_threshold = 0.8
        self.slave = loader()["settings"]["slave"]

    def checkforslave(self, query):
        for words in query:
            if fuzz.ratio(self.slave, words) > 70:
                query.remove(words)
                return [True, query]
        return [False]

    def checkcat(self, query, commands):
        phrase = ""
        for words in query:
            phrase += words + " "
        cat = process.extractOne(phrase, commands)
        if cat[1] > 60:
            return [True, cat[0]]
        else:
            return [False]

    def wake(self):
        # escucha e interpreta lo que escuchó
        with self.mic as source:
            try:
                audio = self.recognizer.listen(source, timeout=1)
            except:
                audio = None
        try:
            audio2text = str(self.recognizer.recognize_google(audio, language="es_ES")).lower()
            return self.checkforslave(audio2text.split())

        except:
            return [False]
