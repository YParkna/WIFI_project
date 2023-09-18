import json
import os
import folium
import pandas as pd
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('D:\chromedriver.exe')
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

geo_jeju = json.load(open('LARD_ADM_SECT_SGG_27.geojson',encoding='UTF-8'))


# 행정 구역 코드 출력
print(geo_jeju['features'][0]['properties'])
# 위도, 경도 좌표 출력
print(geo_jeju['features'][0]['geometry'])

# 02. 서울시 동별 외국인 인구 데이터 준비하기
# Foreigner_EMD_Seoul.csv : 서울시 동별 외국인 인구 통계
# 2021년 서울시의 동별 행정 구역 코드 , 동 이름, 외국인 인구를 담고 있음
# 국가 통계 포털 KOSIS의 지방자치단체외국인주민현황 데이터를 가공해서 만듬

jeju = pd.read_csv('jeju_wifi.csv')
print(jeju.head())

jeju.info()

# 행정 구역 코드를 나타낸 foreigner의 code는 int64 타입
# 행정 구역 코드가 문자 타입으로 되어 있어야 지도를 만드는데 활용 가능

# df.astype() 이용해 code를 문자 타입으로 바꿈
jeju['code']=foreigner['code'].astype(str)

# 03. 단계 구분도 만들기
# 지역을 8단계로 나누도록 8개 계급 구간의 하한값, 상한값을 만듬
bins=list(foreigner['pop'].quantile([0,0.2,0.4,0.5,0.6,0.8,0.9,1]))
print(bins)

# 서울이 가운데에 오도록 배경 지도를 만든 다음 단계 구분도를 추가
# 배경 지도 만들기
map_jeju = folium.Map(location=[33.38, 126.53],  # 제주도 좌표
                      zoom_start=10,  # 확대 단계
                      tiles='cartodbpositron')  # 지도 종류
# 인구가 많을 수록 진한 파란색으로 표현하도록 fill_color='Blues' 입력
# 외국인 인구가 결측치인 지역은 흰색으로 표현하도록 nan_fill_colors='White' 입력


# 단계 구분도 만들기
# folium.Choropleth(geo_data=geo_seoul,
#                   data=foreigner,
#                   columns=('code','pop'),
#                   key_on='feature.properties.ADM_DR_CD',
#                   fill_color='Blues',
#                   nan_fill_color='White',
#                   fill_opacity=1,
#                   line_opacity=0.5,
#                   bins=bins).add_to(map_seoul)

# path_html = 'output/02_01.html'
# map_seoul.save(path_html)
# abs_path = os.path.abspath(path_html)
# driver.get(abs_path)

# 04. 구 경계선 추가하기
# 만든 지도에 구 경계선 추가
# 서울시의 구 경계 좌표를 담은 SIG_Seoul.geojson 파일을 불러옴
# geo_seoul_sig = json.load(open('input/SIG_Seoul.geojson',encoding='UTF-8'))

# 서울시 구 경계선을 이용해 단계 구분도를 만든 다음,
# add_to(map_seoul)을 이용해 앞에 만든 지도에 추가
# 색깔을 칠하지 않도록 fill_opacity=0를 입력하고
# 구 경계선을 두껍게 나타내도록 line_weight=4를 입력

# # 서울 구 라인 추가
# folium.Choropleth(geo_data=geo_seoul_sig, # 지도 데이터
#                   fill_opacity=0, # 투명도
#                   line_weight=4).add_to(map_seoul) # 선 두께, 지도에 추가
# path_html='output/02_02.html'
# map_seoul.save(path_html)
# abs_path=os.path.abspath(path_html)
# driver.get(abs_path)