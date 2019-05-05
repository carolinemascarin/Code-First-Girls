from flask import Flask, render_template, request

app = Flask("MyApp")


@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/")
def hello():
    return hello_someone("")


@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    print(email)
    return "All OK, " +email

@app.route("/hi")
def hi():
    return "Hi"

@app.route("/bye")
def bye():
    return "Bye"

app.run(debug=True)