#공공와이파이(전국)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv('wifi_all.csv')
# print(df)

df1.set_index('번호',inplace=True)
df1.drop(['위도','경도','상세주소'],axis=1,inplace=True) #위도/경도 열(칼럼) 삭제
# print(df)

count_wifi=df1['시도'].value_counts() #시도별 와이파이 ap개수
df1['count_wifi']=count_wifi
print(count_wifi)
'''
시도
경기도        13157
서울특별시      10154
경상북도        7090
인천광역시       6270
전라남도        6264
강원도         6112
경상남도        5612
제주특별자치도     4807
대전광역시       4576
충청남도        3789
부산광역시       3621
충청북도        3480
전라북도        3453
광주광역시       3386
대구광역시       2896
울산광역시       2069
세종특별자치시      739
'''

total_wifi=len(df1) #전체 ap개수
ratio_wifi=count_wifi/total_wifi #와이파이 개수/전국 와이파이 개수
# print(ratio_wifi)

ratio_wifi_percent = ratio_wifi.apply(lambda x: '{:.2%}'.format(x)) #%로 계산
print(ratio_wifi_percent)

#######################그래프#######################

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False #두줄=맑은고딕 폰트

x=count_wifi.index
y=count_wifi.values

colors = ['blue'] * len(x)  # 기본 색상: blue
gg = x.tolist().index('경기도')
colors[gg] = 'gold'  # 경기도: gold색

# 막대그래프: 전국 공공와이파이 ap개수
plt.bar(x,count_wifi,color=colors,alpha=0.5) #alpha=0.5==>투명도(1에 가까울수록 투명도가 낮음)
plt.xlabel('시도')
plt.ylabel('비율 (%)')
plt.title('시도별 공공 와이파이 비율')
plt.xticks(rotation=45) #x축 라벨 각도(45도로 지정)

for i,v in enumerate(count_wifi):
    plt.text(i,v+100,f'{v:,}',ha='center') #f'{v:,} ==>천단위 콤마

plt.show()
#################################################