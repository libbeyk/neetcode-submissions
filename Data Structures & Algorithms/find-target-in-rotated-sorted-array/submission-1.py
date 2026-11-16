class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_side, right_side = 0, len(nums) - 1
        while left_side <= right_side:
            middle = (left_side + right_side) // 2
            if nums[middle] == target:
                return middle
            if nums[left_side] <= nums[middle]:
                if nums[left_side] <= target < nums[middle]:
                    right_side = middle - 1
                else:
                    left_side = middle + 1
            else:
                if nums[middle] < target <= nums[right_side]:
                    left_side = middle + 1
                else:
                    right_side = middle - 1
        return -1