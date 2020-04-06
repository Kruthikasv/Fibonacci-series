REPORT
TEAM
ASHWINI J                                                 1KS18CS007
BHUVANA CHANDRIKA GANTI              1KS18CS013
KRUTHIKA S VASISHT                              1KS18CS035

TEAM CONTRIBUTIONS
* ASHWINI: Has helped with the Logic and coding
* BHUVANA: Has tried different ways to implement program efficiently and checked for errors
* KRUTHIKA: Has helped in decoding the logic part and debug the errors

QUESTION :
TO COMPUTE THE Nth FIBONACCI NUMBER BY DIVIDE AND CONQUER APPROACH BY MAKING USE OF MATRIX EXPONENTIATION.

EXPLANATION:
Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F0=0, F1=1
And Fn=Fn-1+Fn-2         for n>1

Here we consider nth value as 4,
we should get 3 as the output.
We have defined two user defined functions
->power(m,MAT)
->fibonacci(n)
The function power() calculates the result of multiplying the matrix MAT,  m times by making use of divide and conquer approach.
Initially if m>2, then m=m/2 and the power()function is called recursively which is stored in variable half.
If m is even, Then we return half*half.
If m is odd we return MAT*half*half.
This value is returned to the fibonacci()function. Here we have two matrices base_mat and F which can be initialised using numpy library.
NumPy is a Python package which stands for 'Numerical Python'. It is the core library for scientific computing, which contains a powerful n-dimensional array object, provide tools for integrating C, C++ etc, and The sys module provides functions and variables used to manipulate different parts of the Python runtime environment
The value returned by power() function is stored in variable R.Since according to the formula we need to multiply the base matrix with the (matrix R)^m.
This is stored in result. Our desired output is stored in the second component of the matrix result which can be returned ie.,result[0][1] which will be returned when the fibonacci() function is called.

SAMPLE INPUTS
1,2,3,4,5,6,7,8,9,10,(n>=0)

CHALLENGES FACED
The project that was assigned to us was quite challenging, we found it hard to solve it using divide and conquer. These problems were overcome by browsing about these various concepts of and learning about learning about them from various different sources online.
The important links we used are:
https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
https://www.youtube.com/watch?v=EEb6JP3NXBI

TIME COMPLEXITY
The time complexity of the solution is O(logn)

LEARNT FROM ASSIGNMENT
In conclusion, we learnt how to implement arrays in python using numpy library and the divide and conquer algorithm.
