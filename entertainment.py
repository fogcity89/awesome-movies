#!/usr/bin/env python
# Using the python library I had to import two things 'fresh_tomatoes' from another file(udacity) and a 'media' file
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                      "A story of a boy",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

mad_max = media.Movie("Mad Max",
                      "Max and Inferiosa",
                      "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SX640_SY720_.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

the_hateful_eight= media.Movie("The Hateful Eight",
                  "The new Quentin Tarentino moive staring Samuel L. Jackson!!",
                  "http://emertainmentmonthly.com/wp-content/uploads/2014/11/10575455_634561563308145_3740120470904440493_o.jpg"
                  "https://www.youtube.com/watch?v=nIOmotayDMY")


i_am_legend = media.Movie ("I am Legend",
                           "Will Smith is the last human being trying to save the human race before Zombies eat the whole world.",
                           "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSd2odoYVN2fVyLIpVqHhSuGD_imc5gFxs-VPQKmVlHRuG9bNKZDg",
                           "https://www.youtube.com/watch?v=ewpYq9rgg3w")

devil_wears_prada = media.Movie ("Devil Wears Prada",
                                 "Highly reccomended movie by women",
                                 "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
                                 "https://www.youtube.com/watch?v=XTDSwAxlNhc")

the_wolf_on_wall_street = media.Movie ("The Wolf on Wallstreet",
                            "Great movie from Martin S. and Leonardo D.",
                            "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX214_AL_.jpg",
                            "https://www.youtube.com/watch?v=iszwuX1AK6A")

movies = [toy_story, mad_max,the_hateful_eight, i_am_legend, devil_wears_prada, the_wolf_on_wall_street]

fresh_tomatoes.open_movies_page(movies)
