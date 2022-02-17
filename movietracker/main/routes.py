from . import main
from flask import render_template, request
from ..request import get_movies
from .utils import save_data_to_db
from movietracker.models import MovieDB


@main.route('/')
@main.route('/home')
def home():
    # get movies from API
    popular_movies = get_movies(pages=3)

    # save movies to database
    save_data_to_db(popular_movies)

    # paginate
    page = request.args.get('page', 1, type=int)

    # get movies from database
    popular_movies_from_db = MovieDB.query.all() #.paginate(page=page, per_page=12)

    return render_template('home.html', popular_movies=popular_movies_from_db)
