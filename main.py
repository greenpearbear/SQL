import use_BD
from flask import Flask


app = Flask(__name__)


@app.route('/movie/<title>')
def movie_info(title):
    film = use_BD.search_title(title)
    return film




if __name__ == '__main__':
    app.run()
