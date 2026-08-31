#서버 프로그램 만들기
from flask import Flask

app=Flask(__name__) #서버 객체 생성

#http://127.0.0.1:5000/ 내 컴퓨터:포트번호 로 정해져 있음
@app.route('/') #루트 경로
def home():
    return "<h1>Hello~ Flask!</h1>" #h1(큰 클씨)~h6(작은 글씨)

@app.route('/login') #'/'를 이용해 홈 -> 새로운 아래 페이지 생성
def login():
    return "<h2>로그인 페이지 입니다.</h2>"

app.run(debug=True) #서버 실행

#웹 기술(언어) html, css(for 크롤링)