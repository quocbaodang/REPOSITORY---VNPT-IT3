from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" #Dùng để validate email

app = Flask(__name__) # Khởi tạo

# Config các thông số để gửi mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "dqstorm92@gmail.com"
app.config['MAIL_PASSWORD'] = "sxcvgeicxuaoeklt"
#app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True

mail = Mail(app) #Khởi tạo mail

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/send_msg', methods = ['GET', 'POST'])
def send_msg():
    if request.method == "POST":
        #Lấy dữ liệu từ html
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        #is_valid = validate_email('example@gmail.com', verify = True)

        #if is_valid:
        # Validate email
        if re.search(email_condition, email):
            message = Message(subject, sender="dqstorm92@gmail.com", recipients = [email])
            message.body = msg
            mail.send(message)
            success = "Đã gửi!"
            return render_template("result.html", success=success)
        else:
            fail = "Error!"
            return render_template("fail.html", fail=fail)

if __name__ == "__main__":
    app.run(debug=True)

