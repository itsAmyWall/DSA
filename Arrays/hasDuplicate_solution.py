
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Function to check if there are any duplicates in the list of numbers.
        
        Args:
        nums (List[int]): List of integers to check.
        
        Returns:
        bool: True if duplicates are found, False otherwise.
        
        Time Complexity:
        - The time complexity is O(n), where n is the length of the input list `nums`. 
        - We traverse the list once and check if each element is in the set, which is an O(1) operation.
        
        Space Complexity:
        - The space complexity is O(n), because in the worst case (when there are no duplicates),
          we need to store all n elements in the hashset.
        
        Why this solution is efficient:
        - Using a hashset allows constant time lookups and insertions (O(1) on average), which makes the algorithm 
          more efficient than a nested loop (which would result in O(n^2) time complexity).
        - The use of a set also ensures that we don't store duplicate values, which helps in optimizing space usage.
        """
        # Edge case: empty list
        if not nums:
            return False

        # Edge case: single element
        if len(nums) == 1:
            return False

        # Use a set to track seen numbers
        hashset = set()

        for n in nums:
            if n in hashset:
                return True  # Duplicate found
            hashset.add(n)

        return False  # No duplicates found
