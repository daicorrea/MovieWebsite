import media
import fresh_tomatoes

harry_potter = media.Movie('Harry Potter', 'The boy who lived',
                           'https://www.harrypottermovieposters.com/wp-content/uploads/2014/05/harry-potter-and-the-deathly-hallows-part-i-movie-poster-2010-1020560181.jpg',
                           'https://www.youtube.com/watch?v=L8-e_VdwAME')

avatar = media.Movie('Avatar', 'Blue Tall People',
                     "http://4.bp.blogspot.com/_1qPLMlz01yQ/SwTA3GFVzxI/AAAAAAAADts/irJykYj7hJs/s1600/MarketSaw_03+Nov.+18+23.51.jpg",
                     'https://www.youtube.com/watch?v=d1_JBMrrYw8')

hunger_games = media.Movie('Hunger Games', 'A really real reality show',
                           'https://vignette.wikia.nocookie.net/thehungergames/images/c/ca/Hunger-Games-Movie-Poster-Jennifer-Lawrence.jpg/revision/latest?cb=20110417161424',
                           'https://www.youtube.com/watch?v=FovFG3N_RSU')

a_monster_call = media.Movie('A Monster Calls', 'Slap in your face... If you get it...',
                             'https://www.woodbangersentertainment.com/wp-content/uploads/2017/06/vdHUj9cyRe7fIYdJFMyc7elnawC.jpg',
                             'https://www.youtube.com/watch?v=R2Xbo-irtBA')

movies = [harry_potter, avatar, hunger_games, a_monster_call]

fresh_tomatoes.open_movies_page(movies)

