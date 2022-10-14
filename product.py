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