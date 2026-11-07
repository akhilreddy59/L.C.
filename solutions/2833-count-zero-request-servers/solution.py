from collections import defaultdict

class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        # 1. Sort logs chronologically by time
        logs.sort(key=lambda log: log[1])
        
        # 2. Store (query_time, original_index) and sort by query_time
        sorted_queries = sorted(enumerate(queries), key=lambda pair: pair[1])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        # 3. Process queries in increasing order of time
        for orig_idx, q in sorted_queries:
            # EXPAND RIGHT: Add logs where time <= q
            while right < num_logs and logs[right][1] <= q:
                server_id = logs[right][0]
                if server_counts[server_id] == 0:
                    active_servers += 1
                server_counts[server_id] += 1
                right += 1
            
            # CONTRACT LEFT: Remove expired logs where time < q - x
            while left < num_logs and logs[left][1] < q - x:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1
            
            # Record result at original query position
            ans[orig_idx] = n - active_servers
            
        return ans
