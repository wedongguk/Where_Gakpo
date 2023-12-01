import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df

def append_data(value, data):
    value.append((data['Performance Gls'].sum() / (data['Min'].sum() / 90)) / (data['Expected xG'].sum() / (data['Min'].sum() / 90)) if data['Expected xG'].sum() != 0 else 0.0)
    value.append((data['Performance Ast'].sum() / (data['Min'].sum() / 90)) / (data['xA'].sum() / (data['Min'].sum() / 90)) if data['xA'].sum() != 0 else 0.0)
    value.append((data['Passes Cmp'].sum() / (data['Min'].sum() / 90)) / (data['Passes Att'].sum() / (data['Min'].sum() / 90)) if data['Passes Att'].sum() != 0 else 0.0)
    value.append((data['Take-Ons Succ'].sum() / (data['Min'].sum() / 90)) / (data['Take-Ons Att'].sum() / (data['Min'].sum() / 90)) if data['Take-Ons Att'].sum() != 0 else 0.0)
    value.append((data['Passes PrgP'].sum() / (data['Min'].sum() / 90)) / (data['Passes Cmp'].sum() / (data['Min'].sum() / 90)) if data['Passes Cmp'].sum() != 0 else 0.0)
    value.append((data['Carries PrgC'].sum() / (data['Min'].sum() / 90)) / (data['Carries Carries'].sum() / (data['Min'].sum() / 90)) if data['Carries Carries'].sum() != 0 else 0.0)
    value.append((data['Performance SoT'].sum() / (data['Min'].sum() / 90)) / (data['Performance Sh'].sum() / (data['Min'].sum() / 90)) if data['Performance Sh'].sum() != 0 else 0.0)

def pos_radar(data):
    categories = ['Finishing', 'Assist', 'Passing', 'Dribbling', 'Prg Passing', 'Prg Carry', 'Shooting']
    fw_value = []
    mid_value = []
    lw_value= []
    # 각 포지션을 포함하는 행만 선택
    fw_data = data[data['Pos'].str.contains('FW')]
    mid_data = data[data['Pos'].str.contains('LM|RM')]
    lw_data = data[data['Pos'].str.contains('LW')]
    
    append_data(fw_value, fw_data)
    append_data(mid_value, mid_data)
    append_data(lw_value, lw_data)
    
    # 각도 계산
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # 첫 번째 요소를 마지막으로 복사하여 폐곡선 만들기
    fw_value += fw_value[:1]
    mid_value += mid_value[:1]
    lw_value += lw_value[:1]
    angles += angles[:1]

    # 그래프 설정
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, fw_value, color='red', linestyle='solid', linewidth=2)
    ax.plot(angles, mid_value, color='green', linestyle='solid', linewidth=2)
    ax.plot(angles, lw_value, color='blue', linestyle='solid', linewidth=2)

    # 카테고리 레이블 추가
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    # 축의 레이블과 제목 추가
    ax.set_yticklabels([])
    ax.set_rlabel_position(180)

    # 그래프 표시
    plt.savefig('VS_Position/img/vs_pos_radar.png',dpi=300)
    plt.show()
    
    print(fw_value)
    print(mid_value)
    print(lw_value)

data=dataget('csv/Cody-Gakpo/Cody-Gakpo_merged.csv')

pos_radar(data)