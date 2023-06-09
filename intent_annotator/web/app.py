import traceback
import uuid

from flask import render_template, Flask, request, session

from intent_annotator.core.annotator import Annotator
from intent_annotator.core.examples import Examples
from intent_annotator.core.workspace import Workspace

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())


@app.route("/", methods=["POST", "GET"])
@app.route("/load_files", methods=["POST", "GET"])
def load_from_file():
    exception = None

    if request.method == "POST":
        try:
            workspace_file = request.files["workspace_fileselect"]
            examples_file = request.files["examples_fileselect"]

            id = str(uuid.uuid4())
            workspace = Workspace(id=id)
            examples = Examples(id=id)

            workspace.load_from_file_storage(workspace_file)
            examples.load_from_file_storage(examples_file)

            workspace.dump_jsonpickle()
            examples.dump_jsonpickle()

            session["session_id"] = id


        except Exception as e:
            traceback.print_exc()
            exception = str(e)

    return render_template("load_files.html",
                           exception=exception,
                           load_successful=(exception is None and request.method == "POST"))


@app.route("/annotate", methods=["POST", "GET"])
def annotate():
    ANNOTATION_ID_PREFIX = "intent_annotation_";

    workspace_updated = False
    annotator = None

    try:
        id = session["session_id"]

        workspace = Workspace.load_jsonpickle(id)
        examples = Examples.load_jsonpickle(id)

        annotator = Annotator(workspace, examples)

        if request.method == "GET":
            for example_id, example in enumerate(annotator.examples):
                example_intent = request.args.get(ANNOTATION_ID_PREFIX + str(example_id), "")
                example_intent = example_intent.strip()
                if len(example_intent) > 0:
                    annotator.annotate_example(example, example_intent)
                    workspace_updated = True

            if workspace_updated:
                annotator.dump_workspace()
                annotator.dump_workspace_jsonpickle()
    except:
        pass

    return render_template("annotate.html",
                           annotator=annotator,
                           workspace_updated=workspace_updated)


if __name__ == "__main__":
    app.run(debug=True, )
