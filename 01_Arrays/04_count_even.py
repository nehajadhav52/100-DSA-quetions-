# Question 4: Count Even Numbers

arr = [1, 2, 3, 4, 6]

count = 0

for num in arr:
    if num % 2 == 0:
        count = count + 1

print("Number of even elements:", count)
