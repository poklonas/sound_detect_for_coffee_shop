import speech_recognition as sr
from pythainlp.tokenize import word_tokenize
from PyQt5.QtGui import QStandardItemModel
from .text2list import *
from .logging import logging
from thread import *

import time

class Recogning:
    def __init__(self):
        self.r = sr.Recognizer()
        self.on = False
        self.status = False
        self.list = []
        self.threadpool = QThreadPool()
        self.fc_update = None
        self.order_model = QStandardItemModel()
        self.dic = CoffeeShopNLP()

    def reconizing(self,audio):
        start_time = time.time()
        text = self.r.recognize_google(audio,language = "th-TH")
        logging.debug("recognize %s (%.2f s)",text,time.time()-start_time)
        start_time = time.time()
        order = self.dic.text_to_item(text)
        logging.debug("order %s complete (%.2f s)",str(order),time.time()-start_time)
        return order
    
    def setupmic(self):
        with sr.Microphone() as source: self.r.adjust_for_ambient_noise(source)

    def listen(self, fc_update):
        self.fc_update = fc_update
        self.order_model = QStandardItemModel()
        while self.on:
            self.status = True
            start_time = time.time()
            with sr.Microphone() as source:
                logging.info("listening")
                # audio = self.r.listen(source,phrase_time_limit=10)
                audio = self.r.listen(source)
                logging.info("listening complete (%.2f s)",time.time()-start_time)
            thread = Thread(self.reconizing, audio)
            thread.signals.result.connect(self.fc_update)
            self.threadpool.start(thread)
        logging.info("stop all listening")
        self.status = False
        return None

if __name__ == '__main__':
    nlp  = CoffeeShopNLP()
    r = sr.Recognizer()
    listener = Recogning()
    listener.on = True
    listener.listen()
