import json
import os
import folium
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('D:\chromedriver.exe')
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

geo_kor = gpd.read_file('E:/SW/project/project_02/Z_SOP_BND_SIDO_PG.shp', encoding='cp949')
print(geo_kor['SIDO_NM'].head())
# geo_kor.plot(color='gray', edgecolor="w")
# plt.show()

wifi = pd.read_csv('wifi_all.csv')
wifi['시도']=wifi['시도'].astype(str)
wifi.set_index('번호',inplace=True)
wifi.drop(['위도','경도','상세주소'],axis=1,inplace=True) # 위도/경도 열(칼럼) 삭제
# print(df)

count_wifi = wifi['시도'].value_counts().reset_index()
count_wifi.columns = ['시도', 'count_wifi']

# 03. 단계 구분도 만들기
# 지역을 8단계로 나누도록 8개 계급 구간의 하한값, 상한값을 만듬
bins=list(count_wifi['count_wifi'].quantile([0,0.2,0.4,0.5,0.6,0.8,0.9,1]))

map_kor = folium.Map(location=[35.9078, 127.7669],# 서울 좌표
                       zoom_start=7,# 확대 단계
                       tiles='cartodbpositron') # 지도 종류

# 많을 수록 진한 파란색으로 표현하도록 fill_color='Blues' 입력
# 결측치 지역은 흰색으로 표현하도록 nan_fill_colors='White' 입력

# 단계 구분도 만들기
folium.Choropleth(geo_data=geo_kor,
                  data=count_wifi,
                  columns=('시도','count_wifi'),
                  key_on='feature.properties.SIDO_NM',
                  fill_color='Blues',
                  nan_fill_color='White',
                  fill_opacity=1,
                  line_opacity=0.5,
                  bins=bins).add_to(map_kor)

path_html = 'KoreaMap.html'
map_kor.save(path_html)
abs_path = os.path.abspath(path_html)
driver.get(abs_path)
