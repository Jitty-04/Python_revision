scores = {
    "arun": [85, 90, 92],
    "hari": [74, 81, 78],
    "vinay": [65, 75, 70],
    "sajay": [90, 87, 98]
}

# o/p= highest avg mark

largest = 0

for i, j in scores.items():
    avg = sum(j) / len(j)

    if avg > largest:
        largest = avg
        element = i

print(f'{element} has highest avg, avg is {largest}')
