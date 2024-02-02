# Rotate string

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal
        if len(s) != len(goal):
            return False

        # Iterate through possible rotation positions
        for i in range(len(s)):
            # Check if rotating at position i results in the goal string
            rotated_string = s[i:] + s[:i]
            if rotated_string == goal:
                return True

        # If no rotation matches, return False
        return False
    
class Solution_2:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal 