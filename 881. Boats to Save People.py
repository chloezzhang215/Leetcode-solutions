class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people or len(people) == 0:
            return 0
            
        people = sorted(people)
        a = 0
        b = len(people) - 1
        count = 0
        while a < b:
            if people[a] + people[b] <= limit:
                count += 1
                a += 1
                b -= 1
            else:
                b -= 1
            
        count += len(people) - count*2
                    
        return count
