# Question 16: Find the Second Largest Number

arr = [10, 25, 7, 40, 15]

largest = arr[0]
second_largest = arr[0]

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)
