from resources.apps.speaker import speaker
from resources.apps.recognizer import Recognizer

speaker = speaker()
recognizer = Recognizer()


def off():
	query = recognizer.hear()
	if "sí" in query:
		exit()
