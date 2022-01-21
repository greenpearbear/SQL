import use_BD
from flask import Flask
from json2html import *


app = Flask(__name__)


@app.route('/movie/<title>')
def movie_info(title):
    film = use_BD.search_title(title)
    return json2html.convert(film)


@app.route('/movie/<ot>/to/<do>')
def movie_range(ot, do):
    film = use_BD.movie_range(ot, do)
    return json2html.convert(film)


@app.route('/movie/rating/<rating>')
def movie_rating(rating):
    film = use_BD.rating_see(rating)
    return json2html.convert(film)


@app.route('/genre/<genre>')
def movie_genre(genre):
    film = use_BD.genre_search(genre)
    return json2html.convert(film)


if __name__ == '__main__':
    app.run()
