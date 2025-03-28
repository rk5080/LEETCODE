def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)
class Solution(object):
    def generate(self, numRows):
        """
        n = numRows
        l = []
        for i in range(1,n+1):
            l1 = [1]*i
            if len(l1)<=2:
                l.append(l1)
            for j in range(1,len(l1)-1):
                l1[j]=l[i-2][j-1]+l[i-2][j]
                if l1 not in l:
                    l.append(l1)
        return l
        """
        ans = []
        n = numRows

    #Store the entire pascal's triangle:
        for row in range(1, n+1):
            tempLst = [] # temporary list
            for col in range(1, row+1):
                tempLst.append(nCr(row - 1, col - 1))
            ans.append(tempLst)
        return ans