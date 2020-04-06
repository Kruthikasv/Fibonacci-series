import numpy as np
import sys
if len(sys.argv) < 2:
    print("No arguments provided")
    exit()
try:
    number= int(sys.argv[1])
except ValueError:
    print("Invalid Input")
    exit()
if number < 0:
    print("Invalid Input")
    exit()

def power(m,MAT):
    if m == 0:
        return np.ones((2, 2))
    if m == 1:
        return MAT
    if m == 2:
        return MAT.dot(MAT)
    if m > 2:
        half = power(m // 2, MAT)
        if m % 2 == 0:
            return half.dot(half)
        else:
            return MAT.dot(half.dot(half))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        base_mat = np.ones((1, 2))
        base_mat[0][0] = 0
        F = np.ones((2, 2))
        F[0][0] = 0
        R = power(n - 1, F)
        result = base_mat.dot(R)
        return result[0][1]
    return -1

print(fibonacci(number))