class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=''
        w1c=0
        w2c=0
        for i in range(0,len(word1)):
            n+=word1[i]
            w1c+=1
            for j in range(i,len(word2)):
                n+=word2[i]
                w2c+=1
                break
        n+=(word1[w1c:]+word2[w2c:])
        
        return n
            
        