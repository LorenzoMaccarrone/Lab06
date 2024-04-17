import _mysql_connector
from database.DB_connect import DBConnect
from model.go_daily_sales import GoDailySales

class goDailySalesDAO:
    #con @static method intediamo che non c'è bisogno di un init per questa classe
    @staticmethod
    def get_years():
        '''funzione che serve a estrapolare tutti gli anni di recensioni presenti nel database
        quindi se la data è 13-10-2021 voglio avere 2021'''
        cnx=DBConnect.get_connection()
        result=list()
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query=("select distinct (year(gds.`Date`))"
                   "from go_daily_sales gds")
            cursor.execute(query)
            for row in cursor:
                result.append(row)
        return result