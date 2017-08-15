import os
import fresh_tomatoes
import media

y = "C:\Users\ ... \Udacity"   # This is the directory path where all files for the project are save locally
os.chdir(y)   # Changing the directory where fresh_tomatoes and media modules are saved locally

# Creating instances of my favorite movies
foodfight = media.Movie("Foodfight!", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwMDY1MDI0NV5BMl5BanBnXkFtZTgwODAyODk3NzE@._V1_UY268_CR9,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=81uIhu8qrrs")
dunkirk = media.Movie("Dunkirk", "https://images-na.ssl-images-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=F-eMt3SrfFU")
sing = media.Movie("Sing", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzODYzODU2Ml5BMl5BanBnXkFtZTgwNTc1MTA2NzE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=f_jxPEwJNeA")
girls_trip = media.Movie("Girls Trip", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMwNTEzODUwMV5BMl5BanBnXkFtZTgwNjE5NjA5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=7jE61BzKmgQ")
darktower = media.Movie("The Dark Tower", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3MjUwMzQ3MF5BMl5BanBnXkFtZTgwMjcwNjkxMjI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=GjwfqXTebIY")
moana = media.Movie("Moana", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=LKFuXETZUsI")
wall = media.Movie("The Wall", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5ODMyNzE4OF5BMl5BanBnXkFtZTgwNTM0Mzc4MTI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=MyCuUr2_hmA")
logan = media.Movie("Logan", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=gbug3zTm3Ws")
baywatch = media.Movie("Baywatch", "https://images-na.ssl-images-amazon.com/images/M/MV5BNTA4MjQ0ODQzNF5BMl5BanBnXkFtZTgwNzA5NjYzMjI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=nZ5tqzw841s")

# Creating list of favorite movies
movies = [foodfight, dunkirk, sing, girls_trip, darktower, moana, wall, logan, baywatch]

# Using the open_movies_page function to produce website showcase of movies
fresh_tomatoes.open_movies_page(movies)
