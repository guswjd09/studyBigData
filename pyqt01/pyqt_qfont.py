import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# class OOP
class qTemplate(QWidget):
    
    # 생성자
    def __init__(self) -> None:
        # class에 들어가는 함수는 무조건 내가 누군지 지칭해야함 그게 self임
        # '-> None' : class 생성자는 return이 없음(생략가능), '->str' : return str(문자)
        super().__init__()
        self.initUI()

    # 화면 정의를 위해 사용자 함수
    def initUI(self) -> None:
                        # x, y, 너비, 높이
        self.setGeometry(300, 200, 640, 400)
        self.setWindowTitle('QTemplate!!')
        self.text = 'What a wonderful world ~'
        self.show()

    # 그리는 이벤트에 대한 내장함수(QWidget에 속해있음)
    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()  

    # 텍스트를 그리기 위한 사용자 함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50, 50, 50))
        paint.setFont(QFont('NanumGothic',20))
        paint.drawText(105, 100, 'HELL WORLD~')
        paint.setPen(QColor(0, 250, 10))
        paint.setFont(QFont('Impact',15))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()