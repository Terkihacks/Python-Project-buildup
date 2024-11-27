def calculate_discount(price,discount_percent):
    price = input("Enter the original price")
    buyingPrice = input("Enter the buying price")
    discount = buyingPrice-price

    discount_percent = discount/100

    if discount_percent >= 20:
      print(discount_percent)
    else:
       print(price)
       
calculate_discount(price,discount_percent)    
    
