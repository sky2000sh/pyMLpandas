# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# embark_town 열의 829행의 NaN 데이터 출력
print('embark_town 열의 829행의 NaN 데이터 출력')
print(df['embark_town'][825:830])
print('\n')

# embark_town 열의 NaN값을 바로 앞에 있는 828행의 값으로 변경하기
df['embark_town'].fillna(method='ffill', inplace=True)
print('이웃하고 있는 값으로 바꾸기')
print(df['embark_town'][825:830])