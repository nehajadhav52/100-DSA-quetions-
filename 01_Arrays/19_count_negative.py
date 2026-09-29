# Question 19: Count Negative Numbers

arr = [-5, 10, -2, 8, 0, -15]

count = 0

for num in arr:
    if num < 0:
        count = count + 1

print("Negative numbers:", count)
