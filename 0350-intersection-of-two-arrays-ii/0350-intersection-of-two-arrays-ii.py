class Solution(object):
    def intersect(self, nums1, nums2):
        ans=[]
        dict1={}
        dict2={}
        for i in range(len(nums1)):
            dict1[nums1[i]]=dict1.get(nums1[i],0)+1
        for i in range(len(nums2)):
            dict2[nums2[i]]=dict2.get(nums2[i],0)+1

        for key in dict1:
            if key in dict2:
                if dict1[key]<dict2[key]:
                    k=dict1[key]
                else:
                    k=dict2[key]
            
                for i in range(k):
                    ans.append(key)
        return ans

            




        # i=0
        # j=0
        # ans=[]
        # while i <=len(nums2):
        #     if nums1[i]==nums2[j]:
        #         ans.append(nums1[i])
        #         j+=1

        #     i+=1
        # return ans

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna