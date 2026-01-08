def merge(arr,low,mid,high):
    left = low
    right = mid+1
    # create a temp array 
    temp = []
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    # if one of them gets over
    while left<=mid:
        temp.append(arr[left])
        left+=1

    while right<=high:
        temp.append(arr[right])
        right+=1
    
    # insert in original array
    for i in range(low,high+1):
        arr[i] = temp[i-low]


def mergeSort(arr,low,high):
    
    # base case 
    if low==high:
        return 
    # low = 0 
    # high= len(arr)-1
    mid = (low+high)//2
    # Divide
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)

    # Merge
    merge(arr,low,mid,high)


arr = [3,2,4,1,3]
low = 0 
high= len(arr)-1
mergeSort(arr,low,high)
print(arr)