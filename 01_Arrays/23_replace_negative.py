# Question 23: Replace Negative Numbers With Zero

arr = [5, -2, 8, -7, 10]

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0

print("Updated array:", arr)
