# https://leetcode.com/problems/fibonacci-number/
from functools import wraps

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


class Solution(object):
    @memo
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0

        if N == 1:
            return 1

        return self.fib(N - 1) + self.fib(N - 2)

if __name__ == '__main__':
    f = Solution().fib

    print('Start test...')

    assert f(2) == 1
    assert f(3) == 2
    assert f(4) == 3
    assert f(5) == 5
    assert f(6) == 8
    assert f(7) == 13
    assert f(7) == 13
    assert f(7) == 13

    print('Done.')
