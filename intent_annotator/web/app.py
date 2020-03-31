import os
import traceback

from flask import render_template, Flask, request

from intent_annotator.core.annotator import Annotator
from intent_annotator.core.examples import Examples
from intent_annotator.core.workspace import Workspace

app = Flask(__name__)

# Initialize paths
THIS_FILE_PATH = os.path.realpath(__file__)
PACKAGE_PATH = "/".join(THIS_FILE_PATH.split("/")[:-2])
RESOURCES_PATH = PACKAGE_PATH + "/files/"

WORKSPACE_FILE_PATH = RESOURCES_PATH + "workspace.json"

workspace = Workspace()
examples = Examples()
annotator = Annotator(workspace, examples)


@app.route("/", methods=["POST", "GET"])
@app.route("/load_files", methods=["POST", "GET"])
def load_from_file():
    exception = None

    if request.method == "POST":
        try:
            workspace_file = request.files["workspace_fileselect"]
            examples_file = request.files["examples_fileselect"]

            workspace.load(workspace_file.stream)
            examples.load_from_excel(examples_file.stream)

        except Exception as e:
            traceback.print_exc()
            exception = str(e)

    return render_template("load_files.html",
                           exception=exception,
                           load_successful=(exception is None and request.method == "POST"))


@app.route("/annotate", methods=["POST", "GET"])
def annotate():
    exception = None

    return render_template("annotate.html",
                           annotator=annotator,
                           exception=exception)


if __name__ == "__main__":
    app.run(debug=True)
