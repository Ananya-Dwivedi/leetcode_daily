class Solution(object):
    def trap(self, height):

            #brute force --> O(n^2)
            # answer=0
            # for i in range(len(height)):
            #     left_max=max(height[:i+1])
            #     right_max=max(height[i:])
            #     max_water=min(left_max,right_max)-height[i]

            #     answer+=max_water

            # return answer


            #suffix and prefix array


            # left_max=[0]*len(height)
            # left_max[0]=height[0]
            # for i in range(len(height)):
            #     left_max[i]=max(left_max[i-1],height[i])
            # right_max=[0]*len(height)
            # right_max[-1]=height[-1]
            # for i in range(len(height)-2,-1,-1):
            #     right_max[i]=max(right_max[i+1],height[i])

            # max_water = 0

            # for i in range(len(height)):
            #     max_water += min(left_max[i], right_max[i]) - height[i]
              

            # return max_water  


 

        if not height:
            return 0

        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        water = 0

        while left < right:

            if leftMax < rightMax:

                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]

            else:

                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]

        return water      
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna