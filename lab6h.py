# Author: Mehtaash Kaur
# Date: 2026-11-04

# TO DO 1: Copy the code from lab6g.py and paste here.
def add_movie(database, name, director, year, runtime):
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)

# TO DO 2: Create function find_movie().
def find_movie(database, search):
    # Case-insensitive search of the movie title
    matches = []
    for movie in database:
        if search.lower() in movie["name"].lower():
            matches.append(movie)
    return matches
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.
def main():
    movie_db = []
    add_movie(movie_db, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(movie_db, "Gone with the Wind", "Victor Fleming", 1939, 238)
    add_movie(movie_db, "Forever Gone", "Sam Smith", 2015, 95)
    add_movie(movie_db, "The Matrix", "Lana Wachowski", 1999, 136)
 
    for movie in movie_db:
        print(movie)
 
    print("--- Search: gone ---")
    for movie in find_movie(movie_db, "gone"):
        print(movie)
 
    print("--- Search: the ---")
    for movie in find_movie(movie_db, "the"):
        print(movie)
 
main()
