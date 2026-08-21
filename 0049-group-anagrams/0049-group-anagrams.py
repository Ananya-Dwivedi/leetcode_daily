class Solution(object):
    def groupAnagrams(self, strs):
        group={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in group:
                group[key]=[]
            group[key].append(word)
        return list(group.values())


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna