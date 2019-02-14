"""
Flask装饰器
1.安装：pip install flask
2.导入模块：from flask import Flask
3.创建一个应用
4.注册路由（URL）
5.启动服务
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "首页"
@app.route("/zzy")
def zzyinfo():
    return "zzy的个人主页"
@app.route("/lzj")
def lzjinfo():
    return "lzj的个人主页"

@app.route("/lzj/pay")
def zzypay():
    return render_template("pay.html", name="lzj")
app.run()
