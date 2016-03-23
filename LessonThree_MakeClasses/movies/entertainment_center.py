

import media, fresh_tomatoes

##toy_story = media.Movie("Toy story",
##                        "A story of a boy and his toys that come to life",
##                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
##                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

boardwalk_empire = media.Movie("Boardwalk Empire",
                               "A story about prohibtion era gangsters",
                               "https://upload.wikimedia.org/wikipedia/en/2/2d/Boardwalk_Empire_2010_Intertitle.png",
                               "https://www.youtube.com/watch?v=NCIpAvBvXgw")

game_of_thrones = media.Movie("Game of Thrones",
                              "A fantasy world with a war for the throne",
                              "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg",
                              "https://www.youtube.com/watch?v=522l0YE9hRQ")

san_andreas = media.Movie("San Andreas",
                          "A series of recordbreaking earthquakes hit San Francisco",
                          "https://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg",
                          "https://www.youtube.com/watch?v=23VflsU3kZE")
breaking_bad = media.Movie("Breaking Bad",
                           "A highschool chemistry turned meth cook",
                           "http://www.gstatic.com/tv/thumb/tvbanners/9181462/p9181462_b_v8_aa.jpg",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")
                           
#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#game_of_thrones.show_trailer()

movies = [avatar, boardwalk_empire, game_of_thrones, san_andreas, breaking_bad]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
