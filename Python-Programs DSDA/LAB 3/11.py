# Write a program to print the spiral coil matrix with input as N.

def spiralMatrixPattern(N):
    matrix = [[0] * N for _ in range(N)]
    num = 1
    left, right, top, bottom = 0, N-1, 0, N-1

    while left <= right and top <= bottom:
        # left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    for row in matrix:
        print(' '.join(map(str, row)))

n = int(input('Enter N: '))
spiralMatrixPattern(n)
