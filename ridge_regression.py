from typing import List

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, k))
