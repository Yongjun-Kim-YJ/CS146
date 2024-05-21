from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# nums1 = [2, 7, 11, 15]
# target1 = 8
# print(twoSum(nums1, target1))

# nums2 = [3, 2, 4]
# target2 = 6
# print(twoSum(nums2, target2))

# nums3 = [3, 3]
# target3 = 6
# print(twoSum(nums3, target3))
