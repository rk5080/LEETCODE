class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                a = st.pop()
                if (i == ')' and a =='(') or (i == '}' and a == '{') or (i == ']' and a=='['):
                    continue
                else:
                    return False
        return len(st)==0