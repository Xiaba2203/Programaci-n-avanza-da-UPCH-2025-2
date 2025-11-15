def quickSortMid(arr):
    quickSortMidHelper(arr, 0, len(arr) - 1)

def quickSortMidHelper(arr, low, high):
    if low < high:
        split = partitionMid(arr, low, high)
        quickSortMidHelper(arr, low, split - 1)
        quickSortMidHelper(arr, split + 1, high)

def partitionMid(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]

    arr[low], arr[mid] = arr[mid], arr[low]

    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right
print("Prueba QuickSort Mid")
data = [54,26,93,17,77,31,44,55,20]
quickSortMid(data)
print(data)