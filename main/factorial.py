import pytest


def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


assert factorial(5) == 120
assert factorial(2) == 2

