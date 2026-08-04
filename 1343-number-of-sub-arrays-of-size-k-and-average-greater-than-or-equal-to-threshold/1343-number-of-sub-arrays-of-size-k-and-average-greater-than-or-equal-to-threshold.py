class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        arr_count=0
        window=arr[:k]
        current_sum=sum(window)
        current_avg=current_sum/k
        if current_avg>=threshold:
            arr_count+=1
        
        left=0
        for right in range(k,len(arr)):
            current_sum=current_sum-arr[left]+arr[right]
            if current_sum/k >= threshold:
                arr_count+=1
            left+=1
        return arr_count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna