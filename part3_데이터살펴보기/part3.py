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
print('df의 데이터 개수 확인 =>')
print(df.count())
print('\n')
print('df.count()가 반환하는 객체 타입 출력 =>')
print(type(df.count()))
print('\n')
print('데이터프레임 df의 특정 열이 가지고 있는 고유값 확인 =>')
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')
print('value_counts 함수가 반환하는 객체 타입 출력 =>')
print(type(unique_values))
print('\n')

# 통계 함수
# 평균값
print('통계 함수 평균값 =>')
print(df.mean)
print('\n')
print(df['mpg'].mean)
print(df.mpg.mean)
print('\n')
print(df[['mpg', 'weight']].mean)
print('\n')

# 중간값
print('통계 함수 중간값 =>')
print(df.median)
print('\n')
print(df['mpg'].median)
print('\n')

# 최대값
print('통계 함수 최대값 =>')
print(df.max)
print('\n')
print(df['mpg'].max)
print('\n')

# 최소값
print('통계 함수 최소값 =>')
print(df.min)
print('\n')
print(df['mpg'].min)
print('\n')

# 표준편차
print('통계 함수 표준편차 =>')
print(df.std)
print('\n')
print(df['mpg'].std)
print('\n')

# 상관계수
print('통계 함수 상관계수 =>')
print(df.corr)
print('\n')
print(df[['mpg', 'weight']].corr)
print('\n')


# 선 그래프 그리기
print('선 그래프를 위한 데이터프레임 변환 =>')
df1 = pd.read_excel(r'./남북한발전전력량.xlsx', engine='openpyxl')
df_ns = df1.iloc[[0, 5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head)
print('\n')
print('선 그래프 그리기 =>')
df_ns.plot()

# 행, 열 전치하여 다시 그리기
print('행, 열 전치하여 다시 그리기 =>')
tdf_ns = df_ns.T
print(tdf_ns.head)
print('\n')
tdf_ns.plot()

# 막대 그래프
print('행, 열 전치하여 막대 그래프 그리기 =>')
tdf_ns.plot(kind='bar')