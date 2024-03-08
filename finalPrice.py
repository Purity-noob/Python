def calculate_disount(price,discount_percent):
    if discount_percent >= 20.0 :
        finalPrice = price - 20.0 * price/100
    else:
        finalPrice = price

    return finalPrice;
userPrice= float(input("Enter the price:"))
userDicount = float(input("Enter the disount percentage:"))

print("The product cost is ",calculate_disount(userPrice,userDicount))

    