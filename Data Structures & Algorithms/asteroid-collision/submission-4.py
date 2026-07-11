class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            if i >0:
                s.append(i)
            elif i<0:
                still_standing = True
                while s and s[-1]>0:

                    a = s.pop()
                    if abs(a) > abs(i):
                        still_standing = False
                        s.append(a)
                        break
                    elif abs(a) == abs(i):
                        still_standing = False
                        break
                if still_standing: s.append(i)
                # condition here to add negative back if it has beat all positives
        return s

        