# Uses python3
import sys


# Relatively efficient in terms of time, but bad in terms of memory.
def optimal_sequence_recursive_dp(n, min_num_steps=None):
    if not min_num_steps:
        min_num_steps = {1: 0}
    if n in min_num_steps:
        return min_num_steps[n]
    elif n % 1 != 0 or n < 1:
        return float('inf')
    else:
        min_num_steps[n] = 1 + min(
            optimal_sequence_recursive_dp(n / 3, min_num_steps) if n % 3 == 0 else float('inf'),
            optimal_sequence_recursive_dp(n / 2, min_num_steps) if n % 2 == 0 else float('inf'),
            optimal_sequence_recursive_dp(n - 1, min_num_steps))
        return min_num_steps[n]


def optimal_sequence(n):
    sequence = []
    a = [0 for _ in range(n + 1)]
    for i in range(1, len(a)):
        a[i] = a[i - 1] + 1
        if i % 2 == 0:
            a[i] = min(1 + a[i // 2], a[i])
        if i % 3 == 0:
            a[i] = min(1 + a[i // 3], a[i])
    while n >= 1:
        sequence.append(n)
        if a[n - 1] == a[n] - 1:
            n -= 1
        elif n % 2 == 0 and a[n // 2] == a[n] - 1:
            n //= 2
        elif n % 3 == 0 and a[n // 3] == a[n] - 1:
            n //= 3
    return reversed(sequence)


n = int(sys.stdin.read())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
