class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title):
        self.songs.append(title)

    def remove_song(self, title):
        if title in self.songs:
            self.songs.remove(title)
        else:
            print(f"'{title}' is not in {self.name}, cannot remove.")

    def show_songs(self):
        print(f"{self.name}: {self.songs}")


playlist_a = Playlist("Workout Mix")
playlist_b = Playlist("Chill Vibes")

playlist_a.add_song("Eye of the Tiger")
playlist_a.add_song("Stronger")

playlist_b.add_song("Weightless")
playlist_b.add_song("Clair de Lune")

playlist_a.show_songs()
playlist_b.show_songs()

playlist_a.remove_song("Nonexistent Song")
playlist_a.remove_song("Stronger")
playlist_a.show_songs()
