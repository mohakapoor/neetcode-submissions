class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        freq = [0]*26
        freq2 = [0]*26
        for i in s1:
            freq[ord(i)-ord('a')] += 1
        for i in s2[:len(s1)]:
            freq2[ord(i)-ord('a')] +=1

        for i in range(len(s1),len(s2)):
            print(i,"og",freq)
            print(i,"check",freq2)
            if freq == freq2:
                return True
            freq2[ord(s2[i-len(s1)])-ord('a')] -= 1
            freq2[ord(s2[i])-ord('a')] += 1
        return freq == freq2
