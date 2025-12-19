# Two Sum
def bruteForce(nums,target): # O(n^2)
    # nums = [1,3,4]
    # target = 4 
    # return indices [0,1]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

def optimized(nums,target): # TC->O(n),SC->O(n)
    complement_dictionary  = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in complement_dictionary:
            return [complement_dictionary[complement],i]
        else:
            complement_dictionary[nums[i]] = i



if __name__ == "__main__":
    tests = []
    test1 = {
        'input':{
            'nums':[2,7,11,15],
            'target':9
        },
        'output': [0,1]
        }
    
    test2 = {
        'input':{
            'nums':[3,2,4],
            'target':6
        },
        'output': [1,2]
        }
    
    test3 = {
        'input':{
            'nums':[3,3],
            'target':6
        },
        'output': [0,1]
        }
    
    tests.append(test1)
    tests.append(test2)
    tests.append(test3)

    counter = 1
    for t in tests:
        if t['output'] == optimized(t['input']['nums'],t['input']['target']):
            print(f"Testcase {counter} Passed")
        else:
            print(f"Testcase {counter} Failed")
        counter+=1

    
