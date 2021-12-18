# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:

    # Brute Force Method
    # Time Complexity: O(n^2)
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     output = []
    #     numlen = len(nums)
    #     for i in range(0, numlen):
    #         for j in range(0, numlen):
    #             if nums[i] + nums[j] == target:
    #                 if len(output) == 0:
    #                     output.append(i)
    #                     output.append(j)
    #     return output

    # Efficient Version

    # Time Complexity: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = dict()
        numlen = len(nums)
        # We are going to populate the hash with all values as keys. The indexes will be the values.
        for x in range(0, numlen):
            hash[nums[x]] = x

        output = []
        for x in range(0, numlen):
            searchNum = target - nums[x]
            found = hash.get(searchNum)
            if found != None and found != x:
                return [x, found]


nums = [2, 7, 11, 15]
target = 17

sol = Solution()

result = sol.twoSum(nums, target)
print(result)
