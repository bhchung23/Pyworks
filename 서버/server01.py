#서버 프로그램 만들기
from flask import Flask

app=Flask(__name__) #서버 객체 생성
@app.route('/') #루트 경로
def home():
    return "<h1>Hello~ Flask!</h1>"

app.run(debug=True) #서버 실행