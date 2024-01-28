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

oauth.register(
    'spotify',
    client_id=env.get("CLIENT_ID"),
    client_secret=env.get("CLIENT_SECRET"),
    request_token_params={
        'scope': 'user-read-email',
        "redirect_uri": "http://localhost:5000/callback",
        "response_type": "code",
        "client_id": env.get("CLIENT_ID"),
        "client_secret": env.get("CLIENT_SECRET")
    },
    base_url='https://api.spotify.com/v1/',
    access_token_method='POST',
    redirect_uri="http://localhost:5000/callback",
    access_token_url='https://accounts.spotify.com/api/token',
    authorize_url='https://accounts.spotify.com/authorize'
)


from rest import *


@app.route("/")
def homepage():
    if session.get("user"):
        return redirect("/albums")
    else:
        return redirect("/login")

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True, provider="auth0")
    )

@app.route("/login/spotify")
def login_spotify():
    return oauth.spotify.authorize_redirect(
        redirect_uri=url_for("callback", _external=True, provider="spotify")
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    provider = request.args.get("provider")
    if provider == "spotify":
        token = oauth.spotify.authorize_access_token()
        session["spotify-user"] = token
        return redirect("/")
    else:
        token = oauth.auth0.authorize_access_token()
        session["user"] = token
        return redirect("/login/spotify")



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
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
