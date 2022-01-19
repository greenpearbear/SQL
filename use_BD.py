import sqlite3
import json


def search_title(word):
    list_key_dict = ["title", "country", "release_year", "genre", "description"]
    dict_search = {}
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT `title`, `country`, `release_year`, `listed_in`, `description`
    FROM netflix 
    WHERE `title` LIKE ? AND type = 'Movie'
    ORDER BY `date_added` 
    DESC LIMIT 1
    """
    cur.execute(sqlite_query, ('%'+word+'%',))
    list_sql = cur.fetchall()
    for key, value in enumerate(list_key_dict):
        dict_search.update({f'{value}': f'{list_sql[0][key]}'})
    con.close()
    return json.dumps(dict_search, separators=(',', ':'), indent=4)


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
    return json.dumps(list_data_return, separators=(',', ':'), indent=4)


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
    list_sql = cur.fetchall()
    list_data_return = []
    for i in list_sql:
        list_data_return.append(dict({'title': i[0], 'rating': i[1], 'description': i[2]}))
    return json.dumps(list_data_return, separators=(',', ':'), indent=4)


def genre_search(genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = """
    SELECT `title`, `description`
    FROM netflix 
    WHERE `listed_in` LIKE ? AND `type` = 'Movie'
    ORDER BY `date_added` 
    DESC LIMIT 10
    """
    params = ('%'+genre+'%',)
    cur.execute(sqlite_query, params)
    list_sql = cur.fetchall()
    list_data_return = []
    for i in list_sql:
        list_data_return.append(dict({'title': i[0], 'description': i[1]}))
    con.close()
    return json.dumps(list_data_return, separators=(',', ':'), indent=4)


def two_actors_search(one, two):
    list_all_actors = []
    actor_dict = {}
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = """
        SELECT `cast`
        FROM netflix 
        WHERE `cast` LIKE ? AND `cast` LIKE ?
        ORDER BY `date_added` 
        DESC LIMIT 10
        """
    params = ('%'+one+'%', '%'+two+'%')
    cur.execute(sqlite_query, params)
    list_sql = cur.fetchall()
    for index_list in list_sql:
        for index_tuple in index_list:
            list_actor = index_tuple.split(', ')
            for actor in list_actor:
                if actor not in actor_dict.keys():
                    actor_dict.update({f'{actor}': 1})
                else:
                    actor_dict.update({f'{actor}': actor_dict[f'{actor}'] + 1})
    for key in actor_dict:
        if actor_dict[key] > 2 and key != one and key != two:
            list_all_actors.append(key)
    return list_all_actors
