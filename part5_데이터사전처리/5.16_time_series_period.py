# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# 날짜 형식의 문자열로 구성되는 리스트 정의
dates = ['2019-01-01', '2020-03-01', '2021-06-01']

# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환
ts_dates = pd.to_datetime(dates)   
print(ts_dates)
print('\n')

# Timestamp를 Period로 변환
print('frq() 옵션 => D:day(1일) / W:week(1주) / ME:month end(월말) / MS:month begin(월초) / Q:quarter end(분기말) / QS:quarter begin(분기초) / Y:year end(연말) / YS:year begin(연초) / B:business day(휴일제외) / h:hour(1시간) / T:minute(1분) / S:second(1초) / L:milisecond(1/1,000초) / U:microsecond(1/1,000,000초) / N:nanosecond(1/1,000,000,000초)')
pr_day = ts_dates.to_period(freq='D')
print(pr_day)
pr_month = ts_dates.to_period(freq='M')
print(pr_month)
# pr_year = ts_dates.to_period(freq='A')
pr_year = ts_dates.to_period(freq='Y')
print(pr_year)
