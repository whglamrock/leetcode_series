
class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        ans = []
        for directory in directories:
            if not directory or directory == '.':
                continue
            if directory == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(directory)

        return '/' + '/'.join(ans)


print(Solution().simplifyPath("/home/.../foo///blabla/../../or/.././../"))
