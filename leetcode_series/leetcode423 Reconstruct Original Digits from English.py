
# zero, one, two, three, four, five, six, seven, eight, nine
# order:
# z is unique (zero);
# x is unique (six);
# g is unique (eight);
# u is unique (four);
# w is unique (two);
# f is unique (five, after removing four);
# s is unique (seven, after removing five);
# r is unique (three, after removing four);
# o is unique (one, after removing zero, four, two);
# i is unique (nine, after removing all above);

class Solution(object):
    def originalDigits(self, s):

        dick = {}
        nums = [0 for i in xrange(10)]
        for letter in s:
            if letter not in dick:
                dick[letter] = 1
            else:
                dick[letter] += 1

        if 'z' in dick and dick['z'] != 0:  # zero
            deduction = dick['z']
            nums[0] = deduction
            del dick['z']
            dick['e'] -= deduction
            dick['r'] -= deduction
            dick['o'] -= deduction

        if 'x' in dick and dick['x'] != 0:  # six
            deduction = dick['x']
            nums[6] = deduction
            del dick['x']
            dick['s'] -= deduction
            dick['i'] -= deduction

        if 'g' in dick and dick['g'] != 0:  # eight
            deduction = dick['g']
            nums[8] = deduction
            del dick['g']
            dick['e'] -= deduction
            dick['i'] -= deduction
            dick['h'] -= deduction
            dick['t'] -= deduction

        if 'u' in dick and dick['u'] != 0:  # four
            deduction = dick['u']
            nums[4] = deduction
            del dick['u']
            dick['f'] -= deduction
            dick['o'] -= deduction
            dick['r'] -= deduction

        if 'w' in dick and dick['w'] != 0:  # two
            deduction = dick['w']
            nums[2] = deduction
            del dick['w']
            dick['t'] -= deduction
            dick['o'] -= deduction

        if 'f' in dick and dick['f'] != 0:  # five
            deduction = dick['f']
            nums[5] = deduction
            del dick['f']
            dick['v'] -= deduction
            dick['i'] -= deduction
            dick['e'] -= deduction

        if 's' in dick and dick['s'] != 0:  # seven
            deduction = dick['s']
            nums[7] = deduction
            del dick['s']
            dick['e'] -= 2 * deduction
            dick['v'] -= deduction
            dick['n'] -= deduction

        if 'r' in dick and dick['r'] != 0:  # three
            deduction = dick['r']
            nums[3] = deduction
            del dick['r']
            dick['e'] -= 2 * deduction
            dick['h'] -= deduction
            dick['t'] -= deduction

        if 'o' in dick and dick['o'] != 0:  # one
            deduction = dick['o']
            nums[1] = deduction
            del dick['o']
            dick['e'] -= deduction
            dick['n'] -= deduction

        if 'i' in dick and dick['i'] != 0:  # nine
            deduction = dick['i']
            nums[9] = deduction
            del dick['i']
            dick['e'] -= deduction
            dick['n'] -= 2 * deduction

        ans = []
        for i in xrange(len(nums)):
            if nums[i] != 0:
                for j in xrange(nums[i]):
                    ans.append(str(i))

        return ''.join(ans)


