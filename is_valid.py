import queue

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False
        stack = queue.LifoQueue()
        i = 0
        opens = ['(', '[', '{']
        par = '()'
        br = '[]'
        cr = '{}'
        while i < len(s):
            if s[i] in opens:
                stack.put(s[i])
                i += 1
                continue
            else:
                if stack.empty():
                    return False
                o = stack.get()
                if o in par and s[i] in par:
                    i += 1
                    continue
                elif o in br and s[i] in br:
                    i += 1
                    continue
                elif o in cr and s[i] in cr:
                    i += 1
                    continue
                else:
                    return False
        return stack.empty()





