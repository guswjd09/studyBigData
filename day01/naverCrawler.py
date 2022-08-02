import os
import sys
import urllib.request
import urllib.parse
import datetime
import time
import json


# 네이버 개발자 내 애플리케이션에서 찾아서 입력
client_id = 'oTbl6ja6lMQVC6D2_Vny'
client_secret = 'sSbX72oEWq'


# url 접속 요청 후 응답 return 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    # 예외 처리
    # 네트워크가 끊기거나 정보가 돌아오지 않을 경우를 대비해서 사용
    try:
        res = urllib.request.urlopen(req) 
                        # 200은 OK/ 400대는 error/ 500대는 server error 
        if res.getcode() == 200:  
            print(f'[{datetime.datetime.now()}] Url Request success')
            return res.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None

# 핵심 함수, 네이버 API 검색
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'

    # url주소에 한글이 포함된 경우 깨질수있는데 그걸 방지해줌
    # url주소에 맞춰서 파싱
    text = urllib.parse.quote(srcText)
    params = f'?query={text}&start={start}&display={display}'

    url = base + node + params
    resDecode = getRequestUrl(url)

    if resDecode == None:
        return None
    else:
        return json.loads(resDecode) # Json형태로 정보를 가져옴

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']

    pubDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:%S') # 2022-08-02 15:56:34

    jsonResult.append({'cnt':cnt,'title':title, 'description':description,
                        'originallink':originallink, 'link':link, 'pubDate':pubDate})

# 실행최초함수
def main():
    node = 'news' # p133 
    srcText = input('검색어를 입력하세요: ')
    cnt = 0
    jsonResult = [] # list로 받을껀데 지금 현재는 비어있음

    jsonRes = getNaverSearch(node, srcText, 1, 50)
    # print(jsonRes)

    total = jsonRes['total'] # 검색된 뉴스 개수

    while ((jsonRes != None) and (jsonRes['display'] != 0)):
        for post in jsonRes['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        # 처음에는 1-50까지 나오고 그 다음은 51- 다음페이지에 나옴
        start = jsonRes['start'] + jsonRes['display'] 
        jsonRes = getNaverSearch(node, srcText, start, 50)

    print(f'전체 검색 : {total}건')

    # file output
    # ./ -> 내위치, indent : 들여쓰기
    with open(f'./{srcText}_naver_{node}.json', mode='w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
    
    print(f'가져온 데이터 : {cnt} 건')
    print(f'{srcText}_naver_{node}.json SAVED')

# 스페셜 변수
if __name__ == '__main__':
    main()