"""
Flask:使用装饰器
1, pip install flask
2, from flask import Flask
3, 创建一个应用
4，注册路由（URL）
5,启动服务
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "首页"

@app.route("/wzk")
def wzkinfo():
    return "王增科的个主页"

@app.route("/zyp")
def zypinfo():
    return "张宇鹏的个主页"

@app.route("/wzk/pay")
def wzkpay():
    # return "<h1>王增科各种网站充值页面</h1>"
    return render_template('pay.html', name = "张振杰")

app.run()