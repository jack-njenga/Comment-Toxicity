#!/usr/bin/env python3
"""
app
"""
from flask import Flask, render_template, request, abort, jsonify

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def homepage():
    """
    home page
    """
    return render_template("index.html")

@app.route("/about", strict_slashes=False)
def about_us():
    """
    About us page
    """
    return render_template("about_us.html")

@app.route("/contact", strict_slashes=False)
def contact_us():
    """
    contact us page
    """
    return render_template("contact_us.html")

@app.route("/help", strict_slashes=False)
def help():
    """
    help page
    """
    return render_template("help.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
