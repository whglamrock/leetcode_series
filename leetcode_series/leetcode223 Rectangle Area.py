
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        if B>=H or D<=F or A>=G or C<=E:
            return (C-A)*(D-B)+(G-E)*(H-F)

        elif (A>E and G>C and B>F and H>D) or (A<E and G<C and B<F and H<D):
            return max((C-A)*(D-B),(G-E)*(H-F))

        else:
            a = sorted([A,C,E,G])
            b = sorted([B,D,F,H])
            return (C-A)*(D-B)+(G-E)*(H-F)-(a[2]-a[1])*(b[2]-b[1])

