from flask import Flask, redirect, url_for, render_template, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import json
from os import environ as env
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from urllib.parse import quote_plus, urlencode
from werkzeug.security import check_password_hash, generate_password_hash
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


@app.route("/")
def homepage():

    if session.get("user"):
        print(json.dumps(session.get("user")))
        return redirect("/albums")
    else:
        return redirect("/login")

@app.route("/login")
def login():
    return render_template("index.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.route("/loginform")
def login_page():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("homepage", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


@app.route("/albums")
def albums():
    return render_template("albums.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

@app.route("/album")
def album_single():
    return render_template("album_single.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
