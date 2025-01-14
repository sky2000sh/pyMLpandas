import seaborn as sns

# print('\n')

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
df_head = df.head()
df_info = df.info

print('타이타닉 head :', df_head)
print('\n')
print('타이타닉 정보 :', df_info)
print('\n')

# deck 열의 NaN 개수 계산하기
nan_deck = df['deck'].value_counts(dropna=False)
print('deck 열의 NaN 개수 계산하기 =>')
print(nan_deck)
print('\n')

# isnull() 메서드로 누락 데이터 찾기
print('isnull() 메서드로 누락 데이터 찾기 =>')
print(df.head().isnull())
print('\n')

# notnull() 메서드로 누락 데이터 찾기
print('notnull() 메서드로 누락 데이터 찾기 =>')
print(df.head().notnull())
print('\n')

# isnull() 메서드로 누락 데이터 개수 구하기
print('isnull() 메서드로 누락 데이터 개수 구하기 =>')
print(df.head().isnull().sum(axis=0))
print('\n')




