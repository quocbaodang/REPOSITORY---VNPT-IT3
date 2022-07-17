
import email
from flask import Flask, render_template, request
from flask_mail import Mail, Message
import sqlite3 as sql

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "dqstorm92@gmail.com"
app.config['MAIL_PASSWORD'] = "sxcvgeicxuaoeklt"
#app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

#Them nhan vien
@app.route('/create')
def create_employee():
    return render_template('create.html')

@app.route('/addemploy', methods= ['POST', 'GET'])
def addemploy():
    if request.method == 'POST':
        try:
            name = request.form['name']
            cccd = request.form['cccd']
            email = request.form['email']
            sdt = request.form['sdt']

            if name != "" and cccd != "" and email != "" and sdt != "":
                with sql.connect("employees.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO NHANVIEN (tenNhanVien,cccd,email,phone) VALUES (?,?,?,?)", (name,cccd,email,sdt))
                    con.commit()
                    msg = "success"
            else: msg = "error!"

            #Gui mail
            if msg == "success":
                subject = "Đã thêm vào danh sách"
                m = "Chúng tôi đã thêm bạn vào danh sách nhân viên thành công!"
                message = Message(subject, sender="dqstorm92@gmail.com", recipients = [email])
                message.body = m
                mail.send(message)  

        except:
            con.rollback()
            msg = "error!"

        finally:   
            return render_template("result.html", msg=msg)
            con.close()

#Hien thi danh sach nhan vien
@app.route('/list', methods = ['GET'])
def list():
    if request.method == "GET":
        con = sql.connect("employees.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from NHANVIEN")
        rows = cur.fetchall()

        return render_template("list.html", rows=rows)

#Thông tin nhan vien
@app.route('/infor')
def infor():
    return render_template("infor.html")

@app.route('/inforemploy', methods = ['GET', 'POST'])
def inforemploy():
    id = request.form['id']
    con = sql.connect("employees.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from NHANVIEN WHERE idNhanVien = ?", (id))
    rows = cur.fetchall()

    return render_template("infor.html", rows=rows)

#Cap nhat nhan vien
@app.route('/update')
def update():
    con = sql.connect("employees.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from NHANVIEN")
    rows = cur.fetchall()

    return render_template("update.html", rows = rows)

@app.route('/updateemploy', methods = ['POST', 'PUT'])
def updateemploy():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        cccd = request.form['cccd']
        email = request.form['email']
        sdt = request.form['sdt']
        msg = "Nothing"

        with sql.connect("employees.db") as con:
            if name != "":
                cur = con.cursor()
                cur.execute("UPDATE NHANVIEN SET tenNhanVien = ? WHERE idNhanVien=?", (name, id))
                con.commit()
                msg = "Updated!"

            if cccd != "":
                cur = con.cursor()
                cur.execute("UPDATE NHANVIEN SET cccd = ? WHERE idNhanVien=?", (cccd, id))
                con.commit()
                msg = "Updated!"

            if email != "":
                cur = con.cursor()
                cur.execute("UPDATE NHANVIEN SET email = ? WHERE idNhanVien=?", (email, id))
                con.commit()
                msg = "Updated!"

            if sdt != "":
                cur = con.cursor()
                cur.execute("UPDATE NHANVIEN SET phone = ? WHERE idNhanVien=?", (sdt, id))
                con.commit()
                msg = "Updated!"

        return render_template("result.html", msg = msg)

#Xoa nhan vien
@app.route('/remove')
def remove():
    con = sql.connect("employees.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from NHANVIEN")
    rows = cur.fetchall()

    return render_template("remove.html", rows = rows)

@app.route('/removeemploy', methods = ['POST'])
def removeemploy():
    id = request.form['id']
    with sql.connect("employees.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM NHANVIEN WHERE idNhanVien=?", (id))
        con.commit()
        msg = "Deleted!"
    return render_template("result.html", msg = msg)

if __name__=='__main__':
    app.run(debug=True)