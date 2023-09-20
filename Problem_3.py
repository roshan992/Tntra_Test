# Function to find the maximum and minimum numbers in an array
def find_max_min(arr):
    if not arr:
        print("Array is empty.")
        return

    # Initialize max and min with the first element of the array
    max_num = min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print("Maximum is:", max_num)
    print("Minimum is:", min_num)

user_input = input("Enter numbers separated by spaces: ")

arr = [int(x) for x in user_input.split()]


find_max_min(arr)
