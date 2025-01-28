from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Drama(db.Model):
    __tablename__ = 'drama_table'
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary)
    title = db.Column(db.String(100), unique=True, nullable=False)
    screenwriter = db.Column(db.String(100), nullable=True)
    director = db.Column(db.String(100), nullable=True)
    themesong = db.Column(db.String(100), nullable=True)
    song_artist = db.Column(db.String(100), nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    tvstation = db.Column(db.String(100), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    actor1 = db.Column(db.String(100), nullable=True)
    actor2 = db.Column(db.String(100), nullable=True)
    actor3 = db.Column(db.String(100), nullable=True)
    actor4 = db.Column(db.String(100), nullable=True)
    actor5 = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Drama {self.title}>'