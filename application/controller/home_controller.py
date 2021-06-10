from application import app
from application.model.dao.ferramentasDAO import FerramentasDAO
from flask import render_template, request, url_for, redirect

ferramentaDAO = FerramentasDAO()
ferramenta_list = ferramentaDAO.lista_ferramentas()



@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", ferramenta_list = ferramenta_list)
