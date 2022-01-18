import sqlite3


def search_title(word):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT `title`, `country`, `release_year`, `listed_in`, `description` " \
                   f"FROM netflix WHERE `title` LIKE '%{word}%' ORDER BY `date_added` DESC LIMIT 1"
    cur.execute(sqlite_query)
    list_key_dict = ["title", "country", "release_year", "genre", "description"]
    dict_search = {}
    list_sql = cur.fetchall()
    for key, value in enumerate(list_key_dict):
        dict_search.update({f'{value}': f'{list_sql[0][key]}'})
    con.close()
    return dict_search


def movie_range(ot, do):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT `title`, `release_year` " \
                   f"FROM netflix WHERE `release_year` BETWEEN ? AND  ?" \
                   f"ORDER BY `release_year` LIMIT 100"
    params = (ot, do)
    cur.execute(sqlite_query, params)
    list_sql = cur.fetchall()
    list_data_return = []
    for i in list_sql:
        list_data_return.append(dict({'title': i[0], 'release_year': i[1]}))
    con.close()
    return str(list_data_return)
