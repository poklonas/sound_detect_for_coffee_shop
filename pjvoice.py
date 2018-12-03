import speech_recognition as sr
#import threading
from pythainlp.tokenize import word_tokenize

#from text2list import CoffeeShopNLP
from thread import * 

class Recogning:
    def __init__(self):
        self.r = sr.Recognizer()
        self.on = False
        self.list = []
        self.threadpool = QThreadPool()

    def reconizing(self,audio):
        print("create thread reconizing")
        try:
            text = self.r.recognize_google(audio,language = "th-TH")
            print(text)
            self.list.append(text)
        except:
            pass

    def listen(self):
        with sr.Microphone() as source: self.r.adjust_for_ambient_noise(source)
        while self.on:
            with sr.Microphone() as source:
                print("listening")
                audio = self.r.listen(source) 
            thread = Thread(self.reconizing, audio)
            self.threadpool.start(thread)
            #t = threading.Thread(target=self.reconizing, args=(audio,))
            #t.start()
        print("exit thread reconizing")
        return self.list

if __name__ == '__main__':
    nlp  = CoffeeShopNLP()
    r = sr.Recognizer()
    listener = Recogning()
    listener.on = True
    listener.listen()
    #t = threading.Thread(target=listen)
    #t.start()
