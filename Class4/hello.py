from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name="".title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK"

@app.route("/hi")
def hi():
    return "Hi"

@app.route("/bye")
def bye():
    return "Bye"

app.run(debug=True)