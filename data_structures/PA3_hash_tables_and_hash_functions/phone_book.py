# python3

# 1. Phone book
# Task: Implement a simple phone book manager. It should be able to process the following types of user queries:
#     - add [number] [name]: Add a person with name [name] and phone number [number] to the phone book. If there
#       exists a user with the number already, then overwrite the corresponding name.
#     - del [number]: Erase anyone with number [number] from the phone book. If there is no such person, ignore.
#     - find [number]: Look for a person with phone number [number] and reply with the appropriate name, or with
#       string "not found" if there is no such person.
# Input: The first line contains a single integer n -- the number of queries. It is followed by n lines, each of
#     which contains one query in the format described above.
# Constraints: 1 <= n <= 10^5. All phone numbers consist of decimal digits. They have no leading zeros, and have
#     no more than 7 digits. All names are non-empty strings of latin letters, and have length at most 15. It is
#     guaranteed that there is no person with name "not found".
# Output: Print the result of each "find" query -- the name corresponding to the phone number, or "not found" if
#     there is no person with the number, with one result per line in the same order as the find queries appear.
# Time limit: 6 seconds
# Memory limit: 512 Mb


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def process_queries(queries):
    contacts = [None for _ in range(10**7)]
    result = []
    for q in queries:
        if q.type == 'add':
            contacts[q.number] = q.name
        elif q.type == 'del':
            contacts[q.number] = None
        elif q.type == 'find':
            name = contacts[q.number]
            result.append(name if name else 'not found')
    return result


if __name__ == '__main__':
    n = int(input())
    queries = [Query(input().split()) for i in range(n)]
    result = process_queries(queries)
    print('\n'.join(result))
