class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people array
        # people[i]= weight of this person
        # infinite number of boats!!
        # each boat can carry weight <= limit and can ONLY carry TWO people at a time
        # sum of weight of these two people has to be <= limit
        # return MIN num of boats to carry all people

        minboats = 0
        people.sort()
        # maintain two pointers that will keep track of people 
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                # a constraint is that a person cannot exceed the weight of the boat
                right -= 1
            minboats += 1
        return minboats
