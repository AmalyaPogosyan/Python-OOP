from read_json import data

class Movie:
    def __init__(self, Released_Year, Runtime, Genre, IMDB_Rating, Director, Star1, Star2, Star3, Star4, Gross, Name):
        self.released_year = Released_Year
        self.runtime = Runtime
        self.genre = Genre.split(', ') if isinstance(Genre, str) else []
        self.imdb_rating = IMDB_Rating
        self.director = Director
        self.actors = [star for star in [Star1, Star2, Star3, Star4] if star] 
        self.gross = Gross
        self.name = Name

    def __repr__(self):
        return (f"--- Movie: '{self.name}' ---\n"
                f"Director: {self.director}\n"
                f"Released Year: {self.released_year}\n"
                f"Main Actors: {' *** '.join(self.actors) if self.actors else 'Unknown'}")

    def get_actors(self):
        return f"--- '{self.name}' actors are ---\n     " + "\n     ".join(self.actors)

    def get_duration(self):
        return self.runtime


class Actor:
    def __init__(self, name):
        self.name = name
        self.movies = [movie for movie in movies if self.name in movie.actors]

    def amount_films(self):
        return len(self.movies)

    def average_rating(self):
        if not self.movies:
            return f"{self.name} has no movies."
        return f"{self.name}'s average rating is {sum(movie.imdb_rating for movie in self.movies) / len(self.movies):.2f}"

    def popular_genre(self):
        if not self.movies:
            return f"{self.name} has not acted in any films."
        genre_count = {}
        for movie in self.movies:
            for genre in movie.genre:
                genre_count[genre] = genre_count.get(genre, 0) + 1
        common_genre = max(genre_count, key=genre_count.get, default='Unknown')
        return f"{self.name} mainly played in '{common_genre}' genre."

    def common_director(self):
        if not self.movies:
            return f"{self.name} has not acted in any films."
        director_count = {}
        for movie in self.movies:
            director_count[movie.director] = director_count.get(movie.director, 0) + 1
        common_director = max(director_count, key=director_count.get, default='Unknown')
        return f"{self.name} mainly worked with director '{common_director}'."

    def common_actor(self):
        if not self.movies:
            return f"{self.name} has not acted in any films."
        co_actor_count = {}
        for movie in self.movies:
            for actor in movie.actors:
                if actor != self.name:
                    co_actor_count[actor] = co_actor_count.get(actor, 0) + 1
        common_actor = max(co_actor_count, key=co_actor_count.get, default='Unknown')
        return f"{self.name} mainly played with '{common_actor}'."

    def __repr__(self):
        return (f"Actor: {self.name}\n"
                f"Played in {self.amount_films()} films.\n"
                f"{self.average_rating()}\n")


class Genre:
    def __init__(self, name):
        self.name = name
        self.movies = [movie for movie in movies if self.name in movie.genre]

    def amount_films(self):
        return len(self.movies)

    def average_rating(self):
        if not self.movies:
            return f"No movies in the '{self.name}' genre."
        return f"'{self.name}' genre average rating is {sum(movie.imdb_rating for movie in self.movies) / len(self.movies):.2f}"

    def common_director(self):
        if not self.movies:
            return f"No movies found in the '{self.name}' genre."
        director_count = {}
        for movie in self.movies:
            director_count[movie.director] = director_count.get(movie.director, 0) + 1
        common_director = max(director_count, key=director_count.get, default='Unknown')
        return f"'{self.name}' genre is mainly directed by {common_director}."

    def common_actor(self):
        if not self.movies:
            return f"No movies found in the '{self.name}' genre."
        actor_count = {}
        for movie in self.movies:
            for actor in movie.actors:
                actor_count[actor] = actor_count.get(actor, 0) + 1
        common_actor = max(actor_count, key=actor_count.get, default='Unknown')
        return f"'{common_actor}' has played the most in '{self.name}' genre."


movies = [Movie(**value) for value in data.values()]

# Testing the functionality
if __name__ == "__main__":
    star1 = Actor("Elizabeth Taylor")
    print(star1.amount_films())
    print(star1.average_rating())
    print(star1.popular_genre())
    print(star1.common_director())
    print(star1.common_actor())
    print(star1)

    genre = Genre("War")
    print(genre.amount_films())
    print(genre.average_rating())
    print(genre.common_actor())
    print(genre.common_director())
