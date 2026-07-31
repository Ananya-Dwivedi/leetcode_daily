class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans=[]
        freq_arr1={}

        for i in range(len(arr1)):
            freq_arr1[arr1[i]]=freq_arr1.get(arr1[i],0)+1

        for num in arr2:
            while freq_arr1[num]!=0:

                ans.append(num)
                freq_arr1[num]-=1

            
        for key in sorted(freq_arr1):
            
            while freq_arr1[key]>0:
                ans.append(key)
                freq_arr1[key]-=1
        
        return ans

    
        # for num in arr2:
        #     for nums in arr1:
        #         if nums==num:
        #             ans.append(nums)
        #             arr1.remove(nums)

        

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna