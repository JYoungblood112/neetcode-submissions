class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {}
        distances = {}
        heap = []

        for i in range(n + 1):
            graph[i] = []

        for start, end, time in times:
            graph[start].append((end, time))


        for i in range(1, n + 1):
            distances[i] = float("inf")

        distances[k] = 0


        heapq.heappush(heap, (0, k))


        while heap:

            cur, node = heapq.heappop(heap)

            for neighbor, weight in graph[node]:

                new = cur + weight

                if new < distances[neighbor]:

                    distances[neighbor] = new

                    heapq.heappush(heap, (new, neighbor))


        m = max(distances.values())

        if m == float("inf"):
            return -1

        return m