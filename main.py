import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)
'''
DA FARE:
1)manca la parte di logica per andare a selezionare dal database secondo i filtri dati dall'utente
  L'idea è quella di logica: o con una maggiore complessità in python, ovvero salvandosi il database
  all'interno del programma e lavorando sulle varie collections, oppure la query per trovare direttamente
  cosa ci serve
2)manca la richiesta 2
prova
'''