class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count= {}
    
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(self.artist)
        Song.genres.append(self.genre)
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1