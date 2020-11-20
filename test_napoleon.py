class Solution:
  def romanToInt(self, s: str) -> int:
    sl = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    if (len(s) >= 1) and (len(s) <= 15):
      for i in range(len(s)-1, -1, -1): # Steping in reverse order
          if ((s[i] in sl.keys()) and (s.count(s[i]) <= 3)): # Checking if entered inappropriate type of string 
            if i != len(s)-1:
              if (list(sl.keys()).index(s[i+1]) > list(sl.keys()).index(s[i])):
                if (s[i] != s[i-1]): # Checking if entered inappropriate type of string 
                  num = num - sl[s[i]]
                else:
                  return 0
              else:
                num = num + sl[s[i]]
            else:
              num = num + sl[s[i]]
          else: 
            return 0
    else:
      return 0
    return num

