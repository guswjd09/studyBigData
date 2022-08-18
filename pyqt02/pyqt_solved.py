import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

# UI thread와 작업 thread를 분리!
class Worker(QThread): # background worker를 의미
    valChangeSignal = pyqtSignal(int) 
    # 대신 서로 통신하게 하여 권한을 위임하는 것이당~
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.working = True # Class 내부 변수 working을 만들어서 값을 지정

    def run(self):
        while(self.working):
            for i in range(10001): # 이거는 10000까지 실행하고 
                print(f'출력 : {i}')
                # self.pgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}') 
                # pgbTask와 txbLog는 ui쪽이라 QThread인 Worker가 작업 권한이 없다고 한다. 그래서 연결해 줘야 함!
                self.valChangeSignal.emit(i)
                time.sleep(0.0001)
            
        
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
        # Worker 클래스 생성, 동작
        self.worker = Worker(self)  
        self.worker.valChangeSignal.connect(self.updateProgress) # 받은 시그널을 updateProgress 함수로 처리하도록 이어준다.
    
    @pyqtSlot(int) 
    def updateProgress(self, val): #val이 Worker스레드에서 전달받은 for문의 i(int)값이다. 
        self.pgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 10000:
            self.worker.working =False
             
        
    def btn_clicked(self): # event = signal(in python)
        self.txbLog.append('실행')
        self.pgbTask.setRange(0, 10000) # progress bar가 10000까지 있어서 스레드 작업 run할 때 10000까지 실행(range 10001)해주면 100%까지 뜬다 ㅋㅋㅋ
        self.worker.start()
        self.worker.working = True
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()  
    app.exec_() 
