class Solution:
    
    def combination_sum(self,candidates,target):
        self.result = []
        current_sum = 0
        temp = []
        ind = 0
        self.findCombinationSum(candidates,target,current_sum,temp,ind)
        print(self.result)  

    def findCombinationSum(self,candidates, target, current_sum,temp,ind):
        # base condition 
        if current_sum > target or ind>len(candidates)-1:
            return 
        if current_sum == target:
            self.result.append(temp[:])
            return 
        
        
        # Take 
        current_sum+=candidates[ind]
        temp.append(candidates[ind])
        self.findCombinationSum(candidates,target,current_sum,temp,ind)
        
        # not Take
        current_sum-=candidates[ind]
        temp.pop()
        self.findCombinationSum(candidates,target,current_sum,temp,ind+1)

        return



sol = Solution()
candidates = [2,3,6,7]
target = 7
sol.combination_sum(candidates,target)