mobiles = {
    "Apple": {"model": "iphone15", "price": 120000, "color": "Black"},
    "Samsung": {"model": "s23 ultra", "price": 180000, "color": "white"},
    "Sony": {"model": "xperia ultra", "price": 130000, "color": "red"},
    "Huawei": {"model": "Pura 70 ultra", "price": 170000, "color": "Black"}
}

# wap to list the phones priced above 130000

for i in mobiles:
    if mobiles[i]["price"] > 130000:
        print(i, mobiles[i]["model"])

# wap to get the mobile phone price greater than 150000 and black in color

for i in mobiles:
    if mobiles[i]["price"] > 150000 and mobiles[i]["color"] == "Black":
        print(i, mobiles[i]["model"])
