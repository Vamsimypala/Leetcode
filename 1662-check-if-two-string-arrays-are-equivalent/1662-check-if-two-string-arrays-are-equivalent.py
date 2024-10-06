class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1s=""
        w2s=""
        for i in range(len(word1)):
            w1s+=word1[i]
        for i in range(len(word2)):
            w2s+=word2[i]  
        if w1s==w2s:
            return True
        else:
            return False
        
                
                                                                              