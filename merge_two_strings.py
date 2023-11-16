class Solution:
    def merge(self, word1, word2):
        res=''
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]

        return res + word1[i+1:] + word2[i+1:]
    
solution_instance = Solution()
word1 = 'sadflkajslkdj'
word2 = 'wewereiiieeeii'

# call the merge method on the instance
result = solution_instance.merge(word1, word2)
print(result)