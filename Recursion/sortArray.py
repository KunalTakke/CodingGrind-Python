# Sort array using Recursion 
def sortArray(arr): # 1,5,0,2
    if len(arr) == 1:
        return
    temp = arr.pop() # temp has 2 
    sortArray(arr) # reduce the size of the array 
    arrayInsert(arr,temp)
    # 

    # call the insert function 

def arrayInsert(arr,temp):
    if len(arr) == 0 or temp>=arr[-1]:
        arr.append(temp)
        return 
    val = arr.pop()
    arrayInsert(arr,temp)
    arr.append(val)


arr = [2,4,1,3,5,7]
sortArray(arr)
print(arr)