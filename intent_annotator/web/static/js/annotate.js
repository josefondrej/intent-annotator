var ANNOTATION_ID_PREFIX = "intent_annotation_";

class Annotator {
    constructor(intents) {
        this._intents = intents;
        this._getNextId("ArrowUp");
        this._init();
    }

    _init() {
        var that = this;
        document.addEventListener("keydown", function (event) {
            if (["ArrowRight", "ArrowLeft"].includes(event.key)) {
                    let nextId = that._getNextId(event.key);
                    $("#" + nextId).focus();
                }
            }
        );

        var inputs = $("input[id^=" + ANNOTATION_ID_PREFIX + "]");
        inputs.autocomplete({
            source: that._intents,
            autoFocus: true,
            delay: 0,
            minLength: 0
        });

        inputs.focusout(function () {
            // console.log("FocusOut")
            if ($(this).val().trim() != "") {
                $(this).addClass("highlited_annotation");
                $(this).css({"border": "none"});
            } else {
                $(this).removeClass("highlited_annotation");
                $(this).removeAttr("style");
            }
        });
    }

    _intToAnnotationId(index) {
        return ANNOTATION_ID_PREFIX + index;
    }

    _annotationIdToInt(elementId) {
        let strIndex = elementId.substring(ANNOTATION_ID_PREFIX.length);
        let index = parseInt(strIndex);
        return index;
    }

    _getCurrentFocusIndex() {
        let focusedId = document.activeElement.getAttribute("id");
        if (focusedId == null) {
            return 0;
        }
        if (!focusedId.startsWith(ANNOTATION_ID_PREFIX)) {
            return 0;
        }
        return this._annotationIdToInt(focusedId);
    }

    _getNextId(arrow) {
        let currentIndex = this._getCurrentFocusIndex();
        let nextIndex = null;
        switch (arrow) {
            case "ArrowLeft":
                nextIndex = Math.max(currentIndex - 1, 0);
                break;
            case "ArrowRight":
                nextIndex = Math.min(currentIndex + 1, this._intents.length)
                break;
        }
        let nextId = this._intToAnnotationId(nextIndex);
        return nextId;
    }
}
