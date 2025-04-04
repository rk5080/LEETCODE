class Solution(object):
    def isIsomorphic(self, s, t):
        map_s = {}
        map_t = {}
    
        for i in range(len(s)):
            if s[i] in map_s and t[i] not in map_t:
                return False
            if s[i] not in map_s and t[i] in map_t:
                return False
        
            if s[i] not in map_s and t[i] not in map_t:
                map_s[s[i]] = i
                map_t[t[i]] = i
            else:
                if map_s[s[i]] != map_t[t[i]]:
                    return False
                
        return True