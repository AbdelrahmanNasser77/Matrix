# Matrix
A Python class that implements basic matrix operations.

# Description
This class allows you to create and manipulate matrices of any size and perform arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation. It also provides a nice string representation of the matrices.

# Installation
To use this class, you need to have Python 3 installed on your system. You don’t need any additional packages or libraries.

# Usage
To use this class, you need to import it in your Python script. For example:

_from matrix import Matrix_

# create a 2x2 matrix with default values of 0
_m1 = Matrix.create_matrix(2, 2, 0)_

# create a 2x2 matrix by entering the values manually
_m2 = Matrix.create_matrix(2, 2)_

# print the matrices
_print(m1)_
_print(m2)_

# perform some operations
_m3 = m1 + m2 # add the matrices_
_m4 = m1 - m2 # subtract the matrices_
_m5 = m1 * m2 # multiply the matrices element-wise_
_m6 = m1 / m2 # divide the matrices element-wise_
_m7 = m1 ** m2 # raise the matrices element-wise to the power of the other matrix_

# print the results
_print(m3)_
_print(m4)_
_print(m5)_
_print(m6)_
_print(m7)_

# License
This code is free to use and modify for personal and educational purposes. For commercial use, please contact the author.
