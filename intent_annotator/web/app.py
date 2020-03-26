import os
import traceback

from flask import render_template, Flask, request

app = Flask(__name__)

# Initialize paths
THIS_FILE_PATH = os.path.realpath(__file__)
PACKAGE_PATH = "/".join(THIS_FILE_PATH.split("/")[:-2])
RESOURCES_PATH = PACKAGE_PATH + "/files/"

WORKSPACE_FILE_PATH = RESOURCES_PATH + "workspace.json"
EXAMPLES_FILE_PATH = RESOURCES_PATH + "examples.csv"


@app.route("/", methods=["POST", "GET"])
@app.route("/load_files", methods=["POST", "GET"])
def load_from_file():
    exception = None

    if request.method == "POST":
        try:
            workspace = request.files["workspace_fileselect"]
            examples = request.files["examples_fileselect"]

            if not workspace:
                exception = "Workspace file missing."

            if not examples:
                exception = "Examples file missing."

            workspace.save(WORKSPACE_FILE_PATH)
            examples.save(EXAMPLES_FILE_PATH)

        except exception as e:
            traceback.print_exc()
            exception = str(e.message)

    return render_template("load_files.html",
                           exception=exception,
                           load_successful=(exception is None and request.method == "POST"))


@app.route("/annotate")
def annotate():
    return render_template("annotate.html")


if __name__ == "__main__":
    app.run(debug=True)
