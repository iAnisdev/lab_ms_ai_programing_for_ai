def multiplyMatrix(a , b):
    # verify if the matrix can be multiplied , for that the number of columns of the first matrix must be equal to the number of rows of the second matrix
    if len(a[0]) != len(b):
        return "The matrices can't be multiplied"

    columns = len(b[0])
    rows = len(a)
    # create a matrix with the same number of rows as the first matrix and the same number of columns as the second matrix filled with zeros
    result = [[0 for _ in range(columns)] for _ in range(rows)]

    # iterate over the rows of the first matrix
    for i in range(rows):
        # iterate over the columns of the second matrix
        for j in range(columns):
            # iterate over the columns of the first matrix
            for k in range(len(a[0])):
                # multiply the element of the first matrix by the element of the second matrix and add it to the result
                result[i][j] += a[i][k] * b[k][j]
                
    return result




print(multiplyMatrix([[1, 2], [3, 4]], [[5, 6], [7, 8]])) #

print(multiplyMatrix([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])) # Expected output: "The matrices can't be multiplied"

print(multiplyMatrix([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))

# 4 columns in the first matrix and 4 rows in the second matrix
print(multiplyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]))
    