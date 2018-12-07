# Uses python3
import sys


def get_change_recursive_dp(m, min_num_coins=None):
    if not min_num_coins:
        min_num_coins = {0: 0}
    if m in min_num_coins:
        return min_num_coins[m]
    if m < 1:
        return float('inf')
    elif m in (4, 3, 1):
        return 1
    else:
        min_num_coins[m] = 1 + min(
            get_change_recursive_dp(m - 4, min_num_coins),
            get_change_recursive_dp(m - 3, min_num_coins),
            get_change_recursive_dp(m - 1, min_num_coins))
        return min_num_coins[m]


def get_change(money, min_num_coins=None):
    if not min_num_coins:
        min_num_coins = {0: 0}
    for m in range(1, money + 1):
        min_num_coins[m] = float('inf')
        for i in (1, 3, 4):
            if m >= i:
                num_coins = min_num_coins[m - i] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
