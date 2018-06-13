#! Python 3

# Find the largest palindrome product of two 3 digit numbers

MaxPal = 0

for x in range(100, 1000):
    for y in range (100, 1000):
        product = x * y
        if str(product) == str(product)[::-1] and product > MaxPal:
            MaxPal = product

print(MaxPal)
