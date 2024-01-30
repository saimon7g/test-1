class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ansStart = 0
        ansEnd = 0
        start = 0
        end = 0
        count = [0] * 256
        position = [0] * 256
        for i in range(len(s)):
            if count[ord(s[i])] == 0:
                count[ord(s[i])] = 1
                position[ord(s[i])] = i
                end += 1
            else:
                length = end - start
                if length > ansEnd - ansStart:
                    ansStart = start
                    ansEnd = end
                if position[ord(s[i])] >= start:
                    start = position[ord(s[i])] + 1
                    end += 1
                    position[ord(s[i])] = i
                else:
                    end += 1
                    position[ord(s[i])] = i
        length = end - start
        if length > ansEnd - ansStart:
            ansStart = start
            ansEnd = end
        print(s[ansStart:ansEnd])
        return ansEnd - ansStart
    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
# Instantiate the Solution class
solution_instance = Solution()

# Get input string from the user
user_input = input("Enter a string: ")

# Call the lengthOfLongestSubstring method with the user's input
solution_instance.lengthOfLongestSubstring(user_input)
