
class Solution(object):
    def specialTriplets(self, nums):
        
        n = len(nums)
        if n < 3:
            return 0

        MAX_VAL = 100001
        MOD = 10**9 + 7

        total_counts = [0] * MAX_VAL
        for num in nums:
            if num < MAX_VAL:
                total_counts[num] += 1

        left_counts = [0] * MAX_VAL
        ans = 0

        for j in range(n):
            val_j = nums[j]

            if val_j < MAX_VAL:
                total_counts[val_j] -= 1

            target = val_j * 2
            if target < MAX_VAL:
                count_i = left_counts[target]
                count_k = total_counts[target]
                ans = (ans + count_i * count_k) % MOD

            if val_j < MAX_VAL:
                left_counts[val_j] += 1

        return ans