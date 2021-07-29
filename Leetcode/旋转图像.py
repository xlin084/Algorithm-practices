# mat = [[1,2,3], [4,5,6], [7,8,9]]
# mat.reverse()
# # print(mat)
# for i in range(len(mat)):
#     for j in range(i):
#         mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
# print(mat)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


test = Solution()
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(test.rotate(matrix))