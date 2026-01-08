def subset_sum_recursive(arr:int, sum: int):
    # base condition
    if sum == 0:
        return True 
    
    # recursive call 



def subset_sum_memo(arr:int,sum:int):
    pass 


def subset_sum_top_down(arr: int, sum: int):
    dp = [[0 for _ in range(sum+1)] for _ in range(len(arr)+1)]
    # initialization of the dp
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True


    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if dp[i][j] <= sum:
                pass 
            
                



# # arr = [2,3,7,8,10]
# sum = 11
# subset_sum(arr,sum)