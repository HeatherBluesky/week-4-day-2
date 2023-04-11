from db.run_sql import run_sql
from repositories import artist_repository
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id] 
    results =run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = row['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(row['title'],row['genre'], artist, row['id'] )
        albums.append(album)
    return albums 


def delete_all():
    sql = "DELETE FROM album"
    run_sql(sql)


def delete(id):
    sql = "DELETED FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


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

def update (album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

