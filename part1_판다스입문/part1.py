import pandas as pd
import numpy as np
import seaborn as sns

# === changing from dictionary to series ===
# key-value 쌍으로 딕셔너리를 만들고, 변수 dic_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# pandas Series() 함수로 dictionary를 Series로 변환. 변수 sr에 저장
sr1 = pd.Series(dict_data)

# type()함수 : sr의 자료형 출력
print(type(sr1))
print('\n')
# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr1)
print('\n')


# === series index ===
# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2024-12-01', 3.14, 'ABC', 100, True]
sr2 = pd.Series(list_data)
print(sr2)

# 인덱스 배열은 변수  idx에 저장. 데이터 값 배열은 변수 val에 저장
idx1 = sr2.index
val1 = sr2.values
print(idx1)
print('\n')
print(val1)
print('\n')


# === series element ===
# 튜플을 시리즈로 변환(인덱스 옵션 지정)
tup_data = ('영인', '2024-11-01', '여', True)
sr3 = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr3)

# 원소를 1개 선택
print('원소를 1개 선택')
# print(sr3[0])
print(sr3['이름'])
print('\n')

# 여러 개의 원소를 선택(인덱스 리스트 활용)
print('여러 개의 원소를 선택(인덱스 리스트 활용)')
# print(sr3[[1, 2]])
print(sr3[['생년월일', '성별']])
print('\n')

# 여러 개의 원소를 선택(인덱스 범위 지정)
print('여러 개의 원소를 선택(인덱스 범위 지정)')
# print(sr3[1: 2])
print(sr3['생년월일': '성별'])

# 딕셔너리 -> 데이터프레임 변환
dic_dataFrame = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
# 판다스 DataFranc() 함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dic_dataFrame)
# df의 자료형 출력
print(type(df))
print('\n')
print(df)
print('\n')

# 행 인덱스/열 이름 설정
# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['준서', '예은'],
                  columns=['나이', '성별', '학교']
                  )
# 행 인덱스, 열 이름 확인하기
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')

# 행 인덱스/열 이름 설정
# 행 인덱스, 열 이름 변경하기
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')

# 행 인덱스/열 이름 변경
# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['준서', '예은'],
                  columns=['나이', '성별', '학교']
                  )
# 데이터프레임 df 출력
print("변경 전 df")
print(df)
print('\n')
# 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)
# df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)

# df 출력(변경 후)
print("변경 후 df")
print(df)
print('\n')

# 행 삭제
# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_dta = {
    '수학' : [90,80,70],
    '영어' : [98,89,95],
    '음악' : [85,95,100],
    '체육' : [100,90,90]
}

df = pd.DataFrame(exam_dta, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임 df를 복제해서 변수 df2에 저장. df2의 1개 행(row) 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print('df2의 1개 행(row) 삭제')
print(df2)
print('\n')

# 데이터프레임 df를 복제해서 변수 df3에 저장. df3의 2개 행(row) 삭제
df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)
print('df3의 2개 행(row) 삭제')
print(df3)
print('\n')

# 열 삭제
# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_dta = {
    '수학' : [90,80,70],
    '영어' : [98,89,95],
    '음악' : [85,95,100],
    '체육' : [100,90,90]
}

df = pd.DataFrame(exam_dta, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임 df를 복제해서 변수 df4에 저장. df4의 1개 열(column) 삭제
df4 = df.copy()
df4.drop('수학', axis=1, inplace=True)
print('df4의 1개 열(column) 삭제')
print(df4)
print('\n')

# 데이터프레임 df를 복제해서 변수 df5에 저장. df5의 2개 열(column) 삭제
df5 = df.copy()
df5.drop(['영어', '음악'], axis=1, inplace=True)
print('df5의 2개 열(column) 삭제')
print(df5)
print('\n')

# 행 선택
# 행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['서준']
position1 = df.iloc[0]
print('행 인덱스를 사용하여 행 1개 선택')
print(label1)
print('\n')
print(position1)
print('\n')

# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print('행 인덱스를 사용하여 2개 이상의 행 선택')
print(label2)
print('\n')
print(position2)
print('\n')

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print('행 인덱스의 범위를 지정하여 행 선택')
print(label3)
print('\n')
print(position3)
print('\n')

# 시리즈 사칙연산
# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})
print('딕셔너리 데이터로 판다스 시리즈 만들기')
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')

# 사직연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print('사직연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)')
print(result)
print('\n')

# NaN 값이 있는 시리즈 연산
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})
print('NaN 값이 있는 시리즈 연산')
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')

# 사직연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print('사직연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)')
print(result)
print('\n')

# 연산 메소드 사용 - 시리즈 연산
sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

# 사직연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print('연산 메소드 사용 : 사직연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)')
print(result)
print('\n')

# 데이터프레임에 숫자 더하기
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print('titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기')
print(df.head())
print('\n')
print(type(df))
print('\n')

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print('데이터프레임에 숫자 10 더하기')
print(addition.head())
print('\n')
print(type(addition))


#





