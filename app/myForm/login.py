from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, length


class MyForm(FlaskForm):
	name = StringField('name', validators=[DataRequired(), length(min=20, max=50)])

