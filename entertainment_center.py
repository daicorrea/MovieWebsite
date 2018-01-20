import media

harry_potter = media.Movie('Harry Potter', 'The boy who lived',
                           'https://www.harrypottermovieposters.com/wp-content/uploads/2014/05/harry-potter-and-the-deathly-hallows-part-i-movie-poster-2010-1020560181.jpg',
                           'https://www.youtube.com/watch?v=L8-e_VdwAME')
print(harry_potter.title)
avatar = media.Movie('Avatar', 'Blue Tall People',
                     "http://4.bp.blogspot.com/_1qPLMlz01yQ/SwTA3GFVzxI/AAAAAAAADts/irJykYj7hJs/s1600/MarketSaw_03+Nov.+18+23.51.jpg",
                     'https://www.youtube.com/watch?v=d1_JBMrrYw8')
print(avatar.storyline)
avatar.show_trailer()

