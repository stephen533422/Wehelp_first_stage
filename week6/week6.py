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
            password="1234",
            database="website"
        )
        cursor = connection.cursor()
        select_stmt = "SELECT * FROM member WHERE username = %s;"
        cursor.execute(select_stmt, (username,))
        issigned = cursor.fetchone()
        # print("user sign up: ", issigned)
        if issigned != None:
            print("already signed up")
            return flask.redirect( flask.url_for("errorMessage", message = "signedup"))
        else:
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
            password="1234",
            database="website"
        )
        cursor=connection.cursor(dictionary=True)
        select_stmt=("SELECT * from member WHERE username = %s")
        data=(username,)
        cursor.execute(select_stmt, data)
        users = cursor.fetchone()
        # print(users)
    finally:
        cursor.close()
        connection.close()
    if users is not None:
        if username == users["username"] and password == users["password"]:
            flask.session["id"] = users["id"]
            flask.session["name"] = users["name"]
            flask.session["username"] = users["username"]
            flask.session["SIGNED-IN"] = True
            return flask.redirect( flask.url_for("member"))
    return flask.redirect( flask.url_for("errorMessage", message = "invalid"))

@app.route("/member")
def member():
    if flask.session.get("SIGNED-IN") == False or flask.session.get("SIGNED-IN") == None:
        return flask.redirect("/")
    id = flask.session["id"]
    name = flask.session["name"]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="website"
        )
        cursor=connection.cursor(dictionary=True)
        select_stmt = "SELECT message.id, message.member_id, member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id ORDER BY message.time DESC;"
        cursor.execute(select_stmt)
        messages = cursor.fetchall()
        # print(messages)
    finally:
        cursor.close()
        connection.close()
    return flask.render_template("member.html", member_id=id, member_name=name, messages=messages)

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
            password="1234",
            database="website"
        )
        cursor=connection.cursor()
        insert_stmt = "INSERT INTO message (member_id, content) VALUES( %s, %s);"
        user_data = (id, content)
        cursor.execute(insert_stmt, user_data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return flask.redirect( flask.url_for("member"))

@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    if flask.session.get("SIGNED-IN") == False or flask.session.get("SIGNED-IN") == None :
        return flask.redirect("/")
    message_id = flask.request.form["message_id"]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="website"
        )
        cursor=connection.cursor()
        delete_stmt = "DELETE FROM message WHERE id = %s"
        data = (message_id,)
        cursor.execute(delete_stmt, data)
        alter_stmt ="ALTER TABLE message AUTO_INCREMENT = 0"
        cursor.execute(alter_stmt)
        '''alter_stmt ="ALTER TABLE message DROP id"
        cursor.execute(alter_stmt)
        alter_stmt ="ALTER TABLE message ADD id BIGINT PRIMARY KEY AUTO_INCREMENT first"
        cursor.execute(alter_stmt)'''
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

