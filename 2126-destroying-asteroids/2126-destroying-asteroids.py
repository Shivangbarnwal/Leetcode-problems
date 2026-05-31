class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        pref=[mass]
        for i in asteroids:
            p=pref[-1]
            if p>=i:
                pref.append(p+i)
            else:
                return False
        return True