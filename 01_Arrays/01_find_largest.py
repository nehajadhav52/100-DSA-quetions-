# Question 1: Find the Largest Element in an Array

def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


arr = [10, 25, 7, 40, 15]

print("Array:", arr)
print("Largest element:", find_largest(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)
