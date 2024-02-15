
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:  # Check if the given node is empty
            return node
        
        visited = {}  # Initialize a hashmap to store visited nodes
        
        def clone(node):
            if node in visited:  # If node is already visited, return its clone
                return visited[node]
            
            # Clone the node and add it to visited hashmap
            cloned_node = Node(node.val)
            visited[node] = cloned_node
            
            # Recursively clone neighbors
            cloned_node.neighbors = [clone(neighbor) for neighbor in node.neighbors]
            
            return cloned_node
        
        return clone(node)  # Return the clone of the given node

class Solution(object):
    # bfs
    def cloneGraph1(self, node):
        if not node:
            return node
        m, visited, queue = {}, set(), collections.deque([node])
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                queue.append(neigh)
        return m[node]

    # dfs iteratively
    def cloneGraph2(self, node):
        if not node:
            return node
        m, visited, stack = dict(), set(), deque([node])
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                stack.append(neigh)
        return m[node]

    # dfs recursively
    def cloneGraph(self, node):
        if not node:
            return node
        m, visited = dict(), set()
        self.dfs(node, m, visited)
        return m[node]

    def dfs(self, n, m, visited):
        if n in visited:
            return
        visited.add(n)
        if n not in m:
            m[n] = Node(n.val)
        for neigh in n.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
            m[n].neighbors.append(m[neigh])
            self.dfs(neigh, m, visited)
