class Solution:
    def merge(self, word1, word2):
        res=''
        for i in range(min(len(word1), len(word2))): # min(...) ensures we only interate up to the length of the shortest word
            res += word1[i] + word2[i] # this concatenates each ith letter into res

        return res + word1[i+1:] + word2[i+1:] # this appends the rest of whichever word was longer
                                               # : goes to the end of the string 
solution_instance = Solution()
wordc = 'sadflkajslkdj'
wordi = 'wewereiiieeeii'

# call the merge method on the instance
result = solution_instance.merge(wordc, wordi)
print(result)