## jupyter 설정

```py
터미널 (CLI)
환경 변수 - Path (경로)
OS 변수
x = 5
name = 'young'

OS (운영 시스템) 구성
 -> Terminal (명령을 실행하는 곳)
 -> 환경 변수 (Terminal에서 사용할 변수 등록해놓는 곳)
   -> 그 중 Path 변수 (프로그램들의 경로들을 미리 등록)
그 결과, Terminal에서 git.exe, conda.exe(bat)의 위치를 직접 찾지 않아도 사용이 가능해진다.

개발 환경 설정
Python을 사용하기 위해 Anaconda를 설치
★가상 환경 (Virtual Environment)
 -> 특정 python 버전을 등록한 환경 (추가 설치한 라이브러리들을 가상환경 별로 격리하여 관리)

아나콘다에서 가상환경 생성 예시
 - conda create -n study python=3.12
 - conda env list

conda create -n 가상환경이름 python=버전
conda env list

CTRL + S 저장
GUI - cell 생성, 삭제

단축키
ESC - 명령모드

명령모드에서
a - 위에 셀 생성
b - 아래에 셀 생성
dd - 삭제

셀 유형 변환
M - 마크다운으로
Y - 파이썬으로

""" """ -> 코드처럼 처리가 안 되고, 문자열 텍스트처럼 처리됨.
```