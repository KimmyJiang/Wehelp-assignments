from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector


## 資料庫連線設定
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL0126",
    database = "website",
    auth_plugin = "mysql_native_password"
)

cursor = db.cursor()

app = Flask(__name__)
app.secret_key = "12345"


## 首頁
@app.route("/")
def index():
    status = session.get("status", "未登入")
    if status != "已登入":
        return render_template("index.html")
    return redirect("/member/")


## 註冊頁面
@app.route("/signup",methods=["POST"])
def signup():
    new_user = request.form["new_user"]
    new_username = request.form["new_username"]
    new_password = request.form["new_password"]

    if new_user == "" or new_username == "" or new_password == "":
        info = "姓名、帳號、密碼不得空白"
        return redirect(f"/error/?message={info}")
        
    check_user = f'''
    SELECT * 
    FROM member 
    WHERE username = "{new_username}";
    ''' 
    cursor.execute(check_user)
    result = cursor.fetchall()

    if len(result) == 0:
        add_user = f'''
        INSERT INTO member(name, username, password)
        VALUES ("{new_user}","{new_username}","{new_password}");
        '''

        cursor.execute(add_user)
        db.commit()

        return redirect("/")

    info = "帳號已經被註冊"
    return redirect(f"/error/?message={info}")


## 登入帳號驗證頁面
@app.route("/signin",methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    if username == "" or password == "":
        info = "請輸入帳號、密碼"
        return redirect(f"/error/?message={info}")

    verify_user = f'''
    SELECT name, username, password
    FROM member
    WHERE username = "{username}";
    ''' 

    cursor.execute(verify_user)
    verify_result = cursor.fetchall()

    try:
        user = verify_result[0][0]
        pswd = verify_result[0][2]

        if password != pswd:
            raise
    except:
        info = "帳號或密碼輸入錯誤"
        return redirect(f"/error/?message={info}")

    session["status"] = "已登入"
    session["user"] = user
    return redirect("/member/")


## 登入成功頁面
@app.route("/member/")
def member():
    status = session.get("status", "未登入")
    if status == "已登入":
        return render_template("member.html", user=session.get("user"))
    return redirect("/")


## 登入失敗頁面
@app.route("/error/")
def error():
    message = request.args.get("message","登入失敗")
    return render_template("error.html", data=message)


## 登出頁面
@app.route("/signout")
def signout():
    session["status"] = "未登入"
    session["user"] = ""
    return redirect("/")

app.run(port=3000)
