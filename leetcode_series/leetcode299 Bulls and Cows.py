
class Solution(object):
    def getHint(self, secret, guess):

        dick1 = {}
        dick2 = {}
        bulls = 0
        cows = 0

        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                continue
            if secret[i] not in dick1:
                dick1[secret[i]] = [i]
            else:
                dick1[secret[i]].append(i)
            if guess[i] not in dick2:
                dick2[guess[i]] = [i]
            else:
                dick2[guess[i]].append(i)


        for item in dick1:
            if item not in dick2:
                continue
            cows += min(len(dick1[item]),len(dick2[item]))

        return str(bulls) + 'A' + str(cows) + 'B'



Sol = Solution()
secret = '1807'
guess = '7810'
print Sol.getHint(secret,guess)










