product = {
    "laptop": {"price": 800, "quantity": 5},
    "mobile": {"price": 400, "quantity": 4},
    "Ipad": {"price": 600, "quantity": 8}
}

# wap to find total price of each product and highest priced product

result = []
largest = 0

for i in product:
    rate = (product[i]["price"] * product[i]["quantity"])
    result.append(rate)

    if rate > largest:
        largest = rate
        element = i

print(result)
print(largest, element)
