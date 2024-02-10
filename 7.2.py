A = [[1,2],
     [3,4]]
def Determinant(matrix, n):
  if n == 2:
      determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
      return determinant
  
  determinant = 0

  def get_submatrix(matrix, row, col):
      submatrix = [row[:col] + row[col+1:] for row in matrix[:row] + matrix[row+1:]]
      return submatrix
  
  for j in range(n):
      cofactor = (-1) ** (0 + j)
      submatrix = get_submatrix(matrix, 0, j)
      determinant += cofactor * matrix[0][j] * Determinant(submatrix, n-1)
  
  return determinant

print(Determinant(A,2))