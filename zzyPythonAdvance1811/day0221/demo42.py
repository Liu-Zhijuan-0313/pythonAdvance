"""
使用Flask进行HTTP编程
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    # return "<h1>这是首页</h1>"
    return render_template("index.html")
@app.route("/list.html")
def list():
    # return "这个是列表页"
    return render_template("list.html")
@app.route("/detail.html")
def detail():
    # return "这个是详情页"
    return render_template("detail.html")

app.run()