class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        to_return = 0
        temp = ""

        for i in s:
            if i in temp:
                if len(temp) > to_return:
                    to_return = len(temp)
                
                temp = temp[temp.index(i)+1:] + i
            else:
                temp += i

        if len(temp) > to_return:
            return len(temp)

        return to_return
