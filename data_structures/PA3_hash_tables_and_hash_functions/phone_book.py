# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


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
    write_responses(process_queries(read_queries()))
