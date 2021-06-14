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
    titulo = request.form.get('form_titulo', None)
    link = request.form.get('form_link', None)
    descricao = request.form.get('form_desc', None)
    tags = request.form.get('form_tags', None).split(" ")
    id = len(ferramenta_list) + 1
    ferramentas = Ferramentas(id, titulo, link, descricao, tags)
    ferramenta_list.append(ferramentas)
    return render_template("index.html", ferramenta_list = ferramenta_list)


@app.route("/excluir/<int:id>", methods=['GET'])
def excluir(id: int):
    for i in ferramenta_list:
        if i.id == id:
            ferramenta_list.remove(i)
            return render_template("index.html", ferramenta_list = ferramenta_list)
    return render_template("index.html",ferramenta_list = ferramenta_list), 404


@app.route("/busca", methods=['GET'])
def busca():
    ferramentas_filtradas_list = []
    pesquisar = request.args.get('pesquisa')
    pesquisar_tag = request.args.get('tag')
    for ferramenta in ferramenta_list:
        if pesquisar_tag == "on":
            if pesquisar in ferramenta.tags:
                ferramentas_filtradas_list.append(ferramenta)
        elif pesquisar_tag == None:
            if pesquisar in ferramenta.titulo or pesquisar in ferramenta.descricao:
                ferramentas_filtradas_list.append(ferramenta)


    return render_template("index.html", ferramenta_list = ferramentas_filtradas_list)
