import json
import os
import folium
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('D:\chromedriver.exe')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

geo = json.load(open('../LARD_ADM_SECT_SGG_27.json', encoding='UTF-8'))

map_jeju = folium.Map(location=[33.38, 126.53],  # 제주도 좌표
                      zoom_start=10,  # 확대 단계
                      tiles='cartodbpositron')  # 지도 종류
folium.Choropleth(geo_data=geo,  # 지도 데이터
                  fill_opacity=0,  # 투명도
                  line_weight=4).add_to(map_jeju)  # 선 두께, 지도에 추가
path_html = 'jeju_map.html'
map_jeju.save(path_html)
abs_path = os.path.abspath(path_html)
driver.get(abs_path)