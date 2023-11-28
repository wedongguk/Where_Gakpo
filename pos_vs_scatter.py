import pandas as pd
import matplotlib.pyplot as plt

#데이터 가져오는 함수
def dataget(url):
    df=pd.read_csv(url)
    return df

#포지션별 스텟 데이터 시각화
def pos(data, stat1, stat2):
    # 각 포지션을 포함하는 행만 선택
    fw_data = data[data['Pos'].str.contains('FW')]
    mid_data = data[data['Pos'].isin(['LM','RM'])]
    lw_data = data[data['Pos'].str.contains('LW')]
    
    #그래프 그리기
    plt.figure(facecolor='#FFFFFF')
    ax =plt.gca()
    ax.set_facecolor('#FFFFFF')
    plt.scatter(fw_data[stat1],fw_data[stat2],s=50,c='#FF0000') #R => FW
    plt.scatter(mid_data[stat1],mid_data[stat2],s=50,c='#00FF00') #G => MID
    plt.scatter(lw_data[stat1],lw_data[stat2],s=50,c='#0000FF') #B => LW
    plt.xlabel(stat1)
    plt.ylabel(stat2)
    plt.tick_params(axis='y',direction='in',labelsize=15,pad=5,length=10,color='#7B7D7D',labelcolor='#7B7D7D')
    plt.tick_params(axis='x',direction='in',labelsize=15,pad=5,length=10,color='#7B7D7D',labelcolor='#7B7D7D')
    plt.title(stat1+'&'+stat2,c='#7B7D7D',size=15)
    
    #이미지 파일로 저장하기.
    plt.savefig('VS_Position/'+stat1+'&'+stat2+'.png',dpi=300)
    plt.show()

summary_data=dataget('Cody-Gakpo/Cody-Gakpo_summary.csv')
pos(summary_data,'Take-Ons Succ', 'Take-Ons Att') #비교 스텟 바꿔가면서 반복