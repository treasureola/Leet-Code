class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()      # Track characters in current window
        l = 0                # Left pointer of sliding window
        res = 0              # Store maximum length found

        # Expand window by moving right pointer
        for r in range(len(s)):
            # Shrink window from left until no duplicate of s[r] exists
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove leftmost character
                l += 1                 # Move left pointer right
            
            # Add current character to window (now guaranteed unique)
            charSet.add(s[r])
            
            # Update max length: current window size = r - l + 1
            res = max(res, r - l + 1)
        
        return res