- 双指针不一定是o(n2) ,也可能是nlgn
- 困难题不要按照规则模拟,肯定超时
- 一定要注意移位运算符的优先级是最低的
```python 
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dp = [[float("inf") for j in range(N+1)] for i in range(N+1)]

        for i in range(1,N+1):
            dp[i][i] = 0

        for u,v,w in times:
            dp[u][v] = w

        for k in range(1,N+1):
            for i in range(1,N+1):
                for j in range(1,N+1):
                    dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j])

        ans = max(dp[K][1:])
        return ans if ans != float("inf") else -1
```
``` python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        cost = dict()
        visited = set()
        dp = [float("inf")]*(N+1)
        for u,v,w in times:
            if u not in cost:
                cost[u] = list()
            cost[u].append((v,w))

        cur = [(0,K)]

        while cur:
            mid_distance,u = heapq.heappop(cur)

            dp[u] = min(dp[u],mid_distance)
            visited.add(u)
            if u in cost:
                for v,w in cost[u]:
                    if v not in visited:
                        heapq.heappush(cur,(mid_distance+w,v))
        #     print(cur)
        # print(dp)
            
        return max(dp[1:]) if max(dp[1:]) != float("inf") else -1
```
```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        parents = [i for i in range(length)]
        def find(u):
            while parents[u] != u:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u

        def distance(x):
            return abs(points[x[0]][0]-points[x[1]][0])+abs(points[x[0]][1]-points[x[1]][1])
        pools = []
        for i in range(length):
            for j in range(i+1,length):
                pools.append([i,j])

        pools.sort(key = distance)
        count = 0
        for x in pools:
            a,b = x
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parents[pa] = pb
                count += distance(x)

        return count
```

- 图的问题一定要想到visited数组
- 树的定义： 全部连通（并查集） +    边树+1== 节点数
- 树和图可以互相转换
- 数据量小于16考虑数位dp
- 