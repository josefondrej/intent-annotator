import traceback

from flask import render_template, Flask, request

from intent_annotator.core.annotator import Annotator
from intent_annotator.core.examples import Examples
from intent_annotator.core.workspace import Workspace

app = Flask(__name__)

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

            workspace.load_from_file_storage(workspace_file)
            examples.load_from_file_storage(examples_file)

        except Exception as e:
            traceback.print_exc()
            exception = str(e)

    return render_template("load_files.html",
                           exception=exception,
                           load_successful=(exception is None and request.method == "POST"))


@app.route("/annotate", methods=["POST", "GET"])
def annotate():
    return render_template("annotate.html",
                           annotator=annotator)


if __name__ == "__main__":
    app.run(debug=True)
