import pandas as pd
import openpyxl
import lxml
# from bs4 import BeautifulSoup4
import requests
import re
import numpy as np
import seaborn as sns
print('\n')
# CSV 파일 읽기
# 파일 경로(파이썬 파일과 같은 폴더)를 찾고, 변수 file_path에 저장
file_path = r'./read_csv_sample.csv'

# read_csv() 함수로 데이터프레임 변환. 변수 df1에 저장
df1 = pd.read_csv(file_path)
print('read_csv() 함수로 데이터프레임 변환. 변수 df1에 저장 =>')
print(df1)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df2에 저장. Header=None 옵션
df2 = pd.read_csv(file_path, header=None)
print('read_csv() 함수로 데이터프레임 변환. 변수 df2에 저장. Header=None 옵션 =>')
print(df2)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print('read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션 =>')
print(df3)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print('read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션 =>')
print(df4)
print('\n')

# Excel 파일 읽기
# read_cexel() 함수로 데이터프레임 변환
# import openpyxl
df5 = pd.read_excel(r'./남북한발전전력량.xlsx', engine='openpyxl')
df6 = pd.read_excel(r'./남북한발전전력량.xlsx', engine='openpyxl', header=None)

# 데이터프레임 출력
print('read_cexel() 함수로 데이터프레임 변환 =>')
print(df5)
print('\n')
print(df6)
print('\n')

# JSON 파일 읽기
# read_json() 함수로 데이터프레임 변환
df7 = pd.read_json(r'./read_json_sample.json')
print('read_json() 함수로 데이터프레임 변환 =>')
print(df7)
print('\n')
print(df7.index)
print('\n')

# 웹에서 표 정보 읽기
# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url = r'./sample.html'
# HTML 웹페이지의 표(TABLE)를 가져와서 데이터프레임으로 변환
# import lxml
tables = pd.read_html(url)
# 표(table)의 개수 확인
print('HTML 웹페이지의 표(TABLE) 개수 확인 =>')
print(len(tables))
print('\n')

# tables 리스트의 원소를 iteration하면서 각가 화면 출력
print('tables 리스트의 원소를 iteration하면서 각가 화면 출력 for문 =>')
for i in range(len(tables)) :
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

# 파이썬 패키지 정보가 들어있는 두 번째 데이터프레임을 선택하여 df 변수에 저장
df8 = tables[1]
# 'name' 열을 인덱스로 지정
df8.set_index(['name'], inplace=True)
print('name 열을 인덱스로 지정 =>')
print(df8)

# 미국 ETF 리스트 가져오기
# 위키피디아 미국 ETF 우베 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
# url_wikiETF = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
# resp = requests.get(url_wikiETF)
# soup = BeautifulSoup4(resp.text, 'lxml')
# rows = soup.select('div > ul > li')
#
# etfs = {}
# for row in rows :
#     try:
#         etf_name = re.findall('^(.*) \(NYSE', row.text)
#         etf_market = re.findall('|((.*)\|)', row.text)
#         etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
#
#         if(len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0) :
#             etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
#
#     except AttributeError as err:
#         pass
#
# # etfs 딕셔너리 출력
# print('etfs 딕셔너리 출력 =>')
# print(etfs)
# print('\n')