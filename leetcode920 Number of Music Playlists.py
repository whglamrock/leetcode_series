# Check: https://leetcode.com/problems/number-of-music-playlists/solutions/180338/dp-solution-that-is-easy-to-understand/
# dp[i][j] means the num of playlists that contain i (the goal) songs with j different songs
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for j in range(n + 1)] for i in range(goal + 1)]
        # We need to set dp[0][0] = 1 for later calculation.
        # It also fits the state transfer formula (think about dp[1][1])
        dp[0][0] = 1

        for i in range(1, goal + 1):
            # dp[0][j] = 0 makes sure each song is played at least once.
            # things like dp[1][2], dp[2][3] will be 0. this means all dp[i][j]
            # where i < j will be 0.
            for j in range(1, min(n + 1, i + 1)):
                dp[i][j] = (dp[i - 1][j - 1] * (n - (j - 1))) % mod
                if j > k:
                    # for a playlist of i - 1 songs with j different songs, we need to generate the new
                    # playlist of i songs (choose one more song). The last k songs in dp[i - 1][j] can't be chose,
                    # and it's guaranteed that there are NO DUPLICATE songs in the last k songs of each playlist.
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod

        return dp[-1][-1]


print(Solution().numMusicPlaylists(n=3, goal=3, k=1))
print(Solution().numMusicPlaylists(n=2, goal=3, k=0))
print(Solution().numMusicPlaylists(n=2, goal=3, k=1))
