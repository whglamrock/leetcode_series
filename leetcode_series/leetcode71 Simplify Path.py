
# O(n) running time/space solution
# understand the unix style path: '..' means going above by one level.
# e.g., when the path is a/b/c, you type 'cd..' in cmd line, your current directory becomes a/b

class Solution(object):
    def simplifyPath(self, path):

        path = path.split('/')
        res = []
        for item in path:
            if not item or item == '.':
                continue
            if item == '..':
                if res:
                    res.pop()
            else:
                res.append(item)

        return '/' + '/'.join(res)



Sol = Solution()
path = "/a/./b/../../c/"
print Sol.simplifyPath(path)



'''
# another solution:

class Solution(object):
    def simplifyPath(self, path):

        paths = path.split('/')
        places = []
        for p in paths:
            if p != '' and p != '.':
                places.append(p)

        #print places

        stack = []
        for p in places:
            if p == '..':
                if stack: stack.pop()
            else:
                stack.append(p)
            #print stack

        return '/'+'/'.join(stack)

'''

