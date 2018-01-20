import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_link):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_link

    def show_trailer(self):
        webbrowser.get('safari').open_new(self.trailer_youtube_url)