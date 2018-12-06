from utils import memoize

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins.reverse()

def possibilities(n, coins):
    p = 0
    for i, s in enumerate(coins):
        if s < n:
            p += possibilities(n-s, coins[i:])
        if s == n:
            p += 1
    return p

print possibilities(200, coins)