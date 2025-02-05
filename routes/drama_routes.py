from flask import Blueprint, render_template, request, jsonify
from models.drama import Drama, db
from datetime import datetime
import logging
from sqlalchemy import or_, and_

drama_bp = Blueprint('drama_bp', __name__)

@drama_bp.route('/')
#def index():
#    try:
#        dramas = Drama.query.all()
#        drama_list = [{'id': drama.id, 'img':drama.img,'title': drama.title, 'screenwriter':drama.screenwriter,'director':drama.director,'themesong':drama.themesong,'song_artist':drama.song_artist,'start_date':drama.start_date,'end_date':drama.end_date,'tvstation':drama.tvstation,'genre': drama.genre,'actor1':drama.actor1,'actor2':drama.actor2,'actor3':drama.actor3,'actor4':drama.actor4, 'actor5':drama.actor5} for drama in dramas]
#
#        return render_template('index.html', insert_dramas=drama_list)
#    except Exception as e:
#        return jsonify({'error': str(e)}), 500
    
def main():
    return render_template("main.html")



@drama_bp.route('/show_genre', methods=['POST'])
def show_genre():
    genre = request.form.get('genre')
    dramas = Drama.query.filter_by(genre=genre).all()
    return render_template('next.html', genre=genre, dramas=dramas)


@drama_bp.route('/show_season', methods=['POST'])
def show_season():
    season = request.form.get('season')
    year, season_name = season[:4], season[4:]
    if season_name == "春":
        start_month = 4
    elif season_name == "夏":
        start_month = 7
    elif season_name == "秋":
        start_month = 10
    else:
        start_month = 1
        
    start_season = datetime(int(year), start_month, 1)
    end_season = datetime(int(year), start_month + 1, 1)  


    dramas = Drama.query.filter(
        and_(
            Drama.start_date >= start_season,
            Drama.start_date < end_season
        )
    ).all()

    return render_template('next.html', season=season, dramas=dramas)



@drama_bp.route('/show_detail', methods=['POST'])
def show_detail():
    moji = request.form.get('moji')
    dramas = Drama.query.filter(
        or_(
            Drama.title.like(f"%{moji}%"),
            Drama.screenwriter.like(f"%{moji}%"),
            Drama.director.like(f"%{moji}%"),
            Drama.themesong.like(f"%{moji}%"),
            Drama.song_artist.like(f"%{moji}%"),
            Drama.tvstation.like(f"%{moji}%"),
            Drama.actor1.like(f"%{moji}%"),
            Drama.actor2.like(f"%{moji}%"),
            Drama.actor3.like(f"%{moji}%"),
            Drama.actor4.like(f"%{moji}%"),
            Drama.actor5.like(f"%{moji}%")
        )
    ).all()
    return render_template('next.html', title=moji, dramas=dramas)