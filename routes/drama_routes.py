from flask import Blueprint, render_template, request, jsonify
from models.drama import Drama, db
from datetime import datetime
import logging
from sqlalchemy import or_, and_

drama_bp = Blueprint('drama_bp', __name__)

@drama_bp.route('/')    
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

def filter_drama(keyword):
    return  Drama.query.filter(
        or_(
            Drama.title.like(f"%{keyword}%"),
            Drama.screenwriter.like(f"%{keyword}%"),
            Drama.director.like(f"%{keyword}%"),
            Drama.themesong.like(f"%{keyword}%"),
            Drama.song_artist.like(f"%{keyword}%"),
            Drama.tvstation.like(f"%{keyword}%"),
            Drama.actor1.like(f"%{keyword}%"),
            Drama.actor2.like(f"%{keyword}%"),
            Drama.actor3.like(f"%{keyword}%"),
            Drama.actor4.like(f"%{keyword}%"),
            Drama.actor5.like(f"%{keyword}%")
        )
    )

@drama_bp.route('/show_search', methods=['POST'])
def show_search():
    moji = request.form.get('moji')
    dramas = filter_drama(moji).all()
    return render_template('next.html', title=moji, dramas=dramas)


@drama_bp.route('/show_detail/<int:drama_id>', methods=['GET'])
def show_detail(drama_id):
    drama = Drama.query.get(drama_id)  
    return render_template('detail.html', drama=drama)


