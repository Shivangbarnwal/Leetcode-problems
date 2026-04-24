class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        r=0
        l=0
        u=0
        for i in moves:
            if i=="R":
                r+=1
            elif i=="L":
                l+=1
            else:
                u+=1
        return (abs(r-l)+u)

        