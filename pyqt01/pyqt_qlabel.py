import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# class OOP
class qTemplate(QWidget):
    
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    # 화면 정의를 위해 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 640, 400)
        self.setWindowTitle('QLabel')
        self.show()

    def addControls(self) -> None:
        # window 아이콘 지정
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png'))
        label1= QLabel('Label1', self)
        label2= QLabel('Label2', self)

        label1.setStyleSheet(
            ('border-width: 3px;'
             'border-style: solid;'
             'border-color: blue;'
             # 상대경로 안됨, python 절대경로 사용
             'image: url(./pyqt01/image/image1.png)')
        )

        label2.setStyleSheet(
            ('border-width: 3px;'
             'border-style: dot-dot-dash;'
             'border-color: red;'
             # 상대경로 안됨, python 절대경로 사용
             'image: url(./pyqt01/image/image2.png)')
        )

        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()