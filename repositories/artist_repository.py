from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def get_albums(artist):
    albums = []
    artist_id = artist.id
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist_id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)

    return albums

def save(artist):
    sql = "INSERT INTO artists (name ) VALUES (%s) RETURNING *"
    values = [artist.name] 
    results =run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETED FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select(id):
    artist = None
    sql = "SELECT * FROM artists where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist(result['name'], result['id'] )
    return artist


