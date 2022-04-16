def order(product, quantity):
    if product == "coffee":
        return quantity*1.50
    elif product == "water":
        return quantity*1.00
    elif product == "coke":
        return 1.40
    elif product == "snacks":
        return quantity*2.00


item = input()
quant = float(input())

print(f"{order(item, quant): .2f}") # може да форматираме направо функцията