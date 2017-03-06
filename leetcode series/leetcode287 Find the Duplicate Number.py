# the idea is consider the array as a linked list and use fast & slow pointers
# to find circle. P.S., when they meet, it could any point inside the circle, not
# necessarily the duplicate number.

# How the aray can be considered as linked list?
# consider the index as the node, the value as the next node.
# e.g., index: 0 1 2 3 4 5 6 7 8 9
#       value: 3 2 5 6 1 2 8 9 7 4
# linked list: 0->3->6->8->7->9->4->1->2->5->2, circle: 2->5->2
# P.S.: WE HAVE TO START FROM nums[0] TO FIND THE CIRCLE THAT CONTAINS DUPLICATES.
# consider such index/value pairs:
#    1 3 2 6 8
#    3 2 6 8 1
# all values are unique, but they can also form a circle: 1->3->2->6->8->1, which
# doesn't have anything to do with other elements in the array. If such circle
# doesn't contain the duplicate number, the fast slow will never enter it when the start
# point is nums[0]. If we start from nums[1], and nums[1] are in such circle, the second
# while loop will becomes an infinite loop.

# WHY STARTING FROM nums[0] GUARANTEES WE FIND THE DUPLICATE?
# Because if the index of nums[0] is ZERO and in the linked list NO node's next is zero.
# Since the number of indices == number of values, we consider the index/value pairs:
#     0 a b c y x z
#     a b c y x z x
# when all unique values are used up to fill the "node's next", the z has no other choice
# but to pick a used value when duplicate occurs and circle forms!
# so if we start from nums[0], we will always find a circle that forms because of duplicates.
# However, the first while loop will never be an infinite loop because it will always find
# a circle. It's just a matter of whether it contains the duplicates.

class Solution(object):
    def findDuplicate(self, nums):

        if len(nums) > 1:
            slow = nums[0]  # it has to start from nums[0].
            fast = nums[nums[0]]

            # the duplicate the is entry/start point of circle.
            # find the circle, but the slow, fast doesn't necessarily meet at the entry point
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
                fast = nums[fast]
                # when exits the while loop, the slow, fast could be the same number (same index)
                # but we need to find the duplicates (with different indices)

            # assume the distance between entry point and meet point is y and
            # the distance from nums[0] to entry point is x; assume the perimeter of circle is C.
            # we can have x + C + y = 2 * (x + y) -- fast pointer went 2 times far of slow pointer
            # So, C = x + y.
            fast = 0
            while slow != fast:
                fast = nums[fast]
                slow = nums[slow]
            # in the above while loop, the two pointers both went through x and they meet at
            # the entry point. The slow starts from the meet point which is y from entry point,
            # and went through part of the circle to entry point (the distance is C - y, which = x)

            return slow

        return -1


Sol = Solution()
nums = [3, 1, 2, 4, 4]
print Sol.findDuplicate(nums)

