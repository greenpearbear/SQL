import use_BD
from flask import Flask


app = Flask(__name__)


@app.route('/movie/<title>')
def movie_info(title):
    film = use_BD.search_title(title)
    return film


@app.route('/movie/<ot>/to/<do>')
def movie_range(ot, do):
    film = use_BD.movie_range(ot, do)
    return film


if __name__ == '__main__':
    app.run()
