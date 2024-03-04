class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ('.' in queryIP and ':' in queryIP) or ('.' not in queryIP and ':' not in queryIP):
            return 'Neither'

        if '.' in queryIP:
            ipv4Tokens = queryIP.split('.')
            if len(ipv4Tokens) != 4:
                return 'Neither'
            for ipv4Token in ipv4Tokens:
                if not self.isValidIpv4Token(ipv4Token):
                    return 'Neither'
            return "IPv4"
        else:
            ipv6Tokens = queryIP.split(':')
            if len(ipv6Tokens) != 8:
                return 'Neither'
            for ipv6Token in ipv6Tokens:
                if not self.isValidIpv6Token(ipv6Token):
                    return 'Neither'
            return "IPv6"

    def isValidIpv4Token(self, ipv4Token: str) -> bool:
        if not (1 <= len(ipv4Token) <= 3):
            return False
        # leading 0
        if len(ipv4Token) > 1 and ipv4Token[0] == '0':
            return False
        for char in ipv4Token:
            if not char.isdigit():
                return False
        return int(ipv4Token) < 256

    def isValidIpv6Token(self, ipv6Token: str) -> bool:
        if not (1 <= len(ipv6Token) <= 4):
            return False
        for char in ipv6Token:
            if not char.isdigit() and char not in 'abcdefABCDEF':
                return False
        return True

