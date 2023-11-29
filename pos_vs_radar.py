import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df
def pos_radar(data):
    categories = ['Finishing', 'Assist', 'Passing', 'Dribbling', 'Prg Passing', 'Prg Carry', 'Shooting']
    fw_value = []
    mid_value = []
    lw_value= []
    # 각 포지션을 포함하는 행만 선택
    fw_data = data[data['Pos'].str.contains('FW')]
    mid_data = data[data['Pos'].isin(['LM','RM'])]
    lw_data = data[data['Pos'].str.contains('LW')]
    
    fw_value.append((fw_data['Performance Gls'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Expected xG'].sum()/(fw_data['Min'].sum()/90)))
    fw_value.append((fw_data['Performance Ast'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Expected xAG'].sum()/(fw_data['Min'].sum()/90)))
    fw_value.append((fw_data['Passes Cmp'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Passes Att'].sum()/(fw_data['Min'].sum()/90)))
    fw_value.append((fw_data['Take-Ons Succ'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Take-Ons Att'].sum()/(fw_data['Min'].sum()/90)))
    fw_value.append((fw_data['Passes PrgP'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Passes Cmp'].sum()/(fw_data['Min'].sum()/90)))
    fw_value.append((fw_data['Carries PrgC'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Carries Carries'].sum()/(fw_data['Min'].sum()/90)))
    fw_value.append((fw_data['Performance SoT'].sum()/(fw_data['Min'].sum()/90))/(fw_data['Performance Sh'].sum()/(fw_data['Min'].sum()/90)))
    
    mid_value.append((mid_data['Performance Gls'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Expected xG'].sum()/(mid_data['Min'].sum()/90)))
    mid_value.append((mid_data['Performance Ast'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Expected xAG'].sum()/(mid_data['Min'].sum()/90)))
    mid_value.append((mid_data['Passes Cmp'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Passes Att'].sum()/(mid_data['Min'].sum()/90)))
    mid_value.append((mid_data['Take-Ons Succ'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Take-Ons Att'].sum()/(mid_data['Min'].sum()/90)))
    mid_value.append((mid_data['Passes PrgP'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Passes Cmp'].sum()/(mid_data['Min'].sum()/90)))
    mid_value.append((mid_data['Carries PrgC'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Carries Carries'].sum()/(mid_data['Min'].sum()/90)))
    mid_value.append((mid_data['Performance SoT'].sum()/(mid_data['Min'].sum()/90))/(mid_data['Performance Sh'].sum()/(mid_data['Min'].sum()/90)))
    
    lw_value.append((lw_data['Performance Gls'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Expected xG'].sum()/(lw_data['Min'].sum()/90)))
    lw_value.append((lw_data['Performance Ast'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Expected xAG'].sum()/(lw_data['Min'].sum()/90)) if lw_data['Expected xAG'].sum() != 0 else 0.0)
    lw_value.append((lw_data['Passes Cmp'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Passes Att'].sum()/(lw_data['Min'].sum()/90)))
    lw_value.append((lw_data['Take-Ons Succ'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Take-Ons Att'].sum()/(lw_data['Min'].sum()/90)))
    lw_value.append((lw_data['Passes PrgP'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Passes Cmp'].sum()/(lw_data['Min'].sum()/90)))
    lw_value.append((lw_data['Carries PrgC'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Carries Carries'].sum()/(lw_data['Min'].sum()/90)))
    lw_value.append((lw_data['Performance SoT'].sum()/(lw_data['Min'].sum()/90))/(lw_data['Performance Sh'].sum()/(lw_data['Min'].sum()/90)))
    
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
    plt.savefig('VS_Position/vs_pos_radar.png',dpi=300)
    plt.show()
    
    print(fw_value)
    print(mid_value)
    print(lw_value)

summary_data=dataget('Cody-Gakpo/Cody-Gakpo_summary.csv')

pos_radar(summary_data)