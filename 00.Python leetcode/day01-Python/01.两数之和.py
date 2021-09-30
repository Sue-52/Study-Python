'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

------------------------
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
------------------------
 
提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
'''

# 方法一：暴力枚举（循环）
'''
最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。

当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配。
而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。
'''

from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if isinstance(nums, list) & isinstance(target, int):
            n = len(nums)
            for x in range(n):
                for y in range(x + 1, n):
                    if nums[x] + nums[y] == target:
                        return [x, y]
            return []


nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6
nums3 = [3, 3]
target3 = 6
test1 = Solution1()
print(test1.twoSum(nums1, target1))
print(test1.twoSum(nums2, target2))
print(test1.twoSum(nums3, target3))
'''
复杂度分析
时间复杂度：O(N^2)，其中 NN 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
空间复杂度：O(1)
'''

# 方法二：哈希表
'''
注意到方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。
因此，我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们需要找出它的索引。

使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N) 降低到 O(1)。

这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。
'''


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()  # 定义一个空的字典
        for i, num in enumerate(nums):  # enumerate 将一个可遍历的数据对象
            if target - num in hashTable:  # 判断 目标数值减去 num 是都在hashTable中
                return [hashTable[target - num], i]  # 返回 索引
            hashTable[nums[i]] = i
        return []


nums4 = [2, 7, 11, 15]
target4 = 9
nums5 = [3, 2, 4]
target5 = 6
nums6 = [3, 3]
target6 = 6
test2 = Solution2()
print(test2.twoSum(nums4, target4))
print(test2.twoSum(nums5, target5))
print(test2.twoSum(nums6, target6))
'''
复杂度分析

时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。
'''