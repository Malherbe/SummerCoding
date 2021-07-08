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

arr = [2,5,8,12,16,23,38,56,72]
x = 23

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("sa wap cheche a nan endeks", result)
else:
    print("sa wap cheche a pa genyen'l")