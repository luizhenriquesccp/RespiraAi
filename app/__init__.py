from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import routes, models
from app.seed import seed_exercicios

with app.app_context():
    models.Base.metadata.create_all(bind=db.engine)
    with db.session() as db_session:
        seed_exercicios(db_session)