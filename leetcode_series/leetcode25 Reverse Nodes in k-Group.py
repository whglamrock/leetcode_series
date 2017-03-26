
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):

        def reverse(node0, node1, n): # e.g., if k = 4, the lists became 4->3->2->1->5->6->7->8->9,
            current = node1           # the node0 is 1, the node1 is 5
            preceding = node0
            if node0.val == None:
                preceding.next = current # in the first round of the recursion,connect the newly defined
                # node0 to the head
            else:
                tail = preceding  # mark the node0, which will be used for next round of recursion

            if n == k+1:
                return preceding  # in the last round of recursion, return the node preceding the last "head"

            for i in range(n-1):  # move the 'preceding' and 'current' to where the swap is needed
                current = current.next
                preceding = preceding.next

            if node0.val != None:
                preceding.next = current.next
                current.next = node1
                tail.next = current  # e.g. in 4->3->2->1->5->6->7->8->9, '1' is before '5', when swapping
                # '5' and '6', the '1' needs to reconnect to '6'
            else:
                preceding.next = current.next # e.g. in 1->2->3->4->5->6->7->8->9, there is no nodes before
                current.next = node1 # '1', which is the case when node.val = None

            if node0.val != None:
                return reverse(tail,current,n+1)
            else:
                return reverse(ListNode(None),current,n+1) # for the first round of recursion

        # check if there are enough remaining nodes for swap
        def judge(node):
            temp = node
            counter = 0
            while temp:
                temp = temp.next
                counter += 1
            if counter < k:
                return False
            else:
                return True

        if judge(head) == False:
            return head

        temp = ListNode(None)
        temp.next = head
        marker = 1
        while temp and judge(temp.next):
            temp = reverse(temp,temp.next,2) #the 'n' always starts with 2 because it's recursive and it
            # will finally return the lists after one round of k-node swap.
            if marker == 1:
                res = temp # we only need the new 'head' after the first round of swap, which will be the
                # final head of completely swapped lists.
            for i in range(k):
                temp = temp.next # after each round of swap, it needs to pass the swapped nodes
            marker +=1 # just to prevent from assigning a new value to res.

        return res.next



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

Sol = Solution()
res = Sol.reverseKGroup(a,2)
print res.val
print res.next.val
print res.next.next.val
print res.next.next.next.val
print res.next.next.next.next.val
print res.next.next.next.next.next.val






