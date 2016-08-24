import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4"
                        )
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io"
                     )

Arumba_Video = media.Movie("Arumba Plays DOTA The Most Broken Abilty Combo in Ability Draft ",
                           "Arumba Plays DOTA The Most Broken Abilty Combo in Ability Draft ",
                           "https://yt3.ggpht.com/-nrLIzF3vsyk/AAAAAAAAAAI/AAAAAAAAAAA/rW5CUuWvGZ0/s88-c-k-no-rj-c0xffffff/photo.jpg",
                           "https://www.youtube.com/watch?v=USgpdwmXpYU"
                           )

#print(Arumba_Video.storyline)
#Arumba_Video.show_trailer()


school_of_rock = media.Movie("School of Rock", "Using rock music to learn.",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/school_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris.",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors.",
                          "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=atLg2wQQxvU")
Hunger_Games = media.Movie("Hunger Games", "A stupid dystopian future.",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,Arumba_Video]
fresh_tomatoes.open_movies_page(movies)
