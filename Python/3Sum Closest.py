# https://leetcode.com/problems/3sum-closest/description/
#
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum_value = nums[i] + nums[j] + nums[k]
                if sum_value == target:
                    return sum_value

                if abs(sum_value - target) < abs(result - target):
                    result = sum_value

                if sum_value < target:
                    j += 1
                elif sum_value > target:
                    k -= 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4],1))
