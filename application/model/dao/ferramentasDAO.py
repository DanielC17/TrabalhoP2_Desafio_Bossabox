
from application.model.entity.ferramentas import Ferramentas

ferramentas_list = [
    Ferramentas(1, "Django", "https://www.djangoproject.com/", "framework para projeto em python WEB", ["python", "framework"]),
    Ferramentas(2, "React", "https://pt-br.reactjs.org/", "framework para projetos em JS", ["JS", "framework"]),
    Ferramentas(3,"Trabalho", "https://vassouras.myopenlms.net/mod/assign/view.php?id=39348", "Entregar trabalho de LabHIPER", ["trabalho", "faculdade"] )
]


class FerramentasDAO():
    def __init__(self):
       self.ferramentas_list = ferramentas_list

    def lista_ferramentas(self):
        return self.ferramentas_list

