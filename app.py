"""User interaction"""

import product

def Validation(item, prompt):
    """Makes sure the input value for the item parameter is an integer, and returns it.
    The prompt is simply a custom message that prompts input from the user."""
    while True:
        try:
            item = int(input(prompt))
            break
        except ValueError:
            print("Invalid entry. Please try again.")
    return item

class App:
    def CreateProduct(self):

        #input

        ProductCode = 0
        ProductName = input("Enter the product name:\n")
        SalePrice = 0
        ManufactureCost = 0
        StockLevel = 0
        EstMonthlyUnits = 0
        ProductCode = Validation(ProductCode, "Enter the product code, an integer:\n")
        SalePrice = Validation(SalePrice, "Enter the sales price in Canadian dollars:\n")
        ManufactureCost = Validation(ManufactureCost, "Enter the cost of manufacturing in Canadian dollrs:\n")
        StockLevel = Validation(StockLevel, "Enter the stock level:\n")
        EstMonthlyUnits = Validation(EstMonthlyUnits, "Enter the estimated monthly production:\n")

        Product = product.Product(ProductCode, ProductName, SalePrice, ManufactureCost, StockLevel, EstMonthlyUnits)
        return Product

        #Statement printing

    def AnnualStatement(self):
        Product = self.CreateProduct()
        Product.ActMonthlyUnits()

        print(f"\nProduct Code: {Product._ProductCode}")
        print(f"Product Name: {Product._ProductName}\n")
        print(f"Sale Price: {Product._SalePrice} CAD")
        print(f"Manufacturing Cost: {Product._ManufactureCost} CAD")
        print(f"Approximate monthly Production: {Product._EstMonthlyUnits}\n    ")

        for i in range(12):
            print(f"Month {i+1}:\n    Manufactured: {Product.EstMonthlyUnits()} units")
            print(f"    Stock: {Product._MonthlyStock[i]}")
            print(f"    Sales: {Product._MonthlySales[i]}")
        print(f"Profit for this year was {Product.Profit()}")


app = App()
app.AnnualStatement()
