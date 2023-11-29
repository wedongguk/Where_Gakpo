import pandas as pd
import re
import os

def process_match_logs(url_df, log_type):
    # URL에서 선수 이름 추출
    match = re.search(r'/([A-Za-z0-9-]+)-Match-Logs', url_df)
    
    if match:
        player_name = match.group(1)
        print(player_name)
    else:
        print("이름을 찾을 수 없습니다.")
    
    # 디렉토리 생성 (이미 존재하면 생성하지 않음)
    if not os.path.exists(player_name):
        os.makedirs(player_name)

    # HTML 테이블 읽기
    dfs = pd.read_html(url_df)
    df = dfs[0]

    # 열 이름 표준화
    df.columns = [' '.join(col).strip() for col in df.columns]
    df = df.reset_index(drop=True)

    # 새로운 열 이름 생성
    new_columns = [col.split()[-1] if 'level_0' in col else col for col in df.columns]
    df.columns = new_columns
    df = df.fillna(0)

    # 데이터 전처리
    df['Squad'] = df['Squad'].replace('eng Liverpool', 'Liverpool')
    df = df[df['Report'] == 'Match Report']
    df = df[df['Squad'] == 'Liverpool']
    df = df[df['Pos'] != 'On matchday squad, but did not play']
    df = df[df['Comp'] != 'EFL Cup']

    # DataFrame을 CSV 파일로 저장
    df.to_csv(f'{player_name}/{player_name}_{log_type.lower()}.csv', index=False)

# 선수 이름 바꾸면서 스크래핑
player_name = 'Harvey-Elliott' 
player_id = 'b9e1436c'
url_possession = f'https://fbref.com/en/players/{player_id}/matchlogs/2023-2024/possession/{player_name}-Match-Logs'
process_match_logs(url_possession, 'Possession')

url_defense = f'https://fbref.com/en/players/{player_id}/matchlogs/2023-2024/defense/{player_name}-Match-Logs'
process_match_logs(url_defense, 'Defense')

url_passing = f'https://fbref.com/en/players/{player_id}/matchlogs/2023-2024/passing/{player_name}-Match-Logs'
process_match_logs(url_passing, 'Passing')

url_summary = f'https://fbref.com/en/players/{player_id}/matchlogs/2023-2024/{player_name}-Match-Logs'
process_match_logs(url_summary, 'Summary')
