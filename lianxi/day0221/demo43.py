# Flask封装框架，render_template渲染模版
from flask import Flask, render_template

# 创建一个app应用
app = Flask(__name__)


# 创建路由
@app.route("/")
# 首页面
@app.route("/index")
def index():
    return render_template("index.html")


# 列表页面
@app.route("/list")
def list():
    return render_template("list.html")


# 详情页面
@app.route("/detail")
def detail():
    return render_template("detail.html")


# 启动服务
app.run()
