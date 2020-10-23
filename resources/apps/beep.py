import os
import winsound


def beep():
	winsound.PlaySound(os.getcwd() + "\\resources\\sounds\\CLICK7C.wav", winsound.SND_FILENAME)
