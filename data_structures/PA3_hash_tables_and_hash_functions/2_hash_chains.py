# python3

"""
2. Hashing with chains

Introduction: In this problem you will implement a hash table using the chaining scheme.

Task: Implement a hash table with lists chaining, using the following polynomial hash function (you are given
    the number of buckets m): h(S) = (SUM[i=0->|S|-1] (S[i]x^i mod p)) mod m, where S[i] is the ASCII code of
    the i-th symbol of S, p = 1000000007, x = 263. Your program should support the following kinds of queries:
    - add [string]: insert [string] into the table. If [string] already exists in the table, ignore the query.
    - del [string]: remove [string] from the table. if there is no such string in the table, ignore the query.
    - find [string]: output "yes" or "no" depending on whether or not the table contains [string].
    - check [i]: output the content of the i-th list in the table. Use spaces to separate the elements of the
      list. If the i-th list is empty, output a blank line.
    When inserting a new string into a hash chain, you must insert it in the beginning of the chain.

Input: The first line contains a single integer m  -- the number of buckets. The next line contains the number
    of queries N. It is followed by N lines, each containing one query in the format described above.

Constraints: 1 <= N <= 10^5; N/5 <= m <= N. All the strings consist of latin letters, are non-empty, and have
     length at most 15.

Output: Print the result of each of the "find" and "check" queries, one result per line, in the same order as
    the queries are given in the input.
"""


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.idx = int(query[1])
        else:
            self.string = query[1]


def poly_hash(string, prime, multiplier):
    hash = 0
    for char in reversed(string):
        hash = (hash * multiplier + ord(char)) % prime
    return hash


def process_query(query, hash_table):
    prime = 1000000007
    multiplier = 263
    bucket_count = len(hash_table)

    if query.type == "check":
        chain = hash_table[query.idx]
        print(' '.join(chain)) if chain else print(' ')
    else:
        hash_key = poly_hash(query.string, prime, multiplier) % bucket_count
        if query.type == 'find':
            print('yes') if query.string in hash_table[hash_key] else print('no')
        elif query.type == 'add':
            if query.string not in hash_table[hash_key]:
                hash_table[hash_key].insert(0, query.string)
        elif query.type == 'del':
            if query.string in hash_table[hash_key]:
                hash_table[hash_key].remove(query.string)


if __name__ == '__main__':
    bucket_count = int(input())
    hash_table = [[] for _ in range(bucket_count)]
    n = int(input())
    for i in range(n):
        process_query(Query(input().split()), hash_table)
