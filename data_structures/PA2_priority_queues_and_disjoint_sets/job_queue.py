# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def _sift_down(self, i):
        minindex = i
        leftchild = 2 * i + 1
        if self.pq[leftchild][1] <= self.pq[minindex][1] and self.pq[leftchild][0] < self.pq[minindex][0]:
            minindex = leftchild
        rightchild = 2 * i + 2
        if (rightchild < len(self.pq) and
            self.pq[rightchild][1] <= self.pq[minindex][1] and self.pq[rightchild][0] < self.pq[minindex][0]):
            minindex = rightchild
        if i != minindex:
            self.pq[i], self.pq[minindex] = self.pq[minindex], self.pq[i]
            if minindex * 2 + 2 <= len(self.pq):
                self._sift_down(minindex)

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.pq = [[i, 0] for i in range(self.num_workers)]
        n = len(self.pq)
        for i in range(len(self.jobs)):
            next_worker = self.pq.pop(0)
            self.assigned_workers[i] = next_worker[0]
            self.start_times[i] = next_worker[1]
            next_worker[1] += self.jobs[i]
            self.pq.append(next_worker)
            for i in range(n // 2 - 1, -1, -1):
                self._sift_down(i)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

#if __name__ == '__main__':
job_queue = JobQueue()
job_queue.solve()

