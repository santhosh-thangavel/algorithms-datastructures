# Find out if a key exists in the sorted list
# array[left..right] or not using binary search algorithm
def binary_search(arr, left, right, key):
    if left > right:
        return -1

    mid = left + right // 2
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, left, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, right, key)
    # Practise Yourself : write your code here
    # return None


if __name__ == '__main__':

    array = [2, 5, 6, 8, 9, 10]
    key = 5
    index = binary_search(array, 0, len(array) - 1, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")



