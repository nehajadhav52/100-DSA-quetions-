# Question 14: Count Numbers Less Than 10

arr = [5, 15, 8, 20, 12, 3]

count = 0

for num in arr:
    if num < 10:
        count = count + 1

print("Numbers less than 10:", count)
