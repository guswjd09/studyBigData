from cmath import rect
import json
import sys
from urllib.parse import quote
import urllib.request
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import webbrowser

class qTemplate(QWidget):

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/navermovie.ui', self) 
        self.initUI()

    def initUI(self):
        self.addControls()
        self.show()
        
    def addControls(self) -> None:  # 위젯 정의, 이벤트(=시그널) 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)
        
    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 2).text()
        webbrowser.open(link)

    def btnSearchClicked(self) -> None:  # 슬롯(이벤트 핸들러)
        jsonResult = []
        totalResult = []
        keyword = 'movie'
        search_word = self.txtSearch.text()
        display_count = 50

        # QMessageBox.information(self,'결과',search_word)
        jsonResult = self.getNaverSearch(keyword, search_word, 1, display_count)
        # print(jsonResult)
        
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))
        
        self.makeTable(totalResult)
                   
        return  # (return 값에 아무것도 안넣으면 return none과 같음)

                          
    def makeTable(self, result):        
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(3)
        self.tblResult.setRowCount(len(result))
        self.tblResult.setHorizontalHeaderLabels(['영화제목','상영년도','뉴스링크'])
        self.tblResult.setColumnWidth(0, 250) # 0번째
        self.tblResult.setColumnWidth(1, 100) # 1번째
        self.tblResult.setColumnWidth(2, 100) # 2번째
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # readonly
        
        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            subtitle = self.strip_tag(item[0]['subtitle'])
            pubDate = item[0]['pubDate']
            link = item[0]['link']
            self.tblResult.setItem(i, 0, QTableWidgetItem(f'{title} / {subtitle}'))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(link))
            i += 1

    def strip_tag(self, title):
        ret = title.replace('&lt;', '<')
        ret = ret.replace('&rt;', '>')
        ret = ret.replace('&quot;', '"')
        ret = ret.replace('&apos;', "'")
        ret = ret.replace('&amp;', '&')
        ret = ret.replace('<b>', '')
        ret = ret.replace('</b>', '')

        return ret
    
    def getPostData(self, post):
        temp = []
        title = post['title']
        subtitle = post['subtitle']
        link = post['link']
        pubDate = post['pubDate']
        
        temp.append({'title': title, 'subtitle': subtitle, 'pubDate':pubDate, 'link': link})
        
        return temp
        
        
    # 네이버 API 크롤링 함수
    def getNaverSearch(self, keyword, search, start, display):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json' \
              f'?query={quote(search)}&start={start}&display={display}'
        print(url)
        req = urllib.request.Request(url)

        # 네이버 인증 추가
        req.add_header('X-Naver-Client-Id', 'OJJDKJIS2WTSrYwSwd1y')
        req.add_header('X-Naver-Client-Secret', 'nu1hjpck0k')

        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print('URL Request Succeess')
        else:
            print('URL Request Failed')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
