
# so many corner cases. In real interview, we need to consider them thoroughly.

class Solution(object):
    def validIPAddress(self, IP):

        if not IP or len(IP) == 0:
            return "Neither"

        if '.' in IP:
            nums = IP.split('.')
            if len(nums) != 4: return 'Neither'
            for num in nums:
                if not num: return 'Neither'
                # this if statement meant to avoid the "len(num.lstrip('0')) != len(num)" check
                if num == '0': continue
                for char in num:
                    if not ('0' <= char <= '9'):
                        return 'Neither'
                if not (0 <= int(num) < 256) or (len(num.lstrip('0')) != len(num)):
                    return 'Neither'
            return "IPv4"

        elif ':' in IP:
            nums = IP.split(':')
            if len(nums) != 8: return 'Neither'
            for num in nums:
                if not num or len(num) > 4: return 'Neither'
                for char in num:
                    if not ('0' <= char <= '9') and not('a' <= char <= 'f') and not ('A' <= char <= 'F'):
                        return 'Neither'
            return 'IPv6'

        else:
            return 'Neither'

