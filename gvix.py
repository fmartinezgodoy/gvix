from resources.main import Apps

gvix = Apps()
gvix.say("Bienvenido {}, soy {}, su asistente virtual".format(gvix.master, gvix.slave))

while True:
	print("..")
	gvix.wakeup()
