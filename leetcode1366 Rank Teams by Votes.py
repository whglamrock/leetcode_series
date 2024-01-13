from functools import cmp_to_key
from typing import List

class Solution:
    def __init__(self):
        self.teamToRankedVotes = {}

    def rankTeams(self, votes: List[str]) -> str:
        self.teamToRankedVotes = {}
        for vote in votes:
            for rank, team in enumerate(vote):
                if team not in self.teamToRankedVotes:
                    self.teamToRankedVotes[team] = [0] * len(vote)
                self.teamToRankedVotes[team][rank] += 1

        teams = sorted(self.teamToRankedVotes.keys(), key=cmp_to_key(self.compare))
        return ''.join(teams)

    def compare(self, a: int, b: int):
        rankRange = len(list(self.teamToRankedVotes.values())[0])
        for rank in range(rankRange):
            if self.teamToRankedVotes[a][rank] < self.teamToRankedVotes[b][rank]:
                return 1
            elif self.teamToRankedVotes[a][rank] > self.teamToRankedVotes[b][rank]:
                return -1
        return 1 if a > b else -1


print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
print(Solution().rankTeams(["WXYZ", "XYZW"]))
print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
print(Solution().rankTeams(
    ["FVSHJIEMNGYPTQOURLWCZKAX", "AITFQORCEHPVJMXGKSLNZWUY", "OTERVXFZUMHNIYSCQAWGPKJL", "VMSERIJYLZNWCPQTOKFUHAXG",
     "VNHOZWKQCEFYPSGLAMXJIUTR", "ANPHQIJMXCWOSKTYGULFVERZ", "RFYUXJEWCKQOMGATHZVILNSP", "SCPYUMQJTVEXKRNLIOWGHAFZ",
     "VIKTSJCEYQGLOMPZWAHFXURN", "SVJICLXKHQZTFWNPYRGMEUAO", "JRCTHYKIGSXPOZLUQAVNEWFM", "NGMSWJITREHFZVQCUKXYAPOL",
     "WUXJOQKGNSYLHEZAFIPMRCVT", "PKYQIOLXFCRGHZNAMJVUTWES", "FERSGNMJVZXWAYLIKCPUQHTO", "HPLRIUQMTSGYJVAXWNOCZEKF",
     "JUVWPTEGCOFYSKXNRMHQALIZ", "MWPIAZCNSLEYRTHFKQXUOVGJ", "EZXLUNFVCMORSIWKTYHJAQPG", "HRQNLTKJFIEGMCSXAZPYOVUW",
     "LOHXVYGWRIJMCPSQENUAKTZF", "XKUTWPRGHOAQFLVYMJSNEIZC", "WTCRQMVKPHOSLGAXZUEFYNJI"]))
print(Solution().rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))
