from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Drama(db.Model):
    __tablename__ = 'drama_table'
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary)
    title = db.Column(db.String(100), unique=True, nullable=False)
    screenwriter = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    themesong = db.Column(db.String(100), nullable=False)
    song_artist = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    tvstation = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    actor1 = db.Column(db.String(100), nullable=False)
    actor2 = db.Column(db.String(100), nullable=False)
    actor3 = db.Column(db.String(100), nullable=False)
    actor4 = db.Column(db.String(100), nullable=False)
    actor5 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Drama {self.title}>'
    
