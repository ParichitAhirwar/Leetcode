class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]
        for w in words:
            tw=sum(weights[ord(ch)-ord('a')]for ch in w)
            mod=tw%26
            res.append(chr(ord('z')-mod))
        return "".join(res)