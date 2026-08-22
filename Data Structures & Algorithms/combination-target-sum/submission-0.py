class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        curr=[]
        sol=[]
        def bt(start):
            if sum(curr) == target:
                sol.append(curr.copy())
                return
            if sum(curr) > target:
                return

            for i in range(start, len(nums)):

                curr.append(nums[i])

                bt(i)

                curr.pop()

            return 
        
        bt(0)

        return sol
            
        



        

        

        
        