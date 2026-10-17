lst = ['red', 10, 'blue', 20, 30, 'green']

colours = []
numbers = []

for item in lst:
    if isinstance(item, str):
        colours.append(item)
    elif isinstance(item, (int, float)):
        numbers.append(item)

print("Colours:", colours)
print("Numbers:", numbers)