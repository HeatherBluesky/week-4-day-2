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