class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        res=[]
        pf=""
        for ch in searchWord:
            pf+=ch
            sugg=[]
            for p in products:
                if p.startswith(pf):
                    sugg.append(p)
                if len(sugg)==3:
                    break
            res.append(sugg)
        return res