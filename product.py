class Product:
    """"The class containing information about the product, and associated mathods."""
    def __init__(self, ProductCode, ProductName, SalePrice, ManufactureCost, StockLevel, EstMonthlyUnits):
        self._ProductCode = ProductCode
        self._ProductName = ProductName
        self._SalePrice = SalePrice
        self._ManufactureCost = ManufactureCost
        self._StockLevel = StockLevel
        self._EstMonthlyUnits = EstMonthlyUnits

    