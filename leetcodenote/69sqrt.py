"""
Using binary search to locate the int sqrt value.

Key: how to define the mid and sqrt

https://leetcode.com/problems/sqrtx/

"""


# ! sqrt = mid*mid
# ! solution is trying to check whether sqrt/mid is equal to mid
def mySqrt1(x):
    if x == 0:
        return 0

    left = 1
    right = x
    mid = sqrt = 0
    while left <= x:
        mid = int(left+(right-left)/2)
        sqrt = int(x/mid)
        if sqrt == mid:
            return mid
        elif mid > sqrt:
            right = mid-1
        else:
            left = mid+1
    return right


# ! solution2 makes more sence when first seeing this
# ! as noticed, the main difference between solution1 and solution2 is condition checking.
def mySqrt2( x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid - 1
        else:
            l = mid + 1

# ! solution3 newton method
def mySqrt3(self, x):
    if x < 2:
        return x
    
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2        
        
    return int(x1)

# a = 30
# mySqrt(30)
