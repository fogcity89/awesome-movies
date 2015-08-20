import webbrowser
class Movie():
    """
    The class movie will call on 4 arguments, movie title, storyline, image, and youtube.
    Movie class is for many elements inside one class of the Movie folder
    
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """
    here I used the init function and self function
    """
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
