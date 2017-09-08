from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=['POST','GET'])
def process():
    return render_template("success.html")
    name = request.form["name"]
    return redirect(url_for("/"))

app.run(debug=True)
