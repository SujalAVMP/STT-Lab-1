# Implement merge sort recursively

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        less = []
        greater = []

        for element in arr:
            if element <= pivot:
                less.append(element)
            else:
                greater.append(element)

        return quick_sort(less) + [pivot] + quick_sort(greater)
    

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print(f"Given array is {arr}")
    merge_sort(arr)
    print(f"Sorted array is {arr}")
    
    arr = [12, 11, 13, 5, 6, 7]
    print(f"Given array is {arr}")
    arr = quick_sort(arr)
    print(f"Sorted array is {arr}")