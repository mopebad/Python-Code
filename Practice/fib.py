"""
Fibonacci Numbers.

0, 1, 1, 2, 3, 5, 8, 13, ...
"""

"""
Example Input:
fib(7)

Output:
0
1
1
2
3
5
8

Example Input:
fib(3)

Output:
0
1
1
"""


def fib(n: int) -> None:
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(n):
        x = a + b
        print(x)
        a, b = b, x


fib(4)
