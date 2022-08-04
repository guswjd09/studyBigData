# 할리스 커피숍 매장정보 크롤링

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def getHollysStoreInfo(result):
    for page in range(1,54):
        hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        # print(hollys_url)
        html = urllib.request.urlopen(hollys_url)
        soup = BeautifulSoup(html, 'html.parser') # html을 html.parser로 파싱하라
        # thead : 테이블 index / tbody : 테이블의 내용
        tbody = soup.find('tbody')

        for store in tbody.find_all('tr'): # tr 찾기
            if len(store) < 3:
                break
            
            store_td = store.find_all('td') # td 찾기

            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            
            result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    # result
    print('완료!!') # 완료!! 가 뜨면 끝났다는 것!

def main():
    result = [] # 리스트 형태로 값을 받음
    print('할리스 매장 크롤링 >>> ')
    # 크롤링 함수
    getHollysStoreInfo(result)

    # 판다스 데이터프레임 생성
    columns = ['store', 'sido-gu', 'address', 'phone']
    hollys_df = pd.DataFrame(result, columns=columns)

    # csv 저장
    hollys_df.to_csv('C:/localRepository/studyBigData/day03/hollys_shop_info2.csv', index=True, encoding='utf-8')
    # hollys_df.to_csv('./hollys_shop_info.csv', index=True, encoding='utf-8')

    # 디버깅을 하지않을꺼면 글자를 출력해주기
    print('저장완료')

    del result[:]


if __name__ == '__main__':
    main()



