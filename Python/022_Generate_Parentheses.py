class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        
        res = []
        s, left, right = '(', n-1, n
        stack = []
        while s or stack:
            if s:
                if not left:
                    s += ')'
                    right -= 1
                else:
                    if left < right:
                        stack.append((s, left, right))
                    s += '('
                    left -= 1
                if not left and not right:
                    res.append(s)
                    s, left, right = '', None, None
            else:
                s, left, right = stack.pop()
                s += ')'
                right -= 1
            
        return set(res)
            
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res, stack = [], []
        s, left, right = '(', n-1, n
        while True:
            if left < right:
                stack.append((s+')', left, right-1))
            if left:
                s += '('
                left -= 1
            else:
                if not stack:
                    return res
                s, left, right = stack.pop()
                if not right:
                    res.append(s)
                    left = right = 0
  
if __name__ == "__main__":
    from leetcodelib import test
    arguments = [3]
    answers = [set(["((()))","(()())","(())()","()(())","()()()"])]
    test(Solution().generateParenthesis, arguments, answers)