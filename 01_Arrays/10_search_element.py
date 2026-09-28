# Question 10: Search for a Number

arr = [10, 20, 30, 40, 50]

search = 30

found = False

for num in arr:
    if num == search:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
