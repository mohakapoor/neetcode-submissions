class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = { i: [] for i in range(numCourses)}

        for course,preq in prerequisites:
            map[course].append(preq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False

            if map[course] == []:
                return True

            visited.add(course)
            for i in map[course]:
                if not dfs(i): return False

            visited.remove(course)
            map[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True

        