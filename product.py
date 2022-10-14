import random

class Product:
    """"The class containing information about the product, and associated mathods."""
    def __init__(self, ProductCode, ProductName, SalePrice, ManufactureCost, StockLevel, EstMonthlyUnits):
        self._ProductCode = ProductCode
        self._ProductName = ProductName
        self._SalePrice = SalePrice
        self._ManufactureCost = ManufactureCost
        self._StockLevel = StockLevel
        self._EstMonthlyUnits = EstMonthlyUnits

    #Attribute return methods

    def ProductCode(self):
        return self._ProductCode
    def ProductName(self):
        return self._ProductName
    def SalePrice(self):
        return self._SalePrice
    def ManufactureCost(self):
        return self._ManufactureCost
    def StockLevel(self):
        return self._StockLevel
    def EstMonthlyUnits(self):
        return self._EstMonthlyUnits

    #Monthly units produced

    def ActMonthlyUnits(self):
        MonthlySales = []
        StockRecord = []
        for i in range(12):
            MonthlySales.append(self._EstMonthlyUnits + random.randint(-10, 10))
            if i == 0:
                StockRecord.append(self._StockLevel + self._EstMonthlyUnits - MonthlySales[0])
            else:
                StockRecord.append(StockRecord[i - 1] + self._EstMonthlyUnits - MonthlySales[i])

        self._MonthlyStock = StockRecord
        self._MonthlySales = MonthlySales
        return StockRecord

    #Returns Total profit

    def Profit(self):
        return sum(self._MonthlySales)*self.SalePrice - sum(self._EstMonthlyUnits)*self.ManufactureCost
