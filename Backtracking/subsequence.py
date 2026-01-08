

def subsequence(ind, arr,arr1, curr_sum,target_sum):

    if ind == len(arr):
        if curr_sum == target_sum:
            print(arr1)
        return 
    
    # Take
    arr1.append(arr[ind])
    curr_sum+=arr[ind]
    subsequence(ind+1,arr,arr1,curr_sum,target_sum)

    # Not Take 
    # we remove first
    arr1.pop()
    curr_sum-=arr[ind]
    subsequence(ind+1,arr,arr1,curr_sum,target_sum)



arr = [1,2,1]
target_sum = 2 
arr1 = []
subsequence(0,arr,arr1,0,target_sum)