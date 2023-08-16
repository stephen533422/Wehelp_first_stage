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

@app.route("/api/member", methods=["GET"])
def apiMember():
    username=flask.request.args.get("username")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="website"
        )
        cursor=connection.cursor(dictionary=True)
        select_stmt = "SELECT * FROM member WHERE username = %s;"
        cursor.execute(select_stmt, (username,))
        userdata = cursor.fetchone()
        if userdata != None and flask.session.get("SIGNED-IN") == True:
            data={"id":userdata["id"], "name":userdata["name"], "username":userdata["username"]}
            return_data={"data":data}
        else:
            data=None
            return_data={"data":data}
    finally:
        cursor.close()
        connection.close()
    return flask.jsonify(return_data)

@app.route("/api/member", methods=["PATCH"])
def changeName():
    if flask.session.get("SIGNED-IN") == False or flask.session.get("SIGNED-IN") == None :
        return_data={"error":True}
        return flask.jsonify(return_data)
    newname=flask.request.get_json().get("name")
    username=flask.session.get("username")
    data={"name":newname, "username":username}
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="website"
        )
        cursor=connection.cursor(dictionary=True)
        update_stmt = "UPDATE member SET name = %(name)s WHERE username = %(username)s;"
        cursor.execute(update_stmt, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return_data={"ok":True}
    return flask.jsonify(return_data)

if __name__ == "__main__":
    app.debug=True
    app.run(port=3000)

