import speech_recognition as sr
from pythainlp.tokenize import word_tokenize
from PyQt5.QtGui import QStandardItemModel
from other_module.text2list import *
from thread import * 

class Recogning:
    def __init__(self):
        self.r = sr.Recognizer()
        self.on = False
        self.list = []
        self.threadpool = QThreadPool()
        self.fc_update = None
        self.order_model = QStandardItemModel()
        self.dic = CoffeeShopNLP()

    def reconizing(self,audio):
        text = self.r.recognize_google(audio,language = "th-TH")
        #self.list.append(text)
        order = self.dic.text_to_item(text)
        for i in order:
            self.list.append(i[0])
            print(i)
        return order

    def listen(self, fc_update):
        self.fc_update = fc_update
        self.order_model = QStandardItemModel()
        with sr.Microphone() as source: self.r.adjust_for_ambient_noise(source)
        while self.on:
            with sr.Microphone() as source:
                print("listening")
                audio = self.r.listen(source) 
                print("listening complete")
            thread = Thread(self.reconizing, audio)
            thread.signals.result.connect(self.fc_update)
            self.threadpool.start(thread)
        print("stop all listening")
        return self.list


if __name__ == '__main__':
    nlp  = CoffeeShopNLP()
    r = sr.Recognizer()
    listener = Recogning()
    listener.on = True
    listener.listen()
