from flask import Blueprint, render_template, jsonify
from models.drama import Drama, db

drama_bp = Blueprint('drama_bp', __name__)

@drama_bp.route('/')
def index():
    try:
        dramas = Drama.query.all()
        drama_list = [{'id': drama.id, 'img':drama.img,'title': drama.title, 'screenwriter':drama.screenwriter,'director':drama.director,'themesong':drama.themesong,'song_artist':drama.song_artist,'start_date':drama.start_date,'end_date':drama.end_date,'tvstation':drama.tvstation,'genre': drama.genre,'actor1':drama.actor1,'actor2':drama.actor2,'actor3':drama.actor3,'actor4':drama.actor4, 'actor5':drama.actor5} for drama in dramas]

        return render_template('index.html', insert_dramas=drama_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500