
# this question isn't that straightforward if we want to write clean code with no redundant data structures

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # it's guaranteed that both lists will have at least 1 element

        restaurantsToIndex1 = {}
        for i, restaurant in enumerate(list1):
            restaurantsToIndex1[restaurant] = i

        maxIndexSum = 2147483647
        ans = []
        for j, restaurant in enumerate(list2):
            if restaurant in restaurantsToIndex1:
                i = restaurantsToIndex1[restaurant]
                if i + j == maxIndexSum:
                    ans.append(restaurant)
                elif i + j < maxIndexSum:
                    maxIndexSum = i + j
                    ans = [restaurant]

        return ans