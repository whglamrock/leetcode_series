
# the DFA state transition table is the most elegant solution for this. I don't expect myself to really remember
# this algorithm. Once the table is constructed, I should complete coding part easily.

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},

                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},

                 # State (2) - found sign (expect digit/dot). e.g. +.2, -2, etc.
                 {'digit': 3, '.': 4},

                 # State (3) - digit consumer (loop until non-digit). P.S. the value for '.' has to be 5 instead of 4 because
                   # '+.' is different from '5.'. '5.' is a valid ending state
                 {'digit': 3, '.': 5, 'e': 6, 'blank': 9}, # state 3 means so far we only have integer. e.g., +333, 012314

                 # State (4) - found dot (only a digit is valid)
                 {'digit': 5},

                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit': 5, 'e': 6, 'blank': 9},  # P.S. +5., 4. are valid inputs!

                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign': 7, 'digit': 8},

                 # State (7) - sign after 'e' (only digit)
                 {'digit': 8},

                 # State (8) - digit after 'e' (expect digits or end of valid input)
                 {'digit': 8, 'blank': 9},

                 # State (9) - Terminal state (fail if non-blank found afterwards)
                 {'blank': 9}]

        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]

        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input
        # also, we cannot include state 4 as valid because simply something like '+.', '.' are not valid
        if currentState not in [3, 5, 8, 9]:
            return False
        return True