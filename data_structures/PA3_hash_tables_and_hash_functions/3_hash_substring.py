# python3

"""
3. Find pattern in text

Task: Implement the Rabin-Karp algorithm for searching a given pattern in a given piece of text.

Input: The input contains two stings: the pattern P and the text T.

Constraints: 1 <= |P| <= |T| <= 5*10^5. The total length of all occurrences of P in T doesn't exceed 10^8. The
    pattern and the text contain only latin letters.

Output: Print all the positions of the occurrences of P in T in ascending order using 0-based indexing.
"""

import random


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


def get_occurrences(pattern, text):
    prime = 1000000007
    x = random.randint(1, prime - 1)
    result = []
    p_hash = poly_hash(pattern, prime, x)
    hashes = precompute_hashes(text, len(pattern), prime, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != hashes[i]:
            continue
        if text[i: i + len(pattern)] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    pattern, text = input().rstrip(), input().rstrip()
    output = get_occurrences(pattern, text)
    print(' '.join(map(str, output)))
