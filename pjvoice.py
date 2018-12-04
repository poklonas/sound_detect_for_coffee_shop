import speech_recognition as sr
#import threading
from pythainlp.tokenize import word_tokenize

from PyQt5.QtGui import QStandardItemModel #user to add order list

#from text2list import CoffeeShopNLP
from thread import *  #use for use pyqtgread

class Recogning:
    def __init__(self):
        self.r = sr.Recognizer()
        self.on = False
        self.list = []
        self.threadpool = QThreadPool()
        self.order_list = None
        self.order_model = QStandardItemModel()

    def reconizing(self,audio):
        #print("create thread reconizing")
        text = self.r.recognize_google(audio,language = "th-TH")
        #print("exit thread reconizing")
        self.addList2Target(text)
        #return text

    def listen(self, target):
        self.order_list = target
        with sr.Microphone() as source: self.r.adjust_for_ambient_noise(source)
        while self.on:
            with sr.Microphone() as source:
                print("listening")
                audio = self.r.listen(source) 
                print("listening complete")
            thread = Thread(self.reconizing, audio)
            #thread.signals.result.connect(self.addList2Target)
            self.threadpool.start(thread)
            #t = threading.Thread(target=self.reconizing, args=(audio,))
            #t.start()
        print("stop all listening")
        return self.list

    def addList2Target(self, text):
        self.list.append(text)
        self.order_model.appendRow(QStandardItem(text))
        self.order_list.setModel(self.order_model)

if __name__ == '__main__':
    nlp  = CoffeeShopNLP()
    r = sr.Recognizer()
    listener = Recogning()
    listener.on = True
    listener.listen()
    #t = threading.Thread(target=listen)
    #t.start()
