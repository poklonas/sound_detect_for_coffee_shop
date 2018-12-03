
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ThreadSignals(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(object)

class Thread(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Thread, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = ThreadSignals()

    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            pass
        finally:
            self.signals.finished.emit()  # Done