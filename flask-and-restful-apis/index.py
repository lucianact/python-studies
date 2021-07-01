from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/greet")
def greet():
    data = request.args.get("name")
    return render_template("hello.html", name=data)


if __name__ == "__main__":
    app.run(debug=True)

