from resources.main import apps

gvix = apps()
gvix.say("Bienvenido {}, soy {}, su asistente virtual".format(gvix.master, gvix.slave))

while True:
	print("..")

	gvix.wakeup()