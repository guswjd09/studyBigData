import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# class OOP
class qTemplate(QWidget):
    
    # 생성자
    def __init__(self) -> None:
        # class에 들어가는 함수는 무조건 내가 누군지 지칭해야함 그게 self임
        # '-> None' : class 생성자는 return이 없음(생략가능), '->str' : return str(문자)
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 400)
        self.setWindowTitle('QPushbutton')
        self.show()
    
    def addControls(self) -> None:
        btn1 = QPushButton('Click', self)
				# btn1.setGeometry(510, 350, 120, 40)
        btn1.setGeometry(510, 350, 120, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()