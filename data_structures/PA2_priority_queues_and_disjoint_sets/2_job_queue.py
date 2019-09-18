# python3

# 2. Parallel processing
# Task: A parallelised program uses n independent threads to process a given list of m jobs. Threads take jobs in
#    the order they are given in the input. If there is a free thread, it immediately takes the next job from the
#    list. If a thread has started processing a job, it doesn't interrupt or stop until it finishes. If several
#    threads try to take jobs from the list simultaneously, the thread with the smaller index takes the job. For
#    each job it is known exactly how long it will take any thread to process the job, and this time is the same
#    for all the threads. Determine for each job which thread will process it and when it will start processing.
# Input: The first line contains integers n and m. The second line contains m integers t_i -- the time in seconds
#    it takes any thread to process the i-th job. The times are given in the same order as they are in the list
#    from which threads take jobs. Threads are indexed starting from 0.
# Constraints: 1 <= n <= 10^5; 1 <= m <= 10^5; 0 <= t_i <= 10^9.
# Output: Exactly m lines, where the i-th line contains two space-separated integers -- the 0-based index of the
#    thread which will process the i-th job and the time in seconds when it will start processing that job.
# Time limit: 6 seconds
# Memory limit: 512 Mb


def sift_down(i, pq):
    minindex = i
    leftchild = 2 * i + 1
    if leftchild < len(pq):
        if (pq[leftchild][1] < pq[minindex][1]
                or (pq[leftchild][1] == pq[minindex][1]
                    and pq[leftchild][0] < pq[minindex][0])):
            minindex = leftchild
    rightchild = 2 * i + 2
    if rightchild < len(pq):
        if (pq[rightchild][1] < pq[minindex][1]
                or (pq[rightchild][1] == pq[minindex][1]
                    and pq[rightchild][0] < pq[minindex][0])):
            minindex = rightchild
    if i != minindex:
        pq[i], pq[minindex] = pq[minindex], pq[i]
        sift_down(minindex, pq)


def assign_jobs(jobs, num_workers):
    assigned_workers = [None] * len(jobs)
    start_times = [None] * len(jobs)
    pq = [[i, 0] for i in range(num_workers)]
    for i in range(len(jobs)):
        assigned_workers[i] = pq[0][0]
        start_times[i] = pq[0][1]
        pq[0][1] += jobs[i]
        sift_down(0, pq)
    return assigned_workers, start_times


if __name__ == '__main__':
    num_workers, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    assigned_workers, start_times = assign_jobs(jobs, num_workers)
    for i in range(len(jobs)):
        print(assigned_workers[i], start_times[i])
