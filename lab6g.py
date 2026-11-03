# Author: Mehtaash Kaur
# Date: 2026-11-04

# TO DO 1: Create function add_movie(). 
def add_movie(database, name, director, year, runtime):
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)
# TO DO 2: Call the function 4 times.
# TO DO 3: Print the database as instructed in readme.md file.
def main():
    movie_db = []
    add_movie(movie_db, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(movie_db, "Gone with the Wind", "Victor Fleming", 1939, 238)
    add_movie(movie_db, "Forever Gone", "Sam Smith", 2015, 95)
    add_movie(movie_db, "The Matrix", "Lana Wachowski", 1999, 136)
 
    for movie in movie_db:
        print(movie)
# TO DO 4: Run the script. Take screenshot of code and script.
main()