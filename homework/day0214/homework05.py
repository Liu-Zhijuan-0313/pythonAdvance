# 1.导入模块
from flask import Flask, render_template
# 2.创建一个app应用
app = Flask(__name__)
# 3.创建路由URL
@app.route("/")
def index():
    return "首页"
@app.route("/lzj")
def user():
    return "lzj的个人主页"
@app.route("/lzj/baoke")
def baoke():
    return render_template("index.html", name="lzj")
@app.route("/lzj/address")
def address():
    return render_template("address.html")
# 4.启动服务
app.run()
