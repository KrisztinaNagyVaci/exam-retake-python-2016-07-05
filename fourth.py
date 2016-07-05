class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.rate_list = []

    def rate(self, rating):
        if rating <= 5 and rating >= 1:
            self.rate_list.append(rating)
        else:
            raise ValueError

    def get_average_rating(self):
        average = 0
        summa = 0
        for number in self.rate_list:
            summa += number
        average = summa / len(self.rate_list)
        return average

class Jukebox(object):
    def __init__(self, list_of_songs):
        self.list_of_songs = list_of_songs

    def rate(self, title, rating):
        for song in self.list_of_songs:
            if song.title == title:
                song.rate(rating)

    def get_song_titles_by_artist(self, artist):
        list_of_titles = []
        for song in self.list_of_songs:
            if song.artist == artist:
                list_of_titles.append(song.title)
        return list_of_titles

    def get_top_rated_title(self):
        for song in self.list_of_songs:
            if song.get_average_rating() == 5:
                return song.title


song1 = Song('cool_title', 'cool_author')
song2 = Song('extrasuper_title', 'extrasuper_author')
print(song1.rate(5))
print(song1.rate(4))
print(song1.get_average_rating())
song2.rate(5)

budapestJukebox = Jukebox([song1, song2])
budapestJukebox.rate('cool_title', 4)
print(budapestJukebox.get_song_titles_by_artist('cool_author'))
print(budapestJukebox.get_top_rated_title())
