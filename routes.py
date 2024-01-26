from flask import render_template


@app.route("/")
def landing():
    return render_template('landing.html')