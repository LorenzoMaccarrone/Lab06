import flet as ft
from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno_scelto=None
        self.brand_scelto=None
        self.retailer_scelto=None

    def top_vendite(self,e):
        #gestione errore input
        if self.anno_scelto is None:
            self._view.create_alert("Anno non inserito, perfavore inserire anno")
        elif self.brand_scelto is None:
            self._view.create_alert("Brand non inserito, perfavore inserire brand")
        elif self.retailer_scelto is None:
            self._view.create_alert("Retailer non inserito, perfavore inserire retailer")
        #chiamata al modello

        #aggirnamento interfaccia attraverso la funzione appositamente creata nella view updata_page
        self._view.update_page()
    def analizza_vendite(self,e):
        # gestione errore input
        if self.anno_scelto is None:
            self._view.create_alert("Anno non inserito, perfavore inserire anno")
        elif self.brand_scelto is None:
            self._view.create_alert("Brand non inserito, perfavore inserire brand")
        elif self.retailer_scelto is None:
            self._view.create_alert("Retailer non inserito, perfavore inserire retailer")
        # chiamata al modello

        # aggirnamento interfaccia attraverso la funzione appositamente creata nella view updata_page
        self._view.update_page()

    #con populate dd_ andiamo a popolare i menu a tendina mentre con leggi_dd andiamo a leggere il valore scelto
    #dall'utente
    #populate dd_anno e dd_brand sfruttano le stringhe mente populate dd_retailer sfrutta gli oggetti
    def populate_dd_anno(self):
        #devo popolare a tendina, cerchiamo quanti anni sono prsenti nel database
        lista_di_anni = self._model.get_anni()
        for anno in lista_di_anni:
            #anno[0] perchè anno è una tupla composta da un solo elemento ovvero un intero
            #Quindi io voglio stampare a schermp l'intero, es 2015, e non la tupla, es (2015,)
            #difatti lista di anni è una lista di tuple
            self._view.dd_anno.options.append(ft.dropdown.Option(text=anno[0]))
        self._view.update_page()
    def populate_dd_brand(self):
        lista_di_brand = self._model.get_brand()
        for brand in lista_di_brand:
            self._view.dd_brand.options.append(ft.dropdown.Option(text=brand[0]))
        self._view.update_page()
    #piuttosto che un oggetto retailer il dropdown mi resituisce il codice del retailer scelto
    def populate_dd_retailer(self):
        lista_di_retailer = self._model.get_retailer()
        for retailer in lista_di_retailer:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.code, text=retailer.name))
        self._view.update_page()

    #ricordati la e per metodi che vengono chiamati all'interno di un elemento di flet
    #tutti questi leggi vengono chiamati on change di dropdown quindi devi mettere la e
    #mentre ad esempio i populate vengono chiamati fuori da qualsiasi elemento di flet difatti la e non c'è
    def leggi_anno(self, e):
        self.anno_scelto = self._view.dd_anno.value
    def leggi_brand(self, e):
        self.brand_scelto = self._view.dd_brand
    def leggi_retailer(self, e):
        self.retailer_scelto = self._view.dd_retailer

if __name__ == "__main__":
    m=Model()
    lista=m.get_retailer()
    for e in lista:
        print(e.name)
