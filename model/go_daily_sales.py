from dataclasses import dataclass
from datetime import datetime
@dataclass
class GoDailySales:
    retailer_code: float
    product_number: float
    data: datetime
    quantity: int
    unit_price: float
    unit_sale_price: float

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code and self.product_number == other.product_number and self.data == other.date
    def __hash__(self):
        return hash(self.retailer_code) + hash(self.product_number) + hash(self.data)