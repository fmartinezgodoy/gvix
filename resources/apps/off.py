from resources.apps.speaker import Speaker
from resources.apps.recognizer import Recognizer

speaker = Speaker()
recognizer = Recognizer()


def off():
	query = recognizer.hear()
	if "sí" in query:
		exit()
