# :soccer: Where Gakpo ⁉
21101203 위동국 OSS Project

### 프로젝트 주제
코디 각포의 최적의 포지션은 어디인가
* 평소 프리미어리그의 축구 클럽 리버풀의 열렬한 팬으로써 경기를 챙겨보던 중 코디 각포 선수가 여러 포지션에서 뛰는 모습을 보고 과연 어떤 포지션이 최고의 경기력을 보여줄 수 있는 최적의 포지션인지 궁금증이 생겨 시작하게 되었습니다.

### 사용한 오픈소스 라이브러리
* Pandas
* Numpy
* Matplotlib
* re
* os

### 사용한 데이터
* FBREF https://fbref.com/en/에서 코디 각포 선수의 Match Log를 스크래핑 하여 사용했습니다.
* 11/25일까지의 22-23시즌 리그 경기와 유로파 경기의 데이터만 사용했습니다.

### 포지션별 데이터 시각화 및 분석
코디 각포 선수는 리버풀에서 포워드, 윙, 미드필더 총 세가지 포지션으로 경기를 뛰었습니다.

이 세 포지션이 공통으로 중요하다고 생각하는 스텟들을 경기를 뛴 시간 대비 얼마나 쌓았나 비교해보았습니다.

아래의 Scatter Plot에서 빨간색이 포워드, 초록색이 미드필더, 파란색이 윙을 나타냅니다.

1. 공격 포인트

|Goal|Asist|Shot|Shot On Target|Shot Creating Action|
|---|---|---|---|---|
|![Position Scatter](VS_Position/img/Performance%20Gls&Min.png)|![Position Scatter](VS_Position/img/Performance%20Ast&Min.png)|![Position Scatter](VS_Position/img/Performance%20Sh&Min.png)|![Position Scatter](VS_Position/img/Performance%20SoT&Min.png)|![Position Scatter](VS_Position/img/SCA%20SCA&Min.png)|

FW와 MID에서 각각 1골, FW에서 1어시를 적립하였고, 같은 시간을 뛰었을 때 LW에서 슈팅이 더 많지만 유효슈팅은 비슷하다는 것을 알 수 있었습니다. 

2. 패스

|Pass Complete Percent|Progressive Pass|Pass Final 3rd|Pass Penalty Area|Key Pass|
|---|---|---|---|---|
|![Position Scatter](VS_Position/img/Passes%20Cmp%25&Min.png)|![Position Scatter](VS_Position/img/Passes%20PrgP&Min.png)|![Position Scatter](VS_Position/img/Passes%20Fin%203rd&Min.png)|![Position Scatter](VS_Position/img/PPA&Min.png)|![Position Scatter](VS_Position/img/KP&Min.png)|

같은 시간을 뛰었을 때 평균적으로 MID에서 패스정확도, 전진패스, 파이널 써드 지역으로 패스, 패널티 지역으로 패스, 키패스 횟수 모두 높다는 것을 알 수 있었습니다.

3. 볼 운반

|Progressive Carry Distance|Progressive Carry|Carry Final 3rd|Carry Penalty Area|
|---|---|---|---|
|![Position Scatter](VS_Position/img/Carries%20PrgDist&Min.png)|![Position Scatter](VS_Position/img/Carries%20PrgC&Min.png)|![Position Scatter](VS_Position/img/Carries%20Fin%203rd&Min.png)|![Position Scatter](VS_Position/img/Carries%20CPA&Min.png)|

Progressive Carry란 쉽게 말하면 전진 드리블, 보다 정확한 의미는 "상대진영에서 골라인을 향해 적어도 10야드 볼 이동" 입니다. 

볼 운반 또한 같은 시간을 뛰었을 때 MID에서의 스텟이 평균적으로 높다는 사실을 알 수 있었습니다.

4. 볼 컨트롤

|Take-Ons|Progressive Recieive|Touch Final 3rd|Touch Penalty Area|
|---|---|---|---|
|![Position Scatter](VS_Position/img/Take-Ons%20Succ&Min.png)|![Position Scatter](VS_Position/img/Receiving%20PrgR&Min.png)|![Position Scatter](VS_Position/img/Touches%20Att%203rd&Min.png)|![Position Scatter](VS_Position/img/Touches%20Att%20Pen&Min.png)|

Take-Ons란 완전히 등 뒤로 재친 수비수의 숫자를 의미합니다.

볼 컨트롤 부분에서는 같은 시간을 뛰었을 때 세 포지션이 비슷한 스텟을 가지지만, FW가 약간 높은 수치를 보인다는 것을 알 수 있었습니다.

Scatter Plot을 통해 포지션별 스텟을 비교하였을 때, 각 포지션이 뛴 시간도 다르고, 데이터의 개수도 달라서 정확한 비교가 어렵다고 생각하여 데이터를 가공하여 Radar Plot으로 비교해보고자 하였습니다.

아래의 Radar Plot은 각 스텟을 90당 기록으로 계산하여 만들었습니다. 

'Finishing'은 90당 기대득점 대비 득점, 'Assist'는 90당 기대 어시스트 대비 어시스트, 'Passing'은 90당 패스 시도 대비 패스 성공, 'Dribbling'은 90당 Take-on 시도 대비 성공, 'Prg Passing' 90당 패스 성공 대비 전진 패스, 'Touches' 90분 당 터치 대비 파이널 써드에서의 터치, 'Prg Carry' 90분 당 볼 운반 대비 전진 드리블, 'Shooting'은 90분당 슈팅 대비 유효슈팅을 의미합니다.

![Position Radar](VS_Position/img/vs_pos_radar.png)

Radar Plot을 보면 LW에서는 드리블을 제외한 모든 스텟에서 상대적으로 밀리는 것을 알 수 있고,  FW에서 드리블을 제외하고 전체적으로 비슷하거나 높은 수치를 기록한다는 사실을 알 수 있습니다. 

하지만 MID에서도 어시스트를 제외한 모든 스텟에서 준수한 능력치를 보여주기 때문에 이 정보들만으로는 어느 포지션이 최적의 포지션이라고 판단하기에는 부족하다고 생각하였습니다. 그래서 보다 정확한 분석을 위해 같은 팀에서 뛰는 다른 선수들과 비교해보았습니다.


