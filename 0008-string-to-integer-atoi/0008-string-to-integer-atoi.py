# BEST SOLUTION TO UNDERSTAND RECURSION PROPERLY.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        return self.clamp(int(self.preread(s)))
    
    def preread(self, s):
      if s == "":
        return "0"
      tail = s[1:] if len(s) > 1 else ""
      match s[0:1]:
        case " ":
          return self.preread(tail)
        case "+":
          return self.numread(tail, "+")
        case "-":
          return self.numread(tail, "-")
        case _:
          return self.numread(s, "")
    
    def numread(self, s, r):
      if s == "" and r in ["", "+", "-"]:
        return "0"
      if s == "":
        return r
      if s[0:1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        tail = s[1:] if len(s) > 0 else ""
        return self.numread(tail, r+s[0:1])
      if r in ["", "+", "-"]:
        return "0"
      return r
    
    def clamp(self, int):
      if int > 2147483647:
        return 2147483647
      if int < -2147483648:
        return -2147483648
      return int



"""
class Solution(object):
    def myAtoi(self, s):
        num = '0123456789'
        res = ''
        for x in s:
            if x == ' ' and len(res) == 0:
                continue
            if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
                res += x
            elif x in num:
                res += x
            else:
                break
        if res == '' or res in '-+':
            return 0
        else:
# to avoid int casting simply run a loop and use ord(char) - ord('0')
            if int(res) < -(2**31):
                return -(2**31)
            elif int(res) > (2**31 - 1):
                return (2**31 - 1)
            else:
                return int(res)