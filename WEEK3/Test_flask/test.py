from flask import Flask, redirect, url_for

app = Flask(__name__) #Khởi tạo một app


@app.route('/') #Khởi tạo URL
def hello_world():  #Function thực hiện các thao tác của URL
    return "<h1> Hello flask </h1>"


@app.route('/admin') #Khởi tạo URL
def hello_admin(): #Function thực hiện các thao tác của URL
    return f"<h1> Hello sep dep trai!</h1>"


@app.route('/user/<name>') #Khởi tạo URL
def hello_user(name): #Function thực hiện các thao tác của URL
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f"<h1> Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True) #Khởi chạy Flask