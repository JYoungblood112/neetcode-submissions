class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k <= 0:
            return nums

        mod = len(nums)
        sol = [0] * len(nums)

        for i in range(len(nums)):
            sol[(i+k) % mod] = nums[i]

        nums[:] = sol
        return nums
        