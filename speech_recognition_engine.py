import speech_recognition as sr

r = sr.Recognizer()

def get_user_command():
  with sr.Microphone() as source:
    while True:
      try:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text
      except sr.UnknownValueError:
        print "Unrecognized speech"
