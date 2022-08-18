import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class qTemplate(QWidget):

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/ttask.ui', self) # 디자인은 여기로 다 보내버린당
        self.initUI()

    def initUI(self):
        self.addControls()
        self.show()
        
    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self): # event = signal(in python)
        self.txbLog.append('실행')
        self.pgbTask.setRange(0, 10000)
        for i in range(10001):
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()  
    app.exec_() 
