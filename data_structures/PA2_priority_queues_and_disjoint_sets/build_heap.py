# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def sift_down(self, i):
        minindex = i
        leftchild = 2 * i + 1
        if leftchild < len(self._data) and self._data[leftchild] < self._data[minindex]:
            minindex = leftchild
        rightchild = 2 * i + 2
        if rightchild < len(self._data) and self._data[rightchild] < self._data[minindex]:
            minindex = rightchild
        if i != minindex:
            self._data[i], self._data[minindex] = self._data[minindex], self._data[i]
            self._swaps.append((i, minindex))
            self.sift_down(minindex)

    def generate_swaps(self):
        n = len(self._data)
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
