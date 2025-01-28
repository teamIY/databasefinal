from flask import Blueprint, render_template, request, jsonify
from models.drama import Drama, db
from datetime import datetime
import logging

drama_bp = Blueprint('drama_bp', __name__)

@drama_bp.route('/')
def index():
    try:
        dramas = Drama.query.all()
        drama_list = [{'id': drama.id, 'img':drama.img,'title': drama.title, 'screenwriter':drama.screenwriter,'director':drama.director,'themesong':drama.themesong,'song_artist':drama.song_artist,'start_date':drama.start_date,'end_date':drama.end_date,'tvstation':drama.tvstation,'genre': drama.genre,'actor1':drama.actor1,'actor2':drama.actor2,'actor3':drama.actor3,'actor4':drama.actor4, 'actor5':drama.actor5} for drama in dramas]

        return render_template('index.html', insert_dramas=drama_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@drama_bp.route('/aaa')
def show_aaa():
    return render_template('aaa.html')

@drama_bp.route('/show_genre', methods=['POST'])
def show_genre():
    genre = request.form.get('genre')
    dramas = Drama.query.filter_by(genre=genre).all()
    return render_template('aaa2.html', genre=genre, dramas=dramas)


@drama_bp.route('/show_season', methods=['POST'])
def show_season():
    season = request.form.get('season')
    dramas = Drama.query.filter_by(season=season).all()
    return render_template('aaa2.html', season=season, dramas=dramas)

@drama_bp.route('/show_detail', methods=['post'])
def show_detail(drama_id):
    drama = Drama.query.get_or_404(drama_id)
    return render_template('aaa2.html',drama=drama)