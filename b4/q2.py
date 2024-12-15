# https://leetcode.com/problems/bus-routes/
# Time: O(m* n^2) m: number of routes, n: number of stops
# Space: O(m * n)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        
        for route, stops in enumerate(routes):
            for s in stops:
                graph[s].append(route)

        q = deque()
        visitedStop = set()
        visitedRoutes = set()
        q.append(source)
        visitedStop.add(source)
        res = 0

        while len(q) > 0:
            size = len(q)
            res += 1
            for _ in range(size):
                currentStop = q.popleft()
                
                for route in graph[currentStop]:
                    if route not in visitedRoutes:
                        visitedRoutes.add(route)
                        for stop in routes[route]:
                            if stop == target:
                                return res
                            if stop not in visitedStop:
                                visitedStop.add(stop)
                                q.append(stop)

        return -1
        


