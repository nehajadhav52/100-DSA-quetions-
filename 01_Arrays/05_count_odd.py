# Question 5: Count Odd Numbers

arr = [1, 2, 3, 4, 5, 7]

count = 0

for num in arr:
    if num % 2 != 0:
        count = count + 1

print("Number of odd elements:", count)
