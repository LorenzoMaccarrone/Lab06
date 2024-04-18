from dataclasses import dataclass
'''Usando @dataclass non c'è bisogno di scrivere l'init perchè se lo gestisce lui.
Se ad esempio creassi un oggeto retailer così Retailer(1,b,c,d) verrebbe creato un oggetto che avrà come codice
1 come nome b come tipo c e come country d'''
@dataclass
class Retailer:
    code: int
    name: str
    type: str
    country: str
    def __eq__(self, other):
        return self.code == other.code
    def __hash__(self):
        return hash(self.code)