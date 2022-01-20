from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key = "ertyhugf"

#首頁
@app.route("/")
def index():
    return render_template("index.html")

#帳密驗證頁面
@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]

    if account == "" or password == "":
        info = "請輸入帳號、密碼"
        return redirect(f"/error/?message={info}")
    elif account == "test" and password == "test":
        session["status"] = "已登入"
        return redirect("/member/")  
    else:
        info = "帳號或密碼輸入錯誤"
        return redirect(f"/error/?message={info}")

#登入成功頁面
@app.route("/member/")
def member():
    if session["status"] == "未登入":
        return redirect("/")
    else:
        return render_template("member.html")

#登入失敗頁面
@app.route("/error/")
def error():
    message = request.args.get("message","登入失敗")
    return render_template("error.html",data=message)

#登出頁面
@app.route("/signout")
def signout():
    session["status"] = "未登入"
    return redirect("/")

app.run(port=3000)
