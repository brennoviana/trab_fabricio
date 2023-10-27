from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SetorForm(FlaskForm):
    nome_setor = StringField('Setor', validators=[DataRequired()])
    submit_setor = SubmitField('Adicionar setor')
