class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        hash_set = {} # dictionary
        res = []

        def combinationRes(candidates,target,ind,temp):
            if target<0 or ind>len(candidates)-1:
                return 
            if target == 0:
                res.append(temp[:])
                return

            # pick 
            temp.append(candidates[ind])
            combinationRes(candidates,target-candidates[ind],ind+1,temp)

            # not pick
            temp.pop()
            combinationRes(candidates,target,ind+1,temp)
            return 

        ind = 0
        temp = []
        combinationRes(candidates,target,ind,temp)
        # hash_set = {}
        # for st in res:
        #     if st not in hash_set:
        #         hash_set[st.sort()]
        # return hash_set
        hash_set = set()
        final_res = []
        for i in res:
            i.sort()
        for i in res:
            chk = tuple(i)
            if chk not in hash_set:
                hash_set.add(chk)
                final_res.append(i)
        return final_res

    
sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
print(sol.combinationSum2(candidates,target))