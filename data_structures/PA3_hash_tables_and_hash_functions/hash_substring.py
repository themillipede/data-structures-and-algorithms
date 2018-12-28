# python3

import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(string, prime, x):
    hash = 0
    for i in range(len(string) - 1, -1, -1):
        hash = (hash * x + ord(string[i])) % prime
    return hash


def precompute_hashes(text, len_pattern, prime, x):
    h = [0 for _ in range(len(text) - len_pattern + 1)]
    string = text[len(text) - len_pattern:len(text)]
    h[len(text) - len_pattern] = poly_hash(string, prime, x)
    y = 1
    for i in range(1, len_pattern + 1):
        y = (y * x) % prime
    for i in range(len(text) - len_pattern - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + len_pattern])) % prime
    return h


def are_equal(s1, s2):
    if len(s1) != len(s2):
        return False
    for i, _ in enumerate(s1):
        if s1[i] != s2[i]:
            return False
    return True


def get_occurrences(pattern, text):
    prime = 1000000007
    x = random.randint(1, prime - 1)
    result = []
    p_hash = poly_hash(pattern, prime, x)
    hashes = precompute_hashes(text, len(pattern), prime, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != hashes[i]:
            continue
        if are_equal(text[i : i + len(pattern)], pattern):
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
