import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df
def fw_radar(player1, player2, player3):
    categories = ['Finishing', 'Assist', 'BOX Touch', '3rd Touch', 'Box Carry', '3rd Carry', 'GCA', 'Shooting']
    cody_value = []
    diogo_value = []
    darwin_value= []
    # 각 포지션을 포함하는 행만 선택
    cody_data = player1[player1['Pos'].str.contains('FW')]
    diogo_data = player2[player2['Pos'].str.contains('FW')]
    darwin_data = player3[player3['Pos'].str.contains('FW')]
    
    cody_value.append((cody_data['Performance Gls'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Expected xG'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['Performance Ast'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Expected xAG'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['Touches Att Pen'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Touches Touches'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['Touches Att 3rd'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Touches Touches'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['Carries CPA'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Carries Carries'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['Carries 1/3'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Carries Carries'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['SCA GCA'].sum()/(cody_data['Min'].sum()/90))/(cody_data['SCA SCA'].sum()/(cody_data['Min'].sum()/90)))
    cody_value.append((cody_data['Performance SoT'].sum()/(cody_data['Min'].sum()/90))/(cody_data['Performance Sh'].sum()/(cody_data['Min'].sum()/90)))
    
    diogo_value.append((diogo_data['Performance Gls'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Expected xG'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['Performance Ast'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Expected xAG'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['Touches Att Pen'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Touches Touches'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['Touches Att 3rd'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Touches Touches'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['Carries CPA'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Carries Carries'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['Carries 1/3'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Carries Carries'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['SCA GCA'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['SCA SCA'].sum()/(diogo_data['Min'].sum()/90)))
    diogo_value.append((diogo_data['Performance SoT'].sum()/(diogo_data['Min'].sum()/90))/(diogo_data['Performance Sh'].sum()/(diogo_data['Min'].sum()/90)))
    
    darwin_value.append((darwin_data['Performance Gls'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Expected xG'].sum()/(darwin_data['Min'].sum()/90)))
    darwin_value.append((darwin_data['Performance Ast'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Expected xAG'].sum()/(darwin_data['Min'].sum()/90)) if darwin_data['Expected xAG'].sum() != 0 else 0.0)
    darwin_value.append((darwin_data['Touches Att Pen'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Touches Touches'].sum()/(darwin_data['Min'].sum()/90)))
    darwin_value.append((darwin_data['Touches Att 3rd'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Touches Touches'].sum()/(darwin_data['Min'].sum()/90)))
    darwin_value.append((darwin_data['Carries CPA'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Carries Carries'].sum()/(darwin_data['Min'].sum()/90)))
    darwin_value.append((darwin_data['Carries 1/3'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Carries Carries'].sum()/(darwin_data['Min'].sum()/90)))
    darwin_value.append((darwin_data['SCA GCA'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['SCA SCA'].sum()/(darwin_data['Min'].sum()/90)))
    darwin_value.append((darwin_data['Performance SoT'].sum()/(darwin_data['Min'].sum()/90))/(darwin_data['Performance Sh'].sum()/(darwin_data['Min'].sum()/90)))
    
    # 각도 계산
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # 첫 번째 요소를 마지막으로 복사하여 폐곡선 만들기
    cody_value += cody_value[:1]
    diogo_value += diogo_value[:1]
    darwin_value += darwin_value[:1]
    angles += angles[:1]

    # 그래프 설정
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, cody_value, color='red', linestyle='solid', linewidth=2)
    ax.plot(angles, diogo_value, color='green', linestyle='solid', linewidth=2)
    ax.plot(angles, darwin_value, color='blue', linestyle='solid', linewidth=2)

    # 카테고리 레이블 추가
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)

    # 축의 레이블과 제목 추가
    ax.set_yticklabels([])
    ax.set_rlabel_position(180)

    # 그래프 표시
    plt.savefig('VS_fw_player/vs_fw_radar.png',dpi=300)
    plt.show()
    
    print(cody_value)
    print(diogo_value)
    print(darwin_value)

cody_gakpo_data=dataget('Cody-Gakpo/Cody-Gakpo_merged.csv')
diogo_jota_data=dataget('Diogo-Jota/Diogo-Jota_merged.csv')
darwin_nunez_data=dataget('Darwin-Nunez/Darwin-Nunez_merged.csv')
fw_radar(cody_gakpo_data, diogo_jota_data, darwin_nunez_data) #비교 스텟 바꿔가면서 반복