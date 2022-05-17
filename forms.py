from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class DataForm(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired(), Length(min=3)])
