import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df

#포지션별 스텟 데이터 시각화
def fw_player_scatter(player1, player2, player3, player4, player5, stat1, stat2):
    # 각 포지션을 포함하는 행만 선택
    cody_data = player1[player1['Pos'].str.contains('LM|RM')]
    curtis_data = player2[player2['Pos'].str.contains('LM|RM')]
    dominik_data = player3[player3['Pos'].str.contains('LM|RM')]
    harvey_data = player4[player4['Pos'].str.contains('LM|RM')]
    ryan_data = player5[player5['Pos'].str.contains('LM|RM')]
    
    
    #그래프 그리기
    plt.figure(facecolor='#FFFFFF')
    ax =plt.gca()
    ax.set_facecolor('#FFFFFF')
    plt.scatter(cody_data[stat1],cody_data[stat2],s=50,c='#FF0000') #Cody => R
    plt.scatter(curtis_data[stat1],curtis_data[stat2],s=50,c='#00FF00') #Curtis => G
    plt.scatter(dominik_data[stat1],dominik_data[stat2],s=50,c='#0000FF') #Dominik => B
    plt.scatter(harvey_data[stat1],harvey_data[stat2],s=50,c='#FF00FF') #Harvey => M
    plt.scatter(ryan_data[stat1],ryan_data[stat2],s=50,c='#FFFF00') #Ryan => Y
    plt.xlabel(stat1)
    plt.ylabel(stat2)
    plt.tick_params(axis='y',direction='in',labelsize=15,pad=5,length=10,color='#7B7D7D',labelcolor='#7B7D7D')
    plt.tick_params(axis='x',direction='in',labelsize=15,pad=5,length=10,color='#7B7D7D',labelcolor='#7B7D7D')
    plt.title(stat2+'&'+stat1,c='#7B7D7D',size=15)
    
    #이미지 파일로 저장하기.
    plt.savefig('VS_mid_player/'+stat2+'&'+stat1+'.png',dpi=300)
    plt.show()

cody_gakpo_data=dataget('Cody-Gakpo/Cody-Gakpo_merged.csv')
curtis_jones_data=dataget('Curtis-Jones/Curtis-Jones_merged.csv')
dominik_szboszlai_data=dataget('Dominik-Szoboszlai/Dominik-Szoboszlai_merged.csv')
harvey_elliott_data=dataget('Harvey-Elliott/Harvey-Elliott_merged.csv')
ryan_Gravenberch_data=dataget('Ryan-Gravenberch/Ryan-Gravenberch_merged.csv')
fw_player_scatter(cody_gakpo_data, curtis_jones_data, dominik_szboszlai_data, harvey_elliott_data, ryan_Gravenberch_data, 'Min', 'Tackles Mid 3rd') #비교 스텟 바꿔가면서 반복
