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


def poly_hash(string, prime, multiplier):
    hash = 0
    for char in reversed(string):
        hash = (hash * multiplier + ord(char)) % prime
    return hash


def precompute_hashes(text, len_pattern, prime, multiplier):
    length_diff = len(text) - len_pattern
    h = [0 for _ in range(length_diff + 1)]
    string = text[length_diff:len(text)]
    h[length_diff] = poly_hash(string, prime, multiplier)  # Set hash value at rightmost potential match position.
    y = 1
    for i in range(1, len_pattern + 1):
        y = (y * multiplier) % prime
    for i in range(length_diff - 1, -1, -1):
        # Set hash value for each position to the left, without needing to call poly_hash each time.
        h[i] = (multiplier * h[i + 1] + ord(text[i]) - y * ord(text[i + len_pattern])) % prime
    return h


def get_occurrences(pattern, text):
    prime = 1000000007
    multiplier = random.randint(1, prime - 1)
    result = []
    p_hash = poly_hash(pattern, prime, multiplier)
    hashes = precompute_hashes(text, len(pattern), prime, multiplier)
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
