import speech_recognition as sr

recognizeSpeech = sr.Recognizer()

def talk():
    with sr.Microphone() as source:
        audio = recognizeSpeech.listen(source)
        user = recognizeSpeech.recognize_wit(audio,key='VSDKI2TOPBRIMVEWOCPGE32MMUWESQML')
        print(user)
    return user
