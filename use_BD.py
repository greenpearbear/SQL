import sqlite3


def search_title(word):
    list_key_dict = ["title", "country", "release_year", "genre", "description"]
    dict_search = {}
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT `title`, `country`, `release_year`, `listed_in`, `description`
    FROM netflix 
    WHERE `title` 
    LIKE ? ORDER 
    BY `date_added` 
    DESC LIMIT 1
    """
    cur.execute(sqlite_query, ('%'+word+'%',))
    list_sql = cur.fetchall()
    for key, value in enumerate(list_key_dict):
        dict_search.update({f'{value}': f'{list_sql[0][key]}'})
    con.close()
    return dict_search


def movie_range(ot, do):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT `title`, `release_year`
    FROM netflix 
    WHERE `type` = 'Movie' AND `release_year` BETWEEN ? AND  ?
    ORDER BY `release_year` LIMIT 100
    """
    params = (ot, do)
    cur.execute(sqlite_query, params)
    list_sql = cur.fetchall()
    list_data_return = []
    for i in list_sql:
        list_data_return.append(dict({'title': i[0], 'release_year': i[1]}))
    con.close()
    return str(list_data_return)


def rating_see(rating):
    dict_rating = {"children": ['G'],
                   "family": ['G', 'PG', 'PG-13'],
                   "adult": ['R', 'NC-17']}
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT `title`, `rating`, `description` " \
                   f"FROM netflix WHERE `rating` IN ({','.join(['?']*len(dict_rating[rating]))})" \
                   f"ORDER BY `release_year`"
    cur.execute(sqlite_query, dict_rating[rating])
    return str(cur.fetchall())
