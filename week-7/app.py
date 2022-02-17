from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from mysql.connector.pooling import MySQLConnectionPool


## 資料庫連線設定
db_config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "MySQL0126",
    "database" : "website",
    "auth_plugin" : "mysql_native_password"
}

dbpool = MySQLConnectionPool(
                    **db_config,
                    pool_name="my_connection_pool",
                    pool_size=5
                    )

mypool = dbpool.get_connection()
cursor = mypool.cursor()

app = Flask(__name__,
            static_url_path='/'
            )
app.secret_key = "wfegriw"


## 查詢會員資料 API
@app.route("/api/members")
def query_api():
    query_username = request.args.get("username")

    query_member = '''
        SELECT id, name, username
        FROM member
        WHERE username = %s ;
    '''

    cursor.execute(query_member,(query_username,))
    query_result = cursor.fetchone()

    try:
        data = {
            "id":query_result[0],
            "name":query_result[1],
            "username":query_result[2]
        }
    except:
        data = None
    finally:
        return jsonify({"data":data})


## 修改會員姓名 API
@app.route("/api/member",methods=["POST"])
def revise_api():
    username = session.get("username")
    status = session.get("status")
    update_name = request.json["name"]

    if status == "已登入":
        revise_name = '''
        UPDATE member
        SET name = %s 
        WHERE username = %s ;
        '''

        try:
            cursor.execute(revise_name,(update_name,username))
            mypool.commit()
            session["user"] = update_name
            return jsonify({"ok":True})
        except:
            mypool.rollback()
    return jsonify({"error":True})


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

    check_user = '''
    SELECT * 
    FROM member 
    WHERE username = %s ;
    '''

    if new_user == "" or new_username == "" or new_password == "":
        info = "姓名、帳號、密碼不得空白"
        return redirect(f"/error/?message={info}")


    cursor.execute(check_user,(new_username,) )
    result = cursor.fetchone()

    if result is None :
        add_user = '''
        INSERT INTO member(name, username, password)
        VALUES ( %s, %s, %s);
        '''

        user_data = [
            new_user, new_username, new_password
        ]

        cursor.execute(add_user,user_data)
        mypool.commit()

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

    verify_user = '''
    SELECT name, username, password
    FROM member
    WHERE username = %s ;
    '''

    cursor.execute(verify_user,(username,))
    verify_result = cursor.fetchone()

    try:
        user = verify_result[0]
        pswd = verify_result[2]

        if password != pswd:
            raise
    except:
        info = "帳號或密碼輸入錯誤"
        return redirect(f"/error/?message={info}")

    session["status"] = "已登入"
    session["user"] = user
    session["username"] = username
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


cursor.close()
mypool.close()
