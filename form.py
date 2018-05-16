from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired


class lambdaForm(FlaskForm):
    lambda1 = FloatField('', validators=[DataRequired()])
    lambda2 = FloatField('', validators=[DataRequired()])
    submit = SubmitField('Start')

