import speech_recognition as sr
import threading
from pythainlp.tokenize import word_tokenize

from text2list import CoffeeShopNLP

def reconizing(audio):
    try:
        text = r.recognize_google(audio,language = "th-TH")
        print(text)
        item = nlp.text_to_item(text)
        print(item)
    except:
        pass

def listen():
    with sr.Microphone() as source: r.adjust_for_ambient_noise(source)
    while True:
        with sr.Microphone() as source:
            print("listening")
            audio = r.listen(source)
        t = threading.Thread(target=reconizing, args=(audio,))
        t.start()

if __name__ == '__main__':
    nlp  = CoffeeShopNLP()
    r = sr.Recognizer()
    listen()
    #t = threading.Thread(target=listen)
    #t.start()
