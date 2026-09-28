# Question 11: Find the Largest Number

arr = [12, 45, 7, 23, 56]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest number:", largest)
