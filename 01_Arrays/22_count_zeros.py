# Question 22: Count Zeros in an Array

arr = [0, 5, 0, 10, 3, 0]

count = 0

for num in arr:
    if num == 0:
        count = count + 1

print("Number of zeros:", count)
