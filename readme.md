# 규약

# Commit Message Format
- [add] 추가한 내용
- [mdf] 수정한 내용
- [del] 지운 내용
- [merge] 병합

> 예시 : [add] main app 생성

# branch
- 루트 및 배포 : master
- 개발 : develop
- 개인 : 각자 닉네임 or 이름

# 협업 순서

[개발 단계]
1. 각자의 branch에서 작업
2. 각자의 branch에서 develop에 Pull Request
3. develop branch에서 최소 1명 검열 후 merge 

[배포 단계]

4. develop branch에서 master에 Pull Request
5. master branch에서 merge


### 치훈
* 2020-07-16
  * Sign in , Sign up Flow 개선 작업 및 Authenticate수정
  * 구독 기능구현
  * 매일 Checklist초기화 되는 기능 구현
  * 매일 달성률 기록할수있는 Model생성
  * 유저 생성시 default mission random으로 분배
* 2020-07-17
  * Task CRUD 기능 구현
  * 전체 기록을 남길 필요성이 있어서 Checking되는 부분 totalLog로 기록
  * Task에 일수 추가 기능
  * Task Model에 desc , tags, period 추가
  * 페이지별 요소 재분배, 템플릿 상속
  * Task Create Page change display field
  * Task Create PAge Period Task List Toggle ADD