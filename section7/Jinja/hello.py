from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def jinja_intro():
    return render_template(
        "jinja_intro.html", name="Nathan Webb", template_name="Jinja2"
    )

@app.route("/first")
def hello_world():
    return render_template("first_page.html")

@app.route("/second")
def hello_world_fancy():
    return render_template("second_page.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')