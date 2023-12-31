import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df

#포지션별 스텟 데이터 시각화
def fw_player_scatter(player1, player2, player3, stat1, stat2):
    # 각 포지션을 포함하는 행만 선택
    cody_data = player1[player1['Pos'].str.contains('FW')]
    diogo_data = player2[player2['Pos'].str.contains('FW')]
    darwin_data = player3[player3['Pos'].str.contains('FW')]
    
    #그래프 그리기
    plt.figure(facecolor='#FFFFFF')
    ax =plt.gca()
    ax.set_facecolor('#FFFFFF')
    plt.scatter(cody_data[stat1],cody_data[stat2],s=50,c='#FF0000') #Cody => R
    plt.scatter(diogo_data[stat1],diogo_data[stat2],s=50,c='#00FF00') #Diogo => G
    plt.scatter(darwin_data[stat1],darwin_data[stat2],s=50,c='#0000FF') #Darwin => B
    plt.xlabel(stat1)
    plt.ylabel(stat2)
    plt.tick_params(axis='y',direction='in',labelsize=15,pad=5,length=10,color='#7B7D7D',labelcolor='#7B7D7D')
    plt.tick_params(axis='x',direction='in',labelsize=15,pad=5,length=10,color='#7B7D7D',labelcolor='#7B7D7D')
    plt.title(stat2+'&'+stat1,c='#7B7D7D',size=15)
    
    #이미지 파일로 저장하기.
    plt.savefig('VS_fw_player/img/'+stat2+'&'+stat1+'.png',dpi=300)
    plt.show()

cody_gakpo_data=dataget('csv/Cody-Gakpo/Cody-Gakpo_merged.csv')
diogo_jota_data=dataget('csv/Diogo-Jota/Diogo-Jota_merged.csv')
darwin_nunez_data=dataget('csv/Darwin-Nunez/Darwin-Nunez_merged.csv')
fw_player_scatter(cody_gakpo_data, diogo_jota_data, darwin_nunez_data, 'Min', 'Passes Fin 3rd') #비교 스텟 바꿔가면서 반복
