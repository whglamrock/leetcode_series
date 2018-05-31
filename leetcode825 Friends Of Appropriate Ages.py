
# refer to: https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127341/10ms-concise-Java-solution-O(n)-time-and-O(1)-space
#   for this O(n) idea

class Solution(object):
    def numFriendRequests(self, ages):

        ageCount = [0] * 121
        for age in ages:
            ageCount[age] += 1
        # how many people are equal or younger than an age
        ageCountSum = [0] * 121
        for i in xrange(1, 121):
            ageCountSum[i] = ageCountSum[i - 1] + ageCount[i]

        ans = 0
        # the condition for A to make friend with B can merge into:
        # B is in the range  (0.5 * A + 7, A]
        for A in ages:
            if A <= 0.5 * A + 7:    # such A cannot make friend
                continue
            bottom = int(0.5 * A + 7)
            numOfPeopleUnderA = ageCountSum[bottom]
            numOfPeopleAboveA = len(ages) - ageCountSum[A]
            # cannot make friend with A himself, so -1
            ans += len(ages) - numOfPeopleUnderA - numOfPeopleAboveA - 1

        return ans