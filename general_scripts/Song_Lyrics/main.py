import lyricsgenius

api_key = '7YPylu0ku9KdiAv10N9jIXhFN1LzKj1r0FUI'
genius = lyricsgenius.Genius(api_key)

name = input("Enter the artist name: ")
artist = genius.search_artist(name)

song = input("Enter the song name for lyrics: ")
song = artist.song(song)

print(song.lyrics)