class Solution(object):
    def searchRange(self, nums, target):

        answer=[]
        
        if nums==[]:
            return [-1,-1]
        


        low = 0
        high = len(nums) - 1

        first = -1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] < target:

                low = mid + 1

            elif nums[mid] > target:

                high = mid - 1

            else:

                first = mid
                high = mid - 1

        answer.append(first)
    

        low = 0
        high = len(nums) - 1

        last = -1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] < target:

                low = mid + 1

            elif nums[mid] > target:

                high = mid - 1

            else:

                last = mid
                low = mid + 1

        answer.append(last)

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna