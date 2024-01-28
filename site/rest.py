from __main__ import app
from flask import request, jsonify
from pipelines.songGen import gen_songs, gen_prompt
from pipelines.summary import summarize_desc
from pipelines.vision import desc_img


@app.route("/songsnapapi/summarise", methods=["POST"])
def summarise_endpoint():
    print(request.json)
    desc = request.json.get("content")
    if desc:
        result = summarize_desc(desc)
        return jsonify({
            "data": result
        })
    return "No provided description", 400

@app.route("/songsnapapi/analyse-image", methods=["POST"])
def analyse_image_endpoint():
    print(request.json)
    url = request.json.get("img_url")
    if url: 
        result = desc_img(url)
        return jsonify({
            "data": result
        })
    return "No provided image URL", 400

    
@app.route("/songsnapapi/generate-songs", methods=["POST"])
def generate_songs_endpoint():
    desc = request.json.get("content")
    if desc:
        result = gen_songs(desc)
        return jsonify({
            "data": result
        })
    return "No provided text", 400

@app.route("/songsnapapi/generate-prompt", methods=["POST"])
def generate_prompt_endpoint():
    text = request.json.get("content")
    songs = request.json.get("songs")
    if text and songs:
        result = gen_prompt(text, songs)
        return jsonify({
            "data": result
        })
    return "No provided text", 400


    
