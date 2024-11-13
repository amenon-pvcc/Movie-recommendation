import csv
import requests

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __repr__(self):
        return f"'{self.title}' ({self.genre}) - Rating: {self.rating}"

class MovieDatabase:
    def __init__(self):
        self.movies = self.load_movies()

    def load_movies(self):
        movies = []
        url = "https://raw.githubusercontent.com/your-username/movie-recommendation-chatbot/main/movies.csv"
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()
        csv_reader = csv.DictReader(lines)
        for row in csv_reader:
            movies.append(Movie(row["title"], row["genre"], float(row["rating"])))
        return movies

    def get_movies_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]

def chatbot():
    print("Welcome to the Movie Recommendation Chatbot!")
    print("I can recommend movies based on genre.")
    
    movie_db = MovieDatabase()

    while True:
        genre = input("\nEnter a movie genre (e.g., Sci-Fi, Drama, Comedy, etc.) or 'exit' to quit: ").strip()

        if genre.lower() == 'exit':
            print("Goodbye!")
            break

        movies = movie_db.get_movies_by_genre(genre)

        if movies:
            print(f"\nHere are some {genre} movies you might like:")
            for movie in movies:
                print(movie)
        else:
            print(f"\nSorry, I couldn't find any {genre} movies. Try another genre.")

if __name__ == "__main__":
    chatbot()
