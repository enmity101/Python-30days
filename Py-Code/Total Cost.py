price_shirt = 25.00
price_jeans = 45.50

qty_shirt = 2
qty_jeans = 1

total_shirt = price_shirt * qty_shirt
print("Total Shirt Cost:", total_shirt)
total_jeans = price_jeans * qty_jeans
print("Total Jeans Cost:", total_jeans)
subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)
discount = 0.10 * subtotal
print("Discount:", discount)
total = subtotal - discount
print("Total after Discount:", total)