import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df

def append_data(value, data):
    value.append((data['Performance Gls'].sum() / (data['Min'].sum() / 90)) / (data['Expected xG'].sum() / (data['Min'].sum() / 90)) if data['Expected xG'].sum() != 0 else 0.0)
    value.append((data['Performance Ast'].sum() / (data['Min'].sum() / 90)) / (data['Expected xAG'].sum() / (data['Min'].sum() / 90)) if data['Expected xAG'].sum() != 0 else 0.0)
    value.append((data['CrsPA'].sum() / (data['Min'].sum() / 90)) / (data['Pass Types Crs'].sum() / (data['Min'].sum() / 90)) if data['Pass Types Crs'].sum() != 0 else 0.0)
    value.append((data['Take-Ons Succ'].sum() / (data['Min'].sum() / 90)) / (data['Take-Ons Att'].sum() / (data['Min'].sum() / 90)) if data['Take-Ons Att'].sum() != 0 else 0.0)
    value.append((data['Carries CPA'].sum() / (data['Min'].sum() / 90)) / (data['Carries Carries'].sum() / (data['Min'].sum() / 90)) if data['Carries Carries'].sum() != 0 else 0.0)
    value.append((data['Carries Fin 3rd'].sum() / (data['Min'].sum() / 90)) / (data['Carries Carries'].sum() / (data['Min'].sum() / 90)) if data['Carries Carries'].sum() != 0 else 0.0)
    value.append((data['SCA GCA'].sum() / (data['Min'].sum() / 90)) / (data['SCA SCA'].sum() / (data['Min'].sum() / 90)) if data['SCA SCA'].sum() != 0 else 0.0)
    value.append((data['PPA'].sum() / (data['Min'].sum() / 90)) / (data['Passes Cmp'].sum() / (data['Min'].sum() / 90)) if data['Passes Cmp'].sum() != 0 else 0.0)

def fw_radar(player1, player2, player3):
    categories = ['Finishing', 'Assist', 'Crros into PA', 'Dribble', 'Box Carry', '3rd Carry', 'GCA', 'Pass into PA']
    cody_value = []
    diogo_value = []
    luis_value= []
    # 각 포지션을 포함하는 행만 선택
    cody_data = player1[player1['Pos'].str.contains('LW')]
    diogo_data = player2[player2['Pos'].str.contains('LW')]
    luis_data = player3[player3['Pos'].str.contains('LW')]
    
    append_data(cody_value, cody_data)
    append_data(diogo_value, diogo_data)
    append_data(luis_value, luis_data)
    
    # 각도 계산
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # 첫 번째 요소를 마지막으로 복사하여 폐곡선 만들기
    cody_value += cody_value[:1]
    diogo_value += diogo_value[:1]
    luis_value += luis_value[:1]
    angles += angles[:1]

    # 그래프 설정
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, cody_value, color='red', linestyle='solid', linewidth=2)
    ax.plot(angles, diogo_value, color='green', linestyle='solid', linewidth=2)
    ax.plot(angles, luis_value, color='blue', linestyle='solid', linewidth=2)

    # 카테고리 레이블 추가
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    # 축의 레이블과 제목 추가
    ax.set_yticklabels([])
    ax.set_rlabel_position(180)

    # 그래프 표시
    plt.savefig('VS_lw_player/vs_lw_radar.png',dpi=300)
    plt.show()
    
    print(cody_value)
    print(diogo_value)
    print(luis_value)

cody_gakpo_data=dataget('csv/Cody-Gakpo/Cody-Gakpo_merged.csv')
diogo_jota_data=dataget('csv/Diogo-Jota/Diogo-Jota_merged.csv')
luis_diaz_data=dataget('csv/Luis-Diaz/Luis-Diaz_merged.csv')
fw_radar(cody_gakpo_data, diogo_jota_data, luis_diaz_data) #비교 스텟 바꿔가면서 반복