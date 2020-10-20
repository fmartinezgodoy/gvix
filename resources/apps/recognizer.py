import speech_recognition

class recognizer(object):

    def __init__(self):
        # instancias para micrófono y reconocedor
        self.__mic = speech_recognition.Microphone()
        self.__recognizer = speech_recognition.Recognizer()
        self.__recognizer.energy_threshold = 400 
        self.__recognizer.dynamic_energy_threshold = False
        self.__recognizer.pause_threshold = 3

    def hear(self):
        with self.__mic as source:
            try:
                audio = self.__recognizer.listen(source, timeout = 3)
            except:
                audio = None
        try:
            audio2text = str(self.__recognizer.recognize_google(audio, language="es-ES")).lower()
            print(audio2text)
            return audio2text.split()
        
        except:
            return []