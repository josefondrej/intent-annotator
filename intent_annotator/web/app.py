from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
@app.route("/load_files")
def load_from_file():
    return render_template("load_files.html")


@app.route("/annotate")
def annotate():
    return render_template("annotate.html")


if __name__ == "__main__":
    app.run(debug=True)
