class Solution:
    def romanToInt(self, s: str) -> int:
        romans = ['I','V','X','L','C','D','M']
        int_val = [1,5,10,50,100,500,1000]
        con_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        c = 0
        n = len(s)
        for i in range(n):
            if i<n-1 and con_val[s[i]]<con_val[s[i+1]]:
                c -= con_val[s[i]]
            else:
                c += con_val[s[i]]

        return c
