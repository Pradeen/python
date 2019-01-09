from flask import Flask
from flask import request, jsonify
from flask import render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html")
@app.route("/createOrders",  methods=['GET', 'POST','DELETE', 'PATCH'])
def createOrder():
    return "ordpyters are created sucessfully"
@app.route("/home",methods=['GET'])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=9090)