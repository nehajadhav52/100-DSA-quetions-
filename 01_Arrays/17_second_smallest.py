# Question 17: Find the Second Smallest Number

arr = [10, 25, 7, 40, 15]

smallest = arr[0]
second_smallest = arr[0]

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest number:", second_smallest)
