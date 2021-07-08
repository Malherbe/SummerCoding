def binarySearch(arr, start_index, end_index, search_value):
    if end_index >= start_index:
        mid = (end_index - start_index) + start_index // 2
        if arr[mid] == search_value:
            return mid
        elif arr[mid] > search_value:
            return binarySearch(arr, start_index, mid-1, search_value)
        else:
            return binarySearch(arr, mid+1, end_index, search_value)
    else:
        return -1

