# main.py

"""
CodeCraft - Create Beautiful Code Snippets
A Flask web application for syntax highlighting and code snippet generation.
"""

from flask import (
    Flask, 
    render_template, 
    session, 
    redirect, 
    request, 
    url_for
)
from config import (
    load_secret_key,
    PLACEHOLDER_CODE,
    DEFAULT_STYLE,
    DEFAULT_LANGUAGE,
    DEBUG,
    HOST,
    PORT,
)

import os
import socket

# Import services
from services import code_service
from services import style_service
from services import image_service


# Initialize Flask app
app = Flask(
    __name__,
    template_folder="src/templates",
    static_folder="src/static"
)
app.secret_key = load_secret_key()


@app.route("/", methods=["GET"])
def code():
    """Render code input page with session initialization."""
    if session.get("code") is None:
        session["code"] = PLACEHOLDER_CODE
    if session.get("language") is None:
        session["language"] = DEFAULT_LANGUAGE

    context = code_service.prepare_code_context(session["code"], session["language"])
    return render_template("code_input.html", **context)


@app.route("/save_code", methods=["POST"])
def save_code():
    """Save code and language from form to session."""
    session["code"] = code_service.validate_code_input(request.form.get("code", ""))
    session["language"] = request.form.get("language", DEFAULT_LANGUAGE)
    return redirect(url_for("code"))


@app.route("/reset_session", methods=["POST"])
def reset_session():
    """Reset session to default values."""
    session.clear()
    session["code"] = PLACEHOLDER_CODE
    session["language"] = DEFAULT_LANGUAGE
    return redirect(url_for("code"))


@app.route("/style", methods=["GET"])
def style():
    """Render style selection page with highlighted code preview."""
    if session.get("style") is None:
        session["style"] = DEFAULT_STYLE

    context = style_service.prepare_style_context(
        session["code"],
        session["language"],
        session["style"]
    )
    return render_template("style_selection.html", **context)


@app.route("/save_style", methods=["POST"])
def save_style():
    """Save style, code, and language to session."""
    if request.form.get("style"):
        session["style"] = request.form.get("style")
    if request.form.get("code"):
        session["code"] = code_service.validate_code_input(request.form.get("code"))
    if request.form.get("language"):
        session["language"] = request.form.get("language")

    return redirect(url_for("style"))


@app.route("/image", methods=["GET"])
def image():
    """Generate and display code screenshot."""
    try:
        style_url = request.host_url.rstrip("/") + url_for("style", _external=False)
        image_b64 = image_service.generate_code_screenshot(request, style_url)

        if not image_b64:
            return redirect(url_for("style"))

        context = image_service.prepare_image_context(image_b64)
        return render_template("image.html", **context)

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return redirect(url_for("style"))


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return redirect(url_for("code"))


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    print(f"❌ Server error: {error}")
    return redirect(url_for("code"))

# use the server on mobile devices in the same network
def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return "localhost"

def print_startup_info(host, port, local_ip):
    """Print beautiful startup information."""
    print("\n" + "="*60)
    print("🚀 CodeCraft Server Started")
    print("="*60)
    print(f"💻 Local access:    http://localhost:{port}")
    print(f"📱 Mobile access:   http://{local_ip}:{port}")
    print(f"🌐 Network access:  http://{local_ip}:{port}")
    print("="*60 + "\n")

if __name__ == "__main__":
    #PORT = int(os.getenv("PORT", 8080))
    LOCAL_IP = get_local_ip()
    
    print_startup_info(HOST, PORT, LOCAL_IP)
    
    app.run(debug=DEBUG, host=HOST, port=PORT)
