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
    value.append((data['SCA GCA'].sum() / (data['Min'].sum() / 90)) / (data['SCA SCA'].sum() / (data['Min'].sum() / 90)) if data['SCA SCA'].sum() != 0 else 0.0)
    value.append(((data['Tackles TklW'].sum() +  data['Int'].sum())/ (data['Min'].sum() / 90)) / (data['Tkl+Int'].sum() / (data['Min'].sum() / 90)) if data['Tkl+Int'].sum() != 0 else 0.0)
    value.append((data['Touches Att 3rd'].sum() / (data['Min'].sum() / 90)) / (data['Touches Touches'].sum() / (data['Min'].sum() / 90)) if data['Touches Touches'].sum() != 0 else 0.0)
    value.append((data['Passes Cmp'].sum() / (data['Min'].sum() / 90)) / (data['Passes Att'].sum() / (data['Min'].sum() / 90)) if data['Passes Att'].sum() != 0 else 0.0)
    value.append((data['Carries Fin 3rd'].sum() / (data['Min'].sum() / 90)) / (data['Carries Carries'].sum() / (data['Min'].sum() / 90)) if data['Carries Carries'].sum() != 0 else 0.0)
    value.append((data['Performance SoT'].sum() / (data['Min'].sum() / 90)) / (data['Performance Sh'].sum() / (data['Min'].sum() / 90)) if data['Performance Sh'].sum() != 0 else 0.0)

def fw_radar(player1, player2, player3, player4, player5):
    categories = ['Finishing', 'Assist', 'GCA', 'Defense', 'Ball Touch', 'Passing', 'Ball Carry', 'Shooting']
    cody_value = []
    curtis_value = []
    dominik_value= []
    harvey_value= []
    ryan_value= []
    # 각 포지션을 포함하는 행만 선택
    cody_data = player1[player1['Pos'].str.contains('LM|RM')]
    curtis_data = player2[player2['Pos'].str.contains('LM|RM')]
    dominik_data = player3[player3['Pos'].str.contains('LM|RM')]
    harvey_data = player4[player4['Pos'].str.contains('LM|RM')]
    ryan_data = player5[player5['Pos'].str.contains('LM|RM')]
    
    append_data(cody_value, cody_data)
    append_data(curtis_value, curtis_data)
    append_data(dominik_value, dominik_data)
    append_data(harvey_value, harvey_data)
    append_data(ryan_value, ryan_data)
    
    print(cody_value)
    print(curtis_value)
    print(dominik_value)
    print(harvey_value)
    print(ryan_value)
    
    # 각도 계산
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # 첫 번째 요소를 마지막으로 복사하여 폐곡선 만들기
    cody_value += cody_value[:1]
    curtis_value += curtis_value[:1]
    dominik_value += dominik_value[:1]
    harvey_value += harvey_value[:1]
    ryan_value += ryan_value[:1]
    angles += angles[:1]

    # 그래프 설정
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, cody_value, color='red', linestyle='solid', linewidth=2)
    ax.plot(angles, curtis_value, color='green', linestyle='solid', linewidth=2)
    ax.plot(angles, dominik_value, color='blue', linestyle='solid', linewidth=2)
    ax.plot(angles, harvey_value, color='magenta', linestyle='solid', linewidth=2)
    ax.plot(angles, ryan_value, color='yellow', linestyle='solid', linewidth=2)

    # 카테고리 레이블 추가
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    # 축의 레이블과 제목 추가
    ax.set_yticklabels([])
    ax.set_rlabel_position(180)

    # 그래프 표시
    plt.savefig('VS_mid_player/img/vs_mid_radar.png',dpi=300)
    plt.show()
    

cody_gakpo_data=dataget('csv/Cody-Gakpo/Cody-Gakpo_merged.csv')
curtis_jones_data=dataget('csv/Diogo-Jota/Diogo-Jota_merged.csv')
dominik_szoboszlai_data=dataget('csv/Dominik-Szoboszlai/Dominik-Szoboszlai_merged.csv')
harvey_elliott_data=dataget('csv/Harvey-Elliott/Harvey-Elliott_merged.csv')
ryan_Gravenberch_data=dataget('csv/Ryan-Gravenberch/Ryan-Gravenberch_merged.csv')

fw_radar(cody_gakpo_data, curtis_jones_data, dominik_szoboszlai_data, harvey_elliott_data, ryan_Gravenberch_data)