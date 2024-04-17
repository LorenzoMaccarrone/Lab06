import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Analizzatore di vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_top=None
        self.btn_analizza=None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)
        '''quando viene cliccato sul menu a tendina e scelto uno degli elementi, quindi on change, viene mandato tale messaggio
        al controllore attraverso il metodo leggi anno che salverà l'anno scelto in una variabile
        Per popolare il menu a tendina, una volta creato bisogna richiamare un metodo del controllore che legga quali 
        sono gli anni disponibili nel database. Tale funzione viene chiamata populate dd_anno.
        Ovviamente valgono le stesse istruzioni per ognuno dei dropdown. Quindi viene creato il dropdown e subito
        popolato'''
        #row 1
        self.dd_anno = ft.Dropdown(
            hint_text="Anno",
            options=[
                ft.dropdown.Option("Nessun Filtro"),

            ],
            on_change=self._controller.leggi_anno

        )
        self._controller.populate_dd_anno()

        self.dd_brand = ft.Dropdown(
            hint_text="Brand",
            options=[
                ft.dropdown.Option("Nessun Filtro"),

            ],
            on_change=self._controller.leggi_brand
        )
        self._controller.populate_dd_brand()

        self.dd_retailer = ft.Dropdown(
            hint_text="Retailer",
            options=[
                ft.dropdown.Option("Nessun Filtro"),

            ],
            on_change=self._controller.leggi_retailer
        )
        self._controller.populate_dd_retailer()

        row1 = ft.Row([self.dd_anno,self.dd_brand,self.dd_retailer],ft.MainAxisAlignment.CENTER,)
        self._page.controls.append(row1)
        self._page.update()
        #row2
        self.btn_top=ft.ElevatedButton(text="Top Vendite",on_click=self._controller.top_vendite)
        self.btn_analizza = ft.ElevatedButton(text="Analizza Vendite",on_click=self._controller.analizza_vendite)
        row2 = ft.Row([self.btn_top,self.btn_analizza],ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
