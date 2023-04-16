import speech_recognition as sr
import pyttsx3
import pygame

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')

with sr.Microphone() as source:
    engine.say('¿En que puedo ayudarte?')
    engine.runAndWait()
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=5)
try:
    texto = r.recognize_google(audio, language='es')
    engine.save_to_file(texto, 'sayed.wav')
    engine.runAndWait()
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sayed.wav')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.quit()

except sr.UnknownValueError:
    print('no se entendio lo que dijiste')
except sr.RequestError as e:
    print(
        f"No se ha podido obtener una respuesta del servicio de reconocimiento de voz: {e}")
