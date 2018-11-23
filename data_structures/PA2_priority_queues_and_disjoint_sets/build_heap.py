# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = 5#int(input())
        self._data = [1, 2, 3, 4, 5]#[int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def sift_down(self, i):
        minindex = i
        leftchild = 2 * i + 1
        if self._data[leftchild] < self._data[minindex]:
            minindex = leftchild
        rightchild = 2 * i + 2
        if rightchild < len(self._data) and self._data[rightchild] < self._data[minindex]:
            minindex = rightchild
        if i != minindex:
            self._data[i], self._data[minindex] = self._data[minindex], self._data[i]
            self._swaps.append((i, minindex))
            if minindex * 2 + 2 <= len(self._data):
                self.sift_down(minindex)

    def GenerateSwaps(self):
        n = len(self._data)
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
