import _mysql_connector
from database.DB_connect import DBConnect

class goProductsDAO:
    #ATTENZIONE: ti ricordo che static method rende il metodo una sorta di metodo globale,
    #quindi self non deve essere presente da nessuna parte neanche nelle parentesi della definizione
    #del metodo ovviamente! quindi get_product_brand(self)-->NOO proprio perchè è una sorta di metodo globale
    #a quale self dovrebbe fare riferimento se è globale?
    @staticmethod
    def get_product_brand():
        '''funzione che serve a estrapolare tutti i brand del database'''
        cnx = DBConnect.get_connection()
        result = list()
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = ("select DISTINCT(gp.Product_brand)"
                     "from go_products gp" )
            cursor.execute(query)
            for row in cursor:
                result.append(row)
        cursor.close()
        cnx.close()
        return result