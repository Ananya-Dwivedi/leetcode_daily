class Solution(object):
    def maximumGap(self, nums):
       

        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Size of each bucket
        bucket_size = (max_val - min_val + n - 2) // (n - 1)

        # Number of buckets
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Store min and max for every bucket
        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count

        # Put numbers into buckets
        for num in nums:

            index = (num - min_val) // bucket_size

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)

        # Find maximum gap between buckets
        max_gap = 0
        previous_max = min_val

        for i in range(bucket_count):

            # Skip empty bucket
            if bucket_min[i] == float("inf"):
                continue

            gap = bucket_min[i] - previous_max
            max_gap = max(max_gap, gap)

            previous_max = bucket_max[i]

        return max_gap
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna