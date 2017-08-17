import os
import fresh_tomatoes
import media

y = "C:\Users\Jose\Documents\Udacity"    # This is the directory path
os.chdir(y)    # Changing to the directory

# Creating instances of my favorite movies
foodfight = media.Movie("Foodfight!",
                        "foodfight.jpg",
                        "https://www.youtube.com/watch?v=81uIhu8qrrs")
dunkirk = media.Movie("Dunkirk",
                      "dunkirk.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")
sing = media.Movie("Sing",
                   "sing.jpg",
                   "https://www.youtube.com/watch?v=f_jxPEwJNeA")
girls_trip = media.Movie("Girls Trip",
                         "girlstrip.jpg",
                         "https://www.youtube.com/watch?v=7jE61BzKmgQ")
darktower = media.Movie("The Dark Tower",
                        "darktower.jpg",
                        "https://www.youtube.com/watch?v=GjwfqXTebIY")
moana = media.Movie("Moana",
                    "moana.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
wall = media.Movie("The Wall",
                   "wall.jpg",
                   "https://www.youtube.com/watch?v=MyCuUr2_hmA")
logan = media.Movie("Logan",
                    "logan.jpg",
                    "https://www.youtube.com/watch?v=gbug3zTm3Ws")
baywatch = media.Movie("Baywatch",
                       "baywatch.jpg",
                       "https://www.youtube.com/watch?v=nZ5tqzw841s")

# Creating list of favorite movies
movies = [foodfight, dunkirk, sing, girls_trip, darktower,
          moana, wall, logan, baywatch]

# Using the open_movies_page function to produce website showcase of movies
fresh_tomatoes.open_movies_page(movies)
