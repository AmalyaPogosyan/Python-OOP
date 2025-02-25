# Movie Analysis Project

## Overview

This project provides a Python-based system for analyzing movies, actors, and genres using data from a JSON file. The system allows you to:

- Create and manage `Movie` objects with details like release year, duration, genre, IMDb rating, director, actors, and box office earnings.
- Analyze `Actor` statistics, such as the number of movies they have acted in, their average IMDb rating, their most frequent co-actors, and their most popular genre.
- Analyze `Genre` statistics, including the number of movies in the genre, average IMDb rating, most common director, and the most frequent actor in that genre.

## Features

- **Movie Management**: Store and retrieve detailed information about movies.
- **Actor Analysis**: Identify an actor’s most frequent collaborations and highest-rated performances.
- **Genre Analysis**: Determine the most common directors and actors in a particular genre.

## Installation

### Prerequisites

- Python 3.x
- JSON file containing movie data (`read_json.py` should provide `data` as a dictionary)

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/movie-analysis.git
   cd movie-analysis
   ```
2. Ensure you have the required dependencies (if any are added in the future).
3. Run the script:
   ```sh
   python main.py
   ```

## Usage

### Creating a Movie Object

```python
from read_json import data
movies = [Movie(**value) for value in data.values()]
print(movies[0])  # Display first movie details
```

### Actor Analysis

```python
actor = Actor("Elizabeth Taylor")
print(actor.amount_films())
print(actor.average_rating())
print(actor.popular_genre())
print(actor.common_director())
print(actor.common_actor())
```

### Genre Analysis

```python
genre = Genre("War")
print(genre.amount_films())
print(genre.average_rating())
print(genre.common_actor())
print(genre.common_director())
```

## File Structure

```
movie-analysis/
│── read_json.py   # Imports JSON movie data
│── main.py        # Main script to execute analysis
│── movie_analysis.py # Contains Movie, Actor, and Genre classes
│── README.md      # Project documentation
```

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author 

          Amalya Poghosyan

