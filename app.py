"""User interaction"""

import product

def Validation(item, prompt):
    while True:
        try:
            item = int(input(prompt))
            break
        except ValueError:
            print("Invalid entry. Please try again.")
    return item

class app():
    def CreateProduct(self):
        ProductCode = input("Enter the product code:\n")
        ProductName = input("Enter the product name:\n")
        SalePrice = 0
        ManufactureCost = 0
        Validation(SalePrice, "Enter the sales price in Canadian dollars:\n")
        Validation(ManufactureCost, "Enter the cost of manufacturing in Canadian dollrs:\n")

        
