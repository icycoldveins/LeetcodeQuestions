class Solution:
    def minAnagramLength(self, s: str) -> int:
        stringList = list(s)
        n = len(s)
        for size in range(1, n):
            if n % size == 0:
                initialList = sorted(stringList[:size])
                for j in range(size, n, size):
                    temp = stringList[j: j + size]
                    temp.sort()
                    if initialList != temp:
                        break
                else:
                    return size 

        return n


""" 
class Solution:
    def minAnagramLength(self, s: str) -> int:
        # concat anagrams of some string t, we want the min so start from lowest length
        # need the concats to add up to s so len(s) // len(t) 

        for i in range(1, len(s)):
            if len(s) % i != 0:
                continue

            counter = Counter(s[:i])
            
            valid = True
            for j in range(len(s) // i):
                counter2 = Counter(s[j * i: (j + 1) * i])
                for k, v in counter.items():
                    if counter2.get(k, 0) != v:
                        valid = False
                        break

                if not valid:
                    break
            
            if valid:
                return i

        return len(s) """
