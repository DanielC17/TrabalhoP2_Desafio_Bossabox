
from application.model.entity.ferramentas import Ferramentas

ferramentas_list = [
    Ferramentas(1, "Django", "https://www.djangoproject.com/", "framework para projeto em python WEB", ["python", "framework"]),
    Ferramentas(2, "React", "https://pt-br.reactjs.org/", "framework para projetos em JS", ["JS", "framework"]),

]

class FerramentasDAO():
    def __init__(self):
       self.ferramentas_list = ferramentas_list

    def lista_ferramentas(self):
        return self.ferramentas_list

