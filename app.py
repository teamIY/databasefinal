from flask import Flask
from config import Config
from models.drama import db
from routes.drama_routes import drama_bp

app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemyオブジェクトの初期化
db.init_app(app)

# ブループリントの登録
app.register_blueprint(drama_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)