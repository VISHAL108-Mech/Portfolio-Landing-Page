"""Flask app for serving a simple personal name-card landing page."""

from flask import Flask, render_template

# Create the Flask application instance used to serve the webpage.
server = Flask(__name__)


@server.route("/")
def home():
    """Render the homepage for the personal portfolio/name card."""
    return render_template("index.html")


if __name__ == "__main__":
    # Run the app in debug mode so changes are reloaded automatically.
    server.run(debug=True)
