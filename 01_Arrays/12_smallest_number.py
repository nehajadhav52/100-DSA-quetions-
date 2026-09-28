# Question 12: Find the Smallest Number

arr = [12, 45, 7, 23, 56]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
