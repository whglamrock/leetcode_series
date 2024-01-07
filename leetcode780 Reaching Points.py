# searching backwards. O(log(n)) where n = max(tx, ty).
# See: https://leetcode.com/problems/reaching-points/solutions/375429/detailed-explanation-full-through-process-java-100-beat/
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # using tx % ty not tx - ty is for speeding up the search. remember there is ONLY one way from end to start
        # e.g., tx >> ty, you will have to keep doing tx - ty until tx < ty
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

        # either ty = sy + k * sx or tx = sx + k * sy where k is an integer
        return (sx == tx and sy <= ty and (ty - sy) % sx == 0) or (sy == ty and sx <= tx and (tx - sx) % sy == 0)


print(Solution().reachingPoints(sx=1, sy=1, tx=3, ty=5))
print(Solution().reachingPoints(sx=1, sy=1, tx=2, ty=2))
print(Solution().reachingPoints(sx=1, sy=1, tx=1, ty=1))
print(Solution().reachingPoints(sx=10, sy=20, tx=10, ty=90))
print(Solution().reachingPoints(sx=10, sy=20, tx=30, ty=90))
