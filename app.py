from sqlalchemy import desc
from config import app, db
from models import Setor, Funcionarios
from flask import render_template, request, redirect, flash
from forms import *

@app.route('/', methods=['GET', 'POST'])
def get_setores():
    form = SetorForm()
    setores = Setor.query.all()

    if form.validate_on_submit():
        nome_setor = request.form.get('nome_setor')

        for setor in setores:
            if setor.nome == nome_setor:
                flash('Nome de setor já existe. Escolha outro!', 'danger')
                break
        else:
            novo_setor = Setor(nome=nome_setor)
            db.session.add(novo_setor)
            db.session.commit()
            flash(f'Setor "{nome_setor}" criado com sucesso!', 'success')

        return redirect('/')

    return render_template('index.html', setores=setores, form=form)

@app.route('/<int:id>', methods=['POST'])
def delete_setor(id):
    if request.form.get('_method') == 'DELETE':
        setor = Setor.query.get_or_404(id)
        db.session.delete(setor)
        db.session.commit()
        flash('Setor apagado com sucesso!', 'success')

    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_setor(id):
    setor = Setor.query.get_or_404(id)
    form = SetorForm(nome_setor=setor.nome)

    if form.validate_on_submit():
        nome = request.form.get('nome_setor')
        setores = Setor.query.all()

        for setor_post in setores:
            print(setor_post)
            if setor_post.nome == nome:
                flash('Nome de setor já existe. Escolha outro!', 'danger')
                return render_template('edit_setor.html', setor=setor, form=form)
        setor.nome = form.nome_setor.data
        db.session.commit()
        flash('Setor atualizado com sucesso!', 'success')
        return redirect('/')

    return render_template('edit_setor.html', form=form, setor=setor)

@app.route('/funcionarios/<id_setor>', methods=['GET'])
def get_funcionarios(id_setor):

    funcionarios = Funcionarios.query.filter_by(id_setor=id_setor).order_by(desc(Funcionarios.status_funcionario)).all()

    return render_template('funcionario.html', funcionarios=funcionarios)

if __name__ == '__main__':  
    app.run(debug=True)
