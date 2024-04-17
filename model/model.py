from database.go_daily_sales_DAO import goDailySalesDAO
from database.go_products_DAO import goProductsDAO

class Model:
    def __init__(self):
        pass
    def get_anni(self):
        return goDailySalesDAO.get_years()
    def get_brand(self):
        return goProductsDAO.get_product_brand()

