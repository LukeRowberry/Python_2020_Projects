#Luke Rowberry
#10/27/2020
#Cash register

numItems = 4
costPerItem = 10.00
taxRate = 0.08
subTotal = numItems *costPerItem
taxAmount = subTotal *taxRate
totalPrice = subTotal * taxAmount

print("SALES RECEIPT")
print("Number of items :  " + str(numItems))
print("Cost per item   : $" + str(costPerItem))
print("Tax rate        :  " + str(taxRate))
print("Tax amount      : $" + str(taxAmount))
print("TOTAL SALE PRICE: $" + str(totalPrice))
