# python3

"""
3. Advanced Problem: Network packet processing simulation

Introduction: The goal in this problem is to implement a program to simulate the processing of network packets.

Task: You are given a series of incoming network packets, and your task is to simulate their processing. Packets
    arrive in some order. For each packet i, you know the time it arrived, A_i, and the time the processor takes
    to process it, P_i (both in milliseconds). There is only one processor and it processes the incoming packets
    in the order of their arrival. If the processor has started to process some packet, it doesn't interrupt or
    stop until it has finished processing that packet.

    The computer processing the packets has a network buffer of fixed size S. When packets arrive, they are stored
    in the buffer before being processed. However, if the buffer is full when a packet arrives, it is dropped and
    won't be processed at all. If several packets arrive at the same time, they are first all stored in the buffer
    in the order they enter in the input (though some of them may be dropped if the buffer fills up). The computer
    starts processing the next available packet from the buffer as soon as it finishes processing the previous one.
    If at some point the computer is not busy, and there are no packets in the buffer, the computer just waits for
    the next packet to arrive. A packet leaves the buffer and frees up space in the buffer as soon as the computer
    finishes processing it.

Input: The first line contains the size S of the buffer and the number of incoming network packets n. Each of the
    next n lines contains two numbers: the i-th line contains the time of arrive A_i and the processing time P_i
    of of the i-th packet. It it guaranteed that the sequence of arrival times is non-decreasing (however, it can
    contain duplicate arrival times -- in this case the packet that appears earlier in the input is considered to
    have arrived earlier).

Constraints: 1 <= S <= 10^5; 0 <= n <= 10^5; 0 <= A_i <= 10^6; 0 <= P_i <= 10^3; A_i <= A_i+1 for 1 <= i <= n - 1.
    All the numbers in the input are integers.

Output: For each packet output either the time when it started being processed or -1 if the packet was dropped.
    Output the answers for the packets in the same order as the packets are given in the input.
"""

from collections import deque


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, was_dropped, start_time):
        self.was_dropped = was_dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        while self.finish_time and self.finish_time[0] <= request.arrival_time:
            self.finish_time.popleft()
        if len(self.finish_time) < self.size:
            if self.finish_time and request.arrival_time <= self.finish_time[-1]:
                start_time = self.finish_time[-1]
            else:
                start_time = request.arrival_time
            finished_at = start_time + request.process_time
            self.finish_time.append(finished_at)
            return Response(False, start_time)
        return Response(True, -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    buffer = Buffer(size)
    for request in requests:
        response = buffer.process(request)
        print(response.start_time if not response.was_dropped else -1)
