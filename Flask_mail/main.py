
from flask import Flask, render_template, request, flash, redirect

from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "dqstorm92@gmail.com"
app.config['MAIL_PASSWORD'] = "sxcvgeicxuaoeklt"
#app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/send_msg', methods = ['GET', 'POST'])
def send_msg():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        message = Message(subject, sender="dqstorm92@gmail.com", recipients = [email])
        message.body = msg
        mail.send(message)
        success = "Đã gửi!"

        return render_template("result.html", success=success)


if __name__ == "__main__":
    app.run(debug=True)

