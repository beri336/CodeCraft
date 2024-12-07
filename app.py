# app.py

from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for,
)
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.styles import get_all_styles
from utils import take_screenshot_from_url

import json
import base64
import os

def load_secret_key():
    """ Load the secret key for Flask from the config.json file. """
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config["SECRET_KEY"].encode() # convert to bytes

# init Flask app
app = Flask(__name__)
app.secret_key = load_secret_key() #set secret key for session management

# default values
PLACEHOLDER_CODE = "print('HELLO, WORLD!')" # default code snippet
DEFAULT_STYLE = "monokai" # default syntax highlighting style
NO_CODE_FALLBACK = "#No Code Entered" # fallback if no code is provided
DEFAULT_LANGUAGE = "python" # default programming language

@app.route("/", methods=["GET"])
def code():
    """
    Render the code input page. Initializes session values if not set.
    
    Returns:
        HTML: Rendered code input page.
    """
    # init session values
    if session.get("code") is None:
        session["code"] = PLACEHOLDER_CODE
    if session.get("language") is None:
        session["language"] = DEFAULT_LANGUAGE

    # prepare context for template
    lines = session["code"].split("\n")
    lexers = [(lexer[0], lexer[1]) for lexer in get_all_lexers()]
    context = {
        "message": "Paste your Code",
        "code": session["code"],
        "num_lines": len(lines),
        "max_chars": len(max(lines, key=len)),
        "language": session["language"],
        "lexers": lexers
    }

    return render_template("code_input.html", **context)

@app.route("/save_code", methods=["POST"])
def save_code():
    """
    Save code and language settings from the form to the session.

    Returns:
        Redirect: Redirects to the code input page.
    """
    session["code"] = request.form.get("code") or NO_CODE_FALLBACK
    session["language"] = request.form.get("language") or DEFAULT_LANGUAGE

    return redirect(url_for("code"))

@app.route("/reset_session", methods=["POST"])
def reset_session():
    """
    Reset the session to default values.

    Returns:
        Redirect: Redirects to the code input page.
    """
    session.clear()
    session["code"] = PLACEHOLDER_CODE
    session["language"] = DEFAULT_LANGUAGE

    return redirect(url_for("code"))

@app.route("/style", methods=["GET"])
def style():
    """
    Render the style selection page with the current code highlighted.

    Returns:
        HTML: Rendered style selection page.
    """
    if session.get("style") is None:
        session["style"] = DEFAULT_STYLE

    # generate syntax highlighting preview
    formatter = HtmlFormatter(style=session["style"])
    lexer = get_lexer_by_name(session["language"])
    context = {
        "message": "Select Your Style 🍟",
        "all_styles": list(get_all_styles()),
        "style": session["style"],
        "style_definitions": formatter.get_style_defs(),
        "style_bg_color": formatter.style.background_color,
        "highlighted_code": highlight(session["code"], lexer, formatter),
    }

    return render_template("style_selection.html", **context)

@app.route("/save_style", methods=["POST"])
def save_style():
    """
    Save the selected style, code, and language to the session.

    Returns:
        Redirect: Redirects to the style selection page.
    """
    if request.form.get("style") is not None:
        session["style"] = request.form.get("style")
    if request.form.get("code") is not None:
        session["code"] = request.form.get("code") or NO_CODE_FALLBACK
    if request.form.get("language") is not None:
        session["language"] = request.form.get("language") or DEFAULT_LANGUAGE

    return redirect(url_for("style"))

@app.route("/image", methods=["GET"])
def image():
    """
    Generate an image of the highlighted code using a browser screenshot.

    Returns:
        HTML: Rendered page with the image as base64.
    """
    # prepare session data for the screenshot
    session_data = {
        "name": app.config["SESSION_COOKIE_NAME"],
        "value": request.cookies.get(app.config["SESSION_COOKIE_NAME"]),
        "url": request.host_url,
    }
    target_url = request.host_url + url_for("style")

    # generate screenshot of the style page
    image_bytes = take_screenshot_from_url(target_url, session_data)
    context = {
        "message": "DONE! 🎉",
        "image_b64": base64.b64encode(image_bytes).decode("utf-8"),
    }

    return render_template("image.html", **context)

if __name__ == "__main__":
    # run the app in debug mode on all network interfaces
    app.run(debug=True, host='0.0.0.0', port=8080)