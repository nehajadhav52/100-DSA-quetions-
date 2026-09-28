# Question 2: Find the Smallest Number

arr = [10, 25, 7, 40, 15]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
