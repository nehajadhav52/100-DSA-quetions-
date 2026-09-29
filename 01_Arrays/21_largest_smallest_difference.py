# Question 21: Difference Between Largest and Smallest

arr = [10, 25, 7, 40, 15]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

difference = largest - smallest

print("Difference:", difference)
