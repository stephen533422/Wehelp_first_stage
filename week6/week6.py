import flask
import mysql.connector
import os

app = flask.Flask(__name__)
app.secret_key = os.urandom(12).hex()

@app.route("/")
def index():
    return flask.render_template("home.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = flask.request.form["name"]
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    # print(name, username, password)
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor = connection.cursor()
        create_stmt= ("CREATE DATABASE IF NOT EXISTS website")
        cursor.execute(create_stmt)
        use_stmt= ("USE website")
        cursor.execute(use_stmt)
        create_stmt= ("""
            CREATE TABLE IF NOT EXISTS member (
                id BIGINT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,    
                password VARCHAR(255) NOT NULL,    
                follower_count INT UNSIGNED NOT NULL DEFAULT 0,    
                time DATETIME NOT NULL DEFAULT NOW())"""
        )
        cursor.execute(create_stmt)
        select_stmt = "SELECT * FROM member WHERE username = %s;"
        cursor.execute(select_stmt, (username,))
        issigned = cursor.fetchone()
        # print("user sign up: ", issigned)
        if issigned != None:
            print("already signed up")
            return flask.redirect( flask.url_for("errorMessage", message = "signedup"))
        insert_stmt = "INSERT INTO member (name, username, password) VALUES( %s, %s, %s);"
        user_data = (name, username, password)
        cursor.execute(insert_stmt, user_data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return flask.redirect(flask.url_for("index"))

@app.route("/signin", methods=["GET","POST"])
def signin():
    flask.session["SIGNED-IN"] = False
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    if username == "" or password == "":
        return flask.redirect( flask.url_for("errorMessage", message = "empty"))
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor=connection.cursor()
        create_stmt= ("CREATE DATABASE IF NOT EXISTS website")
        cursor.execute(create_stmt)
        cursor.execute("USE website")
        create_stmt= ("""
            CREATE TABLE IF NOT EXISTS member (
                id BIGINT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,    
                password VARCHAR(255) NOT NULL,    
                follower_count INT UNSIGNED NOT NULL DEFAULT 0,    
                time DATETIME NOT NULL DEFAULT NOW())"""
        )
        cursor.execute(create_stmt)
        select_stmt=("SELECT * from member WHERE username = %s")
        data=(username,)
        cursor.execute(select_stmt, data)
        users = cursor.fetchone()
        # print(users)
    finally:
        cursor.close()
        connection.close()
    if users is not None:
        if username == users[2] and password == users[3]:
            flask.session["id"] = users[0]
            flask.session["name"] = users[1]
            flask.session["username"] = users[2]
            flask.session["SIGNED-IN"] = True
            return flask.redirect( flask.url_for("member"))
    return flask.redirect( flask.url_for("errorMessage", message = "invalid"))

@app.route("/member")
def member():
    if flask.session.get("SIGNED-IN") == False or flask.session.get("SIGNED-IN") == None:
        return flask.redirect("/")
    name = flask.session["name"]
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor=connection.cursor()
        cursor.execute("USE website")
        create_stmt= ("""
            CREATE TABLE IF NOT EXISTS message (    
                id BIGINT primary key auto_increment,
                member_id BIGINT NOT NULL,
                content VARCHAR(255) NOT NULL,
                like_count INT UNSIGNED NOT NULL DEFAULT 0,    
                time DATETIME NOT NULL DEFAULT NOW(),
                FOREIGN KEY(member_id) REFERENCES member(id)
                )""")
        cursor.execute(create_stmt)
        select_stmt = "SELECT message.id, member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id ORDER BY message.time DESC;"
        cursor.execute(select_stmt)
        messages = cursor.fetchall()
        print(messages)
    finally:
        cursor.close()
        connection.close()
    return flask.render_template("member.html", name=name, messages=messages)

@app.route("/createMessage", methods =["POST"])
def createMessage():
    if flask.session.get("SIGNED-IN") == False or flask.session.get("SIGNED-IN") == None :
        return flask.redirect("/")
    id = flask.session["id"]
    content = flask.request.form["content"]
    # print("you enter: ",content)
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor=connection.cursor()
        cursor.execute("USE website")
        create_stmt= ("""
            CREATE TABLE IF NOT EXISTS message (    
                id BIGINT primary key auto_increment,
                member_id BIGINT NOT NULL,
                content VARCHAR(255) NOT NULL,
                like_count INT UNSIGNED NOT NULL DEFAULT 0,    
                time DATETIME NOT NULL DEFAULT NOW(),
                FOREIGN KEY(member_id) REFERENCES member(id)
                )""")
        cursor.execute(create_stmt)
        insert_stmt = "INSERT INTO message (member_id, content) VALUES( %s, %s);"
        user_data = (id, content)
        cursor.execute(insert_stmt, user_data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return flask.redirect( flask.url_for("member"))

@app.route("/signout", methods=["GET"])
def signout():
    flask.session["SIGNED-IN"] = False
    return flask.redirect( flask.url_for("index"))

@app.route("/error", methods=["GET"])
def errorMessage():    
    message=flask.request.args.get("message")
    if message == "empty":
        return flask.render_template("error.html", message = "empty")
    if message == "invalid":
        return flask.render_template("error.html", message = "invalid")
    if message =="signedup":
        return flask.render_template("error.html", message = "signedup")

if __name__ == "__main__":
    app.debug=True
    app.run(port=3000)

