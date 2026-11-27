class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # source is where we start (the stop), and routes is a cyclical bus route per route[i]
        # target is the stop that we wanna go to

        # in this test case we start at one, take one bus route to 2 and check if anything, no
        # so check next stop on route to 7 check if anything to transfer, yes so we continue
        # riding this new route but and cycle to 3 (stop), then to target stop of 6, only 2
        # routes were ever taken.


        # we want to go to every node in a route tracking what we have seen and for every node
        # we check if its in any other route, if yes we make sure its not in a route that
        # we are currently/have already visited, and go to that route, and continue the search
        # there
        # the base case is if we have found the target stop, we return counter after each bfs
        if source == target:
            return 0
        
        n, stops = len(routes), defaultdict(list)
        for routeNumber in range(n):
            for stopNumber in routes[routeNumber]:
                stops[stopNumber].append(routeNumber)

        
        q = deque([source])
        visitedRoutes, visitedStops = set(), set([source]) 
        res = 0
        while q:
            for _ in range(len(q)):
                stopNumber = q.popleft()
                if stopNumber == target:
                    return res
                
                for routeNumber in stops[stopNumber]:
                    if routeNumber in visitedRoutes:
                        continue
                    visitedRoutes.add(routeNumber)
                    for stopNumber in routes[routeNumber]:
                        if stopNumber in visitedStops:
                            continue
                        visitedStops.add(stopNumber)
                        q.append(stopNumber)

            res += 1

        return -1