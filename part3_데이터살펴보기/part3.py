import pandas as pd
import openpyxl
import lxml
# from bs4 import BeautifulSoup4
import requests
import re
import numpy as np
import seaborn as sns

# print('\n')

# 데이터 살펴보기
# read_csv() 함수로 df 생성
df = pd.read_csv(r'./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns= ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
             'acceleration', 'model year', 'origin', 'name']
# 데이터프레임 df의 내용을 일부 확인
print('처음 5개 행 =>')
print(df.head())
print('\n')
print('마지막 5개 행 =>')
print(df.tail())
print('\n')
print('df의 모양과 크기 확인: (행의 개수, 열의 개수)를 튜플로 반환 =>')
print(df.shape)
print('\n')
print('df의 내용 확인 =>')
print(df.info())
print('\n')
print('df의 내용 확인 =>')
print(df.info())
print('\n')
print('df의 자료형 확인 =>')
print(df.dtypes)
print('\n')
print('df의 시리즈(mog 열)의 자료형 확인 =>')
print(df.mpg.dtypes)
print('\n')
print('df의 기술 통계 정보 확인 =>')
print(df.describe())
print('\n')
print(df.describe(include='all'))
print('\n')



