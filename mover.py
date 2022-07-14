import os

class Movie:
    def __init__(self, movieTitle, encodedPath, destinationPath) -> None:
        self.movieTitle = movieTitle
        self.encodedPath = encodedPath
        self.destinationPath = destinationPath

movie1 = Movie('Movie 3 (2003).mkv', '/xome/encoded/path', '/some/destination/path')

print(movie1.movieTitle)