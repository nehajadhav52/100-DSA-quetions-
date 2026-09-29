# Question 20: Calculate Sum of Odd Numbers

arr = [1, 2, 3, 4, 5, 6]

total = 0

for num in arr:
    if num % 2 != 0:
        total = total + num

print("Sum of odd numbers:", total)
