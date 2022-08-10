import sys
from PyQt5.QtWidgets import QApplication, QWidget

# class OOP
class qTemplate(QWidget):
    
    # 생성자
    def __init__(self) -> None:
        # class에 들어가는 함수는 무조건 내가 누군지 지칭해야함 그게 self임
        # '-> None' : class 생성자는 return이 없음(생략가능), '->str' : return str(문자)
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
                        # x, y, 너비, 높이
        self.setGeometry(300, 200, 500, 200)
        self.setWindowTitle('QTemplate!!')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()