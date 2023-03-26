''' hello.py is a simple webserver '''
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>Hello this wonderful World!</h1>"

@app.route("/info")
def intro_page():
    return "<h1>Introduction</h1> <p>This is a webpage for practicing usign flask</p>"

@app.route("/profile")
def profile():
    return "<p>name: Xu Cai </p><p>Date: 3, 18, 2023</p>"
if __name__=='__main__':
<<<<<<< HEAD
    app.run(debug=True,port=50)
=======
    app.run(debug=True,port=5001)
>>>>>>> 7999cf2a4e005c4f32c489f8264406f096232e75
