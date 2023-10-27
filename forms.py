from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired
from models import Setor, Cargos

class SetorForm(FlaskForm):
    nome_setor = StringField('Setor', validators=[DataRequired()])
    submit_setor = SubmitField('Adicionar setor')

class FuncionariosForm(FlaskForm):
    primeiro_nome = StringField('Primeiro Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    data_admissao = DateField('Data de Admissão', format='%Y-%m-%d', validators=[DataRequired()])
    status_funcionario = BooleanField('Status do Funcionário')
    
    id_setor = SelectField('Setor', coerce=int, choices=[]) 
    id_cargo = SelectField('Cargo', coerce=int, choices=[])
    
    def set_choices(self):
        self.id_setor.choices = [(s.id, s.nome) for s in Setor.query.all()]
        self.id_cargo.choices = [(c.id, c.nome) for c in Cargos.query.all()]

    submit_funcionario = SubmitField('Adicionar Funcionário')
    