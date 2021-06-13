from application import app
from application.model.dao.ferramentasDAO import FerramentasDAO
from flask import render_template, request, url_for, redirect
from application.model.entity.ferramentas import Ferramentas

ferramentaDAO = FerramentasDAO()
ferramenta_list = ferramentaDAO.lista_ferramentas()



@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", ferramenta_list = ferramenta_list)

@app.route("/inserir", methods=['POST'])
def inserir():
    titulo = request.form.get('titulo', None)
    link = request.form.get('link', None)
    descricao = request.form.get('descricao', None)
    tags = request.form.get('tags', None).split(" ")
    id = len(ferramenta_list) + 1
    ferramentas = Ferramentas(id, titulo, link, descricao, tags)
    ferramentas.append(ferramentas)
    return render_template("index.html", ferramenta_list = ferramenta_list)
