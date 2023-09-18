import tkinter as tk
import pandas as pd
from PIL import ImageTk, Image

df1 = pd.read_excel('c:/data3/wifi_all.xlsx')
df1.set_index('번호', inplace=True)
df1.drop(['위도', '경도', '상세주소'], axis=1, inplace=True)

count_wifi = df1['시도'].value_counts()
total_wifi = len(df1)
ratio_wifi = count_wifi / total_wifi
ratio_wifi_percent = ratio_wifi.apply(lambda x: '{:.2%}'.format(x))

# '제주도'와 '제주특별자치도' 매칭
count_wifi['제주도'] = count_wifi['제주특별자치도']
count_wifi.drop('제주특별자치도', inplace=True)


def show_graph_value():
    region = entry.get()
    if region in count_wifi.index:
        value = count_wifi.loc[region]
        label_value.config(text=f"지역 {region}의 공공 와이파이 개수: {value}")
    else:
        label_value.config(text="해당 지역의 데이터가 없습니다.")


root = tk.Tk()

label = tk.Label(root, text="지역을 입력하세요.")
label.grid(row=1, column=0, padx=30, pady=10)  # 격자의 첫 번째 행에 배치

entry = tk.Entry(root)
entry.grid(row=2, column=0, padx=20, pady=10)  # 격자의 두 번째 행에 배치

button = tk.Button(root, text="확인", command=show_graph_value)
button.grid(row=3, column=0, padx=20, pady=10)  # 격자의 세 번째 행에 배치

# 이미지 로드
image_path = "image.jpg"  # 이미지 파일 경로
image = Image.open(image_path)
image = image.resize((300, 100))  # 이미지 크기 조정
photo = ImageTk.PhotoImage(image)

# 이미지를 표시할 Label 생성
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, padx=20, pady=10)  # 격자의 네 번째 행에 배치

label_value = tk.Label(root, text="")
label_value.grid(row=4, column=0, padx=30, pady=10)  # 격자의 다섯 번째 행에 배치

root.mainloop()