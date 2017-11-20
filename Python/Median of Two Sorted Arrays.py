class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index_1 = 0
        index_2 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)
        even = 1 - ((len_1 + len_2) & 1)
        place = int((len_1 + len_2) / 2 + 0.5) + even
        last = []
        for i in range(place):
            if i > 1:
                last = [last[-1], ]
            if index_1 >= len_1:
                last.append(nums2[index_2])
                index_2 += 1
                continue
            if index_2 >= len_2:
                last.append(nums1[index_1])
                index_1 += 1
                continue
            if nums1[index_1] < nums2[index_2]:
                last.append(nums1[index_1])
                index_1 += 1
            else:
                last.append(nums2[index_2])
                index_2 += 1
        if even:
            return sum(last) / 2
        else:
            return last[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 3, 4, 5], [3, 4, 5, 6]))
