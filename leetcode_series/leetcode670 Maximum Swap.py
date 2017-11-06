
class Solution(object):
    def maximumSwap(self, num):

        num = str(num)
        n = len(num)
        index_of_max_from_right = [0] * n
        swapped_digits = list(num)

        # scan from right to left, find the index of the biggest digit to num[i]'s right (including num[i])
        for i in xrange(n - 1, -1, -1):
            # second condition is ">=" because you want to swap the smaller digit with the
            #   right most bigger digit
            if i < n - 1 and num[index_of_max_from_right[i + 1]] >= num[i]:
                index_of_max_from_right[i] = index_of_max_from_right[i + 1]
            else:
                index_of_max_from_right[i] = i

        the_index_to_swap = None
        j = 0
        while j < n:
            if num[index_of_max_from_right[j]] > num[j]:
                the_index_to_swap = index_of_max_from_right[j]
                break
            j += 1

        if the_index_to_swap != None:
            swapped_digits[the_index_to_swap] = num[j]
            swapped_digits[j] = num[the_index_to_swap]

        return int(''.join(swapped_digits))