# Question 15: Calculate Sum of Even Numbers

arr = [1, 2, 3, 4, 5, 6]

total = 0

for num in arr:
    if num % 2 == 0:
        total = total + num

print("Sum of even numbers:", total)
