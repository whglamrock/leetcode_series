class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        counter = 1
        string = '11'
        newstring = ''

        if n == 1:
            return '1'

        if n == 2:
            return '11'

        for i in range(2,n):
            newstring = ''
            counter = 1

            for j in range(len(string)-1):

                if string[j] == string[j+1] and j+1 != len(string)-1:
                    counter += 1

                if string[j] != string[j+1]:
                    newstring += str(counter)
                    newstring += string[j]
                    counter = 1
                    if j+1 == len(string)-1:
                        newstring += str(counter)
                        newstring += string[j+1]
                elif j+1 == len(string)-1:
                    counter += 1
                    newstring += str(counter)
                    newstring += string[j+1]

            string = newstring

        return newstring

a = Solution()
b = a.countAndSay(7)
print b








