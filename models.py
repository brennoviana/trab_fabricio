from config import db
from sqlalchemy.orm import relationship

class Setor(db.Model):
    __tablename__ = 'setor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    funcionarios = relationship("Funcionarios", back_populates="setor")

class Funcionarios(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    primeiro_nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    status_funcionario = db.Column(db.Boolean, nullable=False)
    id_setor = db.Column(db.Integer, db.ForeignKey('setor.id'))
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargos.id'))

    setor = relationship("Setor", back_populates="funcionarios")
    cargos = relationship("Cargos", back_populates="funcionarios")

class Cargos(db.Model):
    __tablename__ = 'cargos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    id_setor = db.Column(db.Integer, db.ForeignKey('setor.id'))

    funcionarios = relationship("Funcionarios", back_populates="cargos")
