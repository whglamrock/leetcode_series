
class Solution(object):
    def intersect(self, nums1, nums2):

        dick1, dick2 = {}, {}
        for i in xrange(max(len(nums1),len(nums2))):
            if nums1:
                if nums1[0] not in dick1:
                    dick1[nums1[0]] = 1
                    nums1.pop(0)
                else:
                    dick1[nums1[0]] += 1
                    nums1.pop(0)
            if nums2:
                if nums2[0] not in dick2:
                    dick2[nums2[0]] = 1
                    nums2.pop(0)
                else:
                    dick2[nums2[0]] += 1
                    nums2.pop(0)

        ans = []
        if len(dick1) < len(dick2):
            for item in dick1:
                if item in dick2:
                    for i in xrange(min(dick1[item],dick2[item])):
                        ans.append(item)
        else:
            for item in dick2:
                if item in dick1:
                    for i in xrange(min(dick1[item],dick2[item])):
                        ans.append(item)

        return ans



Sol = Solution()
print Sol.intersect([1,2,2,1],[2,3,2])
