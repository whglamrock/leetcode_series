
# don't forget to check if newColor already == image[sr][sc]

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0] or image[sr][sc] == newColor:
            return image

        oldColor = image[sr][sc]
        curr = [[sr, sc]]

        while curr:
            next = []
            for i, j in curr:
                image[i][j] = newColor
                if i - 1 >= 0 and image[i - 1][j] == oldColor:
                    next.append([i - 1, j])
                if i + 1 < len(image) and image[i + 1][j] == oldColor:
                    next.append([i + 1, j])
                if j - 1 >= 0 and image[i][j - 1] == oldColor:
                    next.append([i, j - 1])
                if j + 1 < len(image[0]) and image[i][j + 1] == oldColor:
                    next.append([i, j + 1])
            curr = next

        return image