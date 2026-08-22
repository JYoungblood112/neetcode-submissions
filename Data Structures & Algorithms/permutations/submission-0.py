class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        curr = []
        sol = []

        def bt():

            if len(curr) == len(nums):
                sol.append(curr.copy())
                return

            for i in range(len(nums)):

                if nums[i] in curr:
                    continue

                curr.append(nums[i])

                bt()

                curr.pop()

        bt()

        return sol