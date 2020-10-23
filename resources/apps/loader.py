import json
import os


def loader():
	with open(os.getcwd() + "\\settings\\data.json") as content:
		data = json.load(content)
	return data
