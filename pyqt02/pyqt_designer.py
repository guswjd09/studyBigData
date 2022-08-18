import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class qTemplate(QWidget):

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui', self) # 디자인은 여기로 다 보내버린당
        self.initUI()

    def initUI(self):
        self.addControls()
        self.show()
        
    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked)
        
    def btn1_clicked(self): # event = signal(in python)
        self.label.setText('btn1 버튼 클릭')
        QMessageBox.information(self, '알림제목', '와 떴당')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()  
    app.exec_() 
