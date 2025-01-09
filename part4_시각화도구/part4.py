import pandas as pd
import openpyxl
import lxml
# from bs4 import BeautifulSoup4
import requests
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = r'./malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 윈도우 경우
rc('font', family=font_name)
# mac 경우
# rc('font', family=AppleGothic)

# print('\n')

# 250107
# 선 그래프
# Excel 데이터를 데이터프레임으로 변환
print('Excel 데이터를 데이터프레임으로 변환 =>')
df = pd.read_excel('시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)
print('\n')

# 누락값(NaN)을 앞 데이터로 채움(엑셀 양식 병합 부분)
# df = df.fillna(method='ffill')
df = df.ffill()

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
print('서울에서 다른 지역으로 이동한 데이터만 추출하여 정리 =>')
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print('\n')

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
print('서울에서 경기도로 이동한 인구 데이터 값만 선택 =>')
sr_one = df_seoul.loc['경기도']
print('\n')

# 스타일 서식 지정
print('스타일 서식 지정 =>')
print('스타일 종류 : classic, bmh, dark_background, fast, grayscale, seaborn 등')
print('250107기준 더 많은 스타일 정보 : https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html')
# 스타일 리스트 출력
print('스타일 리스트 출력 =>')
print(plt.style.available)
plt.style.use('ggplot')

# 그림 사이즈 지정(가로 14인치, 세로 5인치
print('그림 사이즈 지정(가로 14인치, 세로 5인치 =>')
plt.figure(figsize=(14, 5))
# x축 눈금 라벨 회전하기
print('x축 눈금 라벨 회전하기 =>')
plt.xticks(rotation='vertical')
print('\n')

# x축, y축 데이터를 plot 함수에 입력
print('x축, y축 데이터를 plot 함수에 입력 + 마커표시 추가 =>')
print('marker 마커 모양 : o 또는 + 또는 * 또는 . 등 이 있음  ')
print('마커 배경색 => markerfacecolor="green"')
print('마커 크기 => markersize=10')
print('선의 색 => color="olive"')
print('선의 두께 => linewidth=2')
print('라벨 지정 => label="서울 -> 경기"')
# plt.plot(sr_one.index, sr_one.vals)
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)
print('\n')

# 차트 제목 추가
print('차트 제목 추가 + 제목이름 크기 추가 =>')
plt.title('서울 -> 경기 인구 이동', size=30)
print('\n')

# 축 이름 추가
print('x축, y축 이름 추가 + 제목이름 크기 추가 =>')
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)
print('\n')

# 범례 표시
print('범례 표시 + 크기 추가 =>')
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)

plt.show()
print('\n')

# 스타일 리스트 출력
print(plt.style.available)
