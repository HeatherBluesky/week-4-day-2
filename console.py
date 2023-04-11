import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository  

artist_1 = Artist("Kate Bush")
artist_repository.save(artist_1)

artist_2 = Artist("Childish Gambino")
artist_repository.save(artist_2)

album_1 = Album("Hounds of Love", "pop", artist_1)
album_repository.save(album_1)

album_2 = Album("Awaken My Love", "hip-hop", artist_2)
album_repository.save(album_2)


results = artist_repository.get_albums(artist_1)

for result in results:
    print(result.__dict__)

album_2.genre = "rap"
album_repository.update(album_2)
updated_albums = album_repository.select_all()
for row in updated_albums:
    print(row.__dict__)