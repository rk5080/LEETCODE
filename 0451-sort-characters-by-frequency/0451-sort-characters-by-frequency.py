class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = {}
        e = ""
        k1,v1 = [],[]
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for k in a:
            k1.append(k)
            v1.append(a[k])
        while v1:
            d = k1[v1.index(max(v1))]
            e += max(v1)*d
            v1.pop(v1.index(max(v1)))
            k1.pop(k1.index(d))
        return e
