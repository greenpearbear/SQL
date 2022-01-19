import use_BD
import json
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/movie/<title>')
def movie_info(title):
    film = use_BD.search_title(title)
    return json.dumps(film, separators=(',', ':'))


@app.route('/movie/<ot>/to/<do>')
def movie_range(ot, do):
    film = use_BD.movie_range(ot, do)
    film = json.dumps(film)
    return jsonify(film)


@app.route('/movie/rating/<rating>')
def movie_rating(rating):
    film = use_BD.rating_see(rating)
    return film


@app.route('/genre/<genre>')
def movie_genre(genre):
    film = use_BD
    return film


if __name__ == '__main__':
    app.run()
