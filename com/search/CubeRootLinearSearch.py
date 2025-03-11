"""
Cube root helper implementation using Linear search
The runtime is O(n), but it is a simple implementation that acts as a good reference before implementing binary search
"""

"""
Helper function that calculates cube root when checks for the range within left and right values
"""
def integercuberoothelper(n, left, right):
    cube = lambda x: x * x * x  # anonymous function to cube a number
    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'

    while left < right:
        if(cube(left) <= n and cube(left+1) > n):
            return left
        left = left + 1

    return None

def integercuberoot(n):
    assert(n > 0)
    if n == 1:
        return 1
    if n == 2:
        return 1
    return integercuberoothelper(n, 0, n-1)

assert(integercuberoot(1) == 1)
assert(integercuberoot(2) == 1)
assert(integercuberoot(4) == 1)
assert(integercuberoot(7) == 1)
assert(integercuberoot(8) == 2)
assert(integercuberoot(20) == 2)
assert(integercuberoot(26) == 2)
for j in range(27, 64):
    assert(integercuberoot(j) == 3)
for j in range(64,125):
    assert(integercuberoot(j) == 4)
for j in range(125, 216):
    assert(integercuberoot(j) == 5)
for j in range(216, 343):
    assert(integercuberoot(j) == 6)
for j in range(343, 512):
    assert(integercuberoot(j) == 7)
