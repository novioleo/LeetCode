# https://leetcode.com/problems/container-with-most-water/description/
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_size = 0
        while l < r:
            cur_size = (r-l)*(height[l] if height[l] < height[r] else height[r])
            if cur_size > max_size:
                max_size = cur_size
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_size

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,2,1]))