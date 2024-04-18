from model.go_retailers import Retailer
from database.DB_connect import DBConnect

class RetailerDAO:
    @staticmethod
    def get_retailers():
        '''funzione che serve a prendere tutti i retailer'''
        cnx = DBConnect.get_connection()
        result = list()
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            #query da implemetare
            query = ("select gr.*"
                     "from go_retailers gr")
            cursor.execute(query)
            for row in cursor:
                result.append(Retailer(row[0],row[1],row[2],row[3]))
        cursor.close()
        cnx.close()
        return result
