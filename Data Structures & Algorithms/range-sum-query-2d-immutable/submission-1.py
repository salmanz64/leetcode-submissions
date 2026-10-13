class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixMatrix = []

        for row in range(len(matrix)):
            newrow = [0] * len(matrix[0])
            self.prefixMatrix.append(newrow)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):

                if r == 0 and c == 0:
                    self.prefixMatrix[r][c] = matrix[r][c]

                elif r == 0:
                    self.prefixMatrix[r][c] = (
                        matrix[r][c] + self.prefixMatrix[r][c - 1]
                    )

                elif c == 0:
                    self.prefixMatrix[r][c] = (
                        matrix[r][c] + self.prefixMatrix[r - 1][c]
                    )

                else:
                    self.prefixMatrix[r][c] = (
                        matrix[r][c]
                        + self.prefixMatrix[r - 1][c]
                        + self.prefixMatrix[r][c - 1]
                        - self.prefixMatrix[r - 1][c - 1]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = self.prefixMatrix[row2][col2]

        if row1 > 0:
            totalSum -= self.prefixMatrix[row1 - 1][col2]

        if col1 > 0:
            totalSum -= self.prefixMatrix[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            totalSum += self.prefixMatrix[row1 - 1][col1 - 1]

        return totalSum