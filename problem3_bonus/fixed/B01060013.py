class Solution(object):
    def minimumDistance(self, nums):
        # Map each number to a list of its indices
        index_map = {}
        min_dist = float('inf')
        found = False

        for current_index, val in enumerate(nums):
            if val not in index_map:
                index_map[val] = []
            
            # Add current index to the list for this value
            index_map[val].append(current_index)
            
            # If we have at least 3 indices, we can form a tuple
            # We only care about the most recent 3 to minimize distance
            if len(index_map[val]) >= 3:
                found = True
                # The indices are naturally sorted as we append them
                # Let i = index_map[val][-3] and k = current_index
                # Distance = 2 * (k - i)
                first_idx = index_map[val][-3]
                dist = 2 * (current_index - first_idx)
                
                if dist < min_dist:
                    min_dist = dist
        
        return min_dist if found else -1