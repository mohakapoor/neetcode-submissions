class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position,speed))
        cars.sort(key=lambda x:x[0])
        for i in range(len(cars)):
            t = (target-cars[i][0])/cars[i][1]
            # print(stack)
            # print(i,t)
            while stack and t>=stack[-1]:
                stack.pop()
            stack.append(t)
        # print(stack)
        return len(stack)
        