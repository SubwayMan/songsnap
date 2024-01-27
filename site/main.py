from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return redirect(url_for("login_page"))

@app.route("/login")
def login_page():
    return render_template("index.html")

@app.route("/albums")
def albums():
    return render_template("albums.html")

@app.route("/album")
def album_single():
    return render_template("album_single.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
