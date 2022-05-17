from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB


db = SQLAlchemy(app)
db.init_app(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jsonb_data = db.Column(JSONB)

    def __repr__(self):
        return str(self.jsonb_data)




