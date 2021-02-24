from flask import Flask
from flask_login import LoginManager

import views
import os
from database import Database
from movie import Movie
from user import get_user


lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)

    app.add_url_rule("/login", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout_page)
    app.add_url_rule("/movies", view_func=views.movies_page, methods=["GET", "POST"])
    app.add_url_rule("/movies/<int:movie_key>", view_func=views.movie_page)
    app.add_url_rule("/movies/<int:movie_key>/edit",view_func=views.movie_edit_page,methods=["GET", "POST"],)
    app.add_url_rule("/new-movie", view_func=views.movie_add_page, methods=["GET", "POST"])

    lm.init_app(app)
    lm.login_view = "login_page"

    path = "\\ege-cloud"

    #conn = sqlite3.connect("C:\\users\\guest\\desktop\\example.db")

    '''
    home_dir = os.path.expanduser("~")
    db = Database(os.path.join(home_dir, "movies.db"))
    app.config["db"] = db
    return app  
    '''

    #'C:\\Users\\ugur_\\movies.db'
    home_dir = os.path.expanduser("~")
    db = Database("C:\\Users\\ugur_\\movies.db")
    app.config["db"] = db
    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 6000)
    app.run(host="127.0.0.1", port=port)