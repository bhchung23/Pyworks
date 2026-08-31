#
from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") #웹 페이지를 업로드 하겠다.

@app.route('/gallery')
def gallery():
    photo_list = os.listdir("static/photos")
    return render_template("gallery.html", photos=photo_list)

app.run(debug=True)