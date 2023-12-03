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


2. 패스

|Pass Complete Percent|Progressive Pass|Pass Final 3rd|Pass Penalty Area|Key Pass|
|---|---|---|---|---|
|![Position Scatter](VS_Position/img/Passes%20Cmp%25&Min.png)|![Position Scatter](VS_Position/img/Passes%20PrgP&Min.png)|![Position Scatter](VS_Position/img/Passes%20Fin%203rd&Min.png)|![Position Scatter](VS_Position/img/PPA&Min.png)|![Position Scatter](VS_Position/img/KP&Min.png)|

3. 볼 운반

|Progressive Carry Distance|Progressive Carry|Carry Final 3rd|Carry Penalty Area|
|---|---|---|---|
|![Position Scatter](VS_Position/img/Carries%20PrgDist&Min.png)|![Position Scatter](VS_Position/img/Carries%20PrgC&Min.png)|![Position Scatter](VS_Position/img/Carries%20Fin%203rd&Min.png)|![Position Scatter](VS_Position/img/Carries%20CPA&Min.png)|

4. 볼 컨트롤

|Take-Ons|Progressive Recieive|Touch Final 3rd|Touch Penalty Area|
|---|---|---|---|
|![Position Scatter](VS_Position/img/Take-Ons%20Succ&Min.png)|![Position Scatter](VS_Position/img/Receiving%20PrgR&Min.png)|![Position Scatter](VS_Position/img/Touches%20Att%203rd&Min.png)|![Position Scatter](VS_Position/img/Touches%20Att%20Pen&Min.png)|





![Position Radar](VS_Position/img/vs_pos_radar.png)

