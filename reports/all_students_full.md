# All Students — Full Submission Dump

====================================================================================================



====================================================================================================

_74 students. Ordered by combined score (highest first); students needing manual review are listed at the end._

====================================================================================================



====================================================================================================

# B00906607 — Vikram Minhas

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B00906607

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |        l = r = window_sum = max_sum = negative_count = 0
 3 | 
 4 |        for r in range(k):
 5 |              window_sum += nums[r]
 6 |              if nums[r] < 0:
 7 |                 negative_count += 1
 8 |        if negative_count <=1:
 9 |              max_sum = window_sum
10 | 
11 |        for r in range(k, len(nums)):
12 |              if nums[l] < 0:
13 |                  negative_count -=1
14 |              window_sum -= nums[l]
15 |              l += 1
16 | 
17 |              window_sum += nums[r]
18 |              if nums[r] < 0:
19 |                 negative_count +=1
20 |              if negative_count <= 1:
21 |                 max_sum = max(max_sum, window_sum)
22 |        return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |        l = r = window_sum = max_sum = negative_count = 0
 3 | 
 4 |        for r in range(k):
 5 |              window_sum += nums[r]
 6 |              if nums[r] < 0:
 7 |                 negative_count += 1
 8 |        if negative_count <=1:
 9 |              max_sum = window_sum
10 | 
11 |        for r in range(k, len(nums)):
12 |              if nums[l] < 0:
13 |                  negative_count -=1
14 |              window_sum -= nums[l]
15 |              l += 1
16 | 
17 |              window_sum += nums[r]
18 |              if nums[r] < 0:
19 |                 negative_count +=1
20 |              if negative_count <= 1:
21 |                 max_sum = max(max_sum, window_sum)
22 |        return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B00906607

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,11 +1,11 @@
 def count_pairs(nums, T):
-       l = 0
-       r = len(nums) - 1
-       count = 0
-       while l < r:
-                 if nums[l] + nums[r] <= T:
-                    count += (r - l)
-                    l += 1
-                 else:
-                    r -=1
-        return count
+    l = 0
+    r = len(nums) - 1
+    count = 0
+    while l < r:
+        if nums[l] + nums[r] <= T:
+            count += (r - l)
+            l += 1
+        else:
+            r -=1
+    return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |        l = 0
 3 |        r = len(nums) - 1
 4 |        count = 0
 5 |        while l < r:
 6 |                  if nums[l] + nums[r] <= T:
 7 |                     count += (r - l)
 8 |                     l += 1
 9 |                  else:
10 |                     r -=1
11 |         return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     l = 0
 3 |     r = len(nums) - 1
 4 |     count = 0
 5 |     while l < r:
 6 |         if nums[l] + nums[r] <= T:
 7 |             count += (r - l)
 8 |             l += 1
 9 |         else:
10 |             r -=1
11 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01060013 — Logan Regueiferos

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01060013

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     current_sum = 0
 4 |     neg_count = 0
 5 |     max_sum = float('-inf')
 6 |     found_valid = False
 7 | 
 8 |     # 1. Build the initial window of size k
 9 |     for i in range(k):
10 |         current_sum += nums[i]
11 |         if nums[i] < 0:
12 |             neg_count += 1
13 |     
14 |     # Check if the first window is valid
15 |     if neg_count <= 1:
16 |         max_sum = current_sum
17 |         found_valid = True
18 | 
19 |     # 2. Slide the window across the rest of the array
20 |     for i in range(k, n):
21 |         # Remove the element that is sliding out (at index i - k)
22 |         out_element = nums[i - k]
23 |         current_sum -= out_element
24 |         if out_element < 0:
25 |             neg_count -= 1
26 |         
27 |         # Add the element that is sliding in (at index i)
28 |         in_element = nums[i]
29 |         current_sum += in_element
30 |         if in_element < 0:
31 |             neg_count += 1
32 |         
33 |         # 3. If the current window is valid, update max_sum
34 |         if neg_count <= 1:
35 |             max_sum = max(max_sum, current_sum)
36 |             found_valid = True
37 | 
38 |     return max_sum if found_valid else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     current_sum = 0
 4 |     neg_count = 0
 5 |     max_sum = float('-inf')
 6 |     found_valid = False
 7 | 
 8 |     # 1. Build the initial window of size k
 9 |     for i in range(k):
10 |         current_sum += nums[i]
11 |         if nums[i] < 0:
12 |             neg_count += 1
13 |     
14 |     # Check if the first window is valid
15 |     if neg_count <= 1:
16 |         max_sum = current_sum
17 |         found_valid = True
18 | 
19 |     # 2. Slide the window across the rest of the array
20 |     for i in range(k, n):
21 |         # Remove the element that is sliding out (at index i - k)
22 |         out_element = nums[i - k]
23 |         current_sum -= out_element
24 |         if out_element < 0:
25 |             neg_count -= 1
26 |         
27 |         # Add the element that is sliding in (at index i)
28 |         in_element = nums[i]
29 |         current_sum += in_element
30 |         if in_element < 0:
31 |             neg_count += 1
32 |         
33 |         # 3. If the current window is valid, update max_sum
34 |         if neg_count <= 1:
35 |             max_sum = max(max_sum, current_sum)
36 |             found_valid = True
37 | 
38 |     return max_sum if found_valid else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01060013

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         
 9 |         if current_sum <= T:
10 |             # If nums[left] + nums[right] is valid, 
11 |             # then nums[left] paired with any element 
12 |             # between left and right is also valid.
13 |             count += (right - left)
14 |             # Move left pointer to check next set of pairs
15 |             left += 1
16 |         else:
17 |             # Sum is too large, decrease the right pointer
18 |             # to reduce the total sum
19 |             right -= 1
20 |             
21 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         
 9 |         if current_sum <= T:
10 |             # If nums[left] + nums[right] is valid, 
11 |             # then nums[left] paired with any element 
12 |             # between left and right is also valid.
13 |             count += (right - left)
14 |             # Move left pointer to check next set of pairs
15 |             left += 1
16 |         else:
17 |             # Sum is too large, decrease the right pointer
18 |             # to reduce the total sum
19 |             right -= 1
20 |             
21 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution(object):
 2 |     def minimumDistance(self, nums):
 3 |         # Map each number to a list of its indices
 4 |         index_map = {}
 5 |         min_dist = float('inf')
 6 |         found = False
 7 | 
 8 |         for current_index, val in enumerate(nums):
 9 |             if val not in index_map:
10 |                 index_map[val] = []
11 |             
12 |             # Add current index to the list for this value
13 |             index_map[val].append(current_index)
14 |             
15 |             # If we have at least 3 indices, we can form a tuple
16 |             # We only care about the most recent 3 to minimize distance
17 |             if len(index_map[val]) >= 3:
18 |                 found = True
19 |                 # The indices are naturally sorted as we append them
20 |                 # Let i = index_map[val][-3] and k = current_index
21 |                 # Distance = 2 * (k - i)
22 |                 first_idx = index_map[val][-3]
23 |                 dist = 2 * (current_index - first_idx)
24 |                 
25 |                 if dist < min_dist:
26 |                     min_dist = dist
27 |         
28 |         return min_dist if found else -1 
29 | The time complexity of the solution is O(n) as the code passes through the array only once. The space complexity is O(n) because each element is stored in a hash map. The solution uses a hash map to track the indices of each number, identifying triplets of identical values and calculating the minimum distance as 2 times (k - i) for the most closely spaced first and third occurrences.
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01061183 — Tianna Balkam

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01061183

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     curr_sum = 0
 3 |     neg_count = 0
 4 |     max_sum = 0
 5 | 
 6 |     for i in range(k):
 7 |         curr_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             neg_count += 1
10 |     if neg_count <= 1:
11 |         max_sum = curr_sum
12 | 
13 |     for i in range(k, len(nums)):
14 |         curr_sum += nums[i]
15 |         if nums[i] < 0:
16 |             neg_count += 1
17 |         if nums[i - k] < 0:
18 |             neg_count -= 1
19 |         curr_sum -= nums[i - k]
20 |         if neg_count <= 1:
21 |             if curr_sum > max_sum:
22 |                 max_sum = curr_sum
23 | 
24 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     curr_sum = 0
 3 |     neg_count = 0
 4 |     max_sum = 0
 5 | 
 6 |     for i in range(k):
 7 |         curr_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             neg_count += 1
10 |     if neg_count <= 1:
11 |         max_sum = curr_sum
12 | 
13 |     for i in range(k, len(nums)):
14 |         curr_sum += nums[i]
15 |         if nums[i] < 0:
16 |             neg_count += 1
17 |         if nums[i - k] < 0:
18 |             neg_count -= 1
19 |         curr_sum -= nums[i - k]
20 |         if neg_count <= 1:
21 |             if curr_sum > max_sum:
22 |                 max_sum = curr_sum
23 | 
24 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01061183

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     num_pairs = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             num_pairs += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return num_pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     num_pairs = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             num_pairs += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return num_pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | N/A
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01061839 — Stephania Calin

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01061839

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -2,22 +2,22 @@
 
 def max_valid_window_sum(nums, k):
-	window_sum = sum(nums[:k])
-	neg_count = sum(1 for x in nums[:k] if x < 0)
+    window_sum = sum(nums[:k])
+    neg_count = sum(1 for x in nums[:k] if x < 0)
 
-	max_sum = window_sum if neg_count <= 1 else 0
+    max_sum = window_sum if neg_count <= 1 else 0
 
-	for i in range(k, len(nums)):
-		incoming = nums[i]
-		outgoing = nums[i - k]
+    for i in range(k, len(nums)):
+        incoming = nums[i]
+        outgoing = nums[i - k]
 
-		window_sum += incoming - outgoing
+        window_sum += incoming - outgoing
 
-		if incoming < 0:
-			neg_count += 1
-		if outgoing < 0:
-			neg_count -= 1
+        if incoming < 0:
+            neg_count += 1
+        if outgoing < 0:
+            neg_count -= 1
 
-		if neg_count <= 1:
-			max_sum = max(max_sum, window_sum)
+        if neg_count <= 1:
+            max_sum = max(max_sum, window_sum)
 
-	return max_sum
+    return max_sum
```

</details>

**Raw extracted input:**

```
 1 | #i chose to write in python for all my answers
 2 | 
 3 | def max_valid_window_sum(nums, k):
 4 | 	window_sum = sum(nums[:k])
 5 | 	neg_count = sum(1 for x in nums[:k] if x < 0)
 6 | 
 7 | 	max_sum = window_sum if neg_count <= 1 else 0
 8 | 
 9 | 	for i in range(k, len(nums)):
10 | 		incoming = nums[i]
11 | 		outgoing = nums[i - k]
12 | 
13 | 		window_sum += incoming - outgoing
14 | 
15 | 		if incoming < 0:
16 | 			neg_count += 1
17 | 		if outgoing < 0:
18 | 			neg_count -= 1
19 | 
20 | 		if neg_count <= 1:
21 | 			max_sum = max(max_sum, window_sum)
22 | 
23 | 	return max_sum
```

**Fixed input:**

```
 1 | #i chose to write in python for all my answers
 2 | 
 3 | def max_valid_window_sum(nums, k):
 4 |     window_sum = sum(nums[:k])
 5 |     neg_count = sum(1 for x in nums[:k] if x < 0)
 6 | 
 7 |     max_sum = window_sum if neg_count <= 1 else 0
 8 | 
 9 |     for i in range(k, len(nums)):
10 |         incoming = nums[i]
11 |         outgoing = nums[i - k]
12 | 
13 |         window_sum += incoming - outgoing
14 | 
15 |         if incoming < 0:
16 |             neg_count += 1
17 |         if outgoing < 0:
18 |             neg_count -= 1
19 | 
20 |         if neg_count <= 1:
21 |             max_sum = max(max_sum, window_sum)
22 | 
23 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01061839

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,13 +1,13 @@
 def count_pairs(nums, T):
-	left = 0
-	right = len(nums) - 1
-	count = 0
+    left = 0
+    right = len(nums) - 1
+    count = 0
 
-	while left < right:
-		if nums[left] + nums[right] <= T:
-			count += right - left
-			left += 1
-		else:
-			right -= 1
+    while left < right:
+        if nums[left] + nums[right] <= T:
+            count += right - left
+            left += 1
+        else:
+            right -= 1
 
-	return count
+    return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 	left = 0
 3 | 	right = len(nums) - 1
 4 | 	count = 0
 5 | 
 6 | 	while left < right:
 7 | 		if nums[left] + nums[right] <= T:
 8 | 			count += right - left
 9 | 			left += 1
10 | 		else:
11 | 			right -= 1
12 | 
13 | 	return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01072737 — Ryan Martin

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01072737

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,29 +1,29 @@
 def max_valid_window_sum(nums, k):
-	negs = 0
-	sum = 0
-	result = 0
+    negs = 0
+    sum = 0
+    result = 0
 
-	for i in range(k):
-		if nums[i] < 0:
-			negs += 1
-		sum += nums[i]
+    for i in range(k):
+        if nums[i] < 0:
+            negs += 1
+        sum += nums[i]
 
-	if negs <= 1:
-		result = sum
+    if negs <= 1:
+        result = sum
 
-	for right in range(k, len(nums)):
-		left = right - k
+    for right in range(k, len(nums)):
+        left = right - k
 
-		if nums[right] < 0:
-			negs += 1
-		sum += nums[right]
+        if nums[right] < 0:
+            negs += 1
+        sum += nums[right]
 
-		if nums[left] < 0:
-			negs -= 1
-		sum -= nums[left]
+        if nums[left] < 0:
+            negs -= 1
+        sum -= nums[left]
 
-		if negs <= 1:
-			result = max(result, sum)
+        if negs <= 1:
+            result = max(result, sum)
 
-	return result
+    return result
 
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 	negs = 0
 3 | 	sum = 0
 4 | 	result = 0
 5 | 
 6 | 	for i in range(k):
 7 | 		if nums[i] < 0:
 8 | 			negs += 1
 9 | 		sum += nums[i]
10 | 
11 | 	if negs <= 1:
12 | 		result = sum
13 | 
14 | 	for right in range(k, len(nums)):
15 | 		left = right - k
16 | 
17 | 		if nums[right] < 0:
18 | 			negs += 1
19 | 		sum += nums[right]
20 | 
21 | 		if nums[left] < 0:
22 | 			negs -= 1
23 | 		sum -= nums[left]
24 | 
25 | 		if negs <= 1:
26 | 			result = max(result, sum)
27 | 
28 | 	return result
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     negs = 0
 3 |     sum = 0
 4 |     result = 0
 5 | 
 6 |     for i in range(k):
 7 |         if nums[i] < 0:
 8 |             negs += 1
 9 |         sum += nums[i]
10 | 
11 |     if negs <= 1:
12 |         result = sum
13 | 
14 |     for right in range(k, len(nums)):
15 |         left = right - k
16 | 
17 |         if nums[right] < 0:
18 |             negs += 1
19 |         sum += nums[right]
20 | 
21 |         if nums[left] < 0:
22 |             negs -= 1
23 |         sum -= nums[left]
24 | 
25 |         if negs <= 1:
26 |             result = max(result, sum)
27 | 
28 |     return result
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01072737

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
 	int left = 0;
@@ -14,2 +15,3 @@
 	return count;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 | 	int left = 0;
 3 | 	int right = nums.length - 1;
 4 | 	int count = 0;
 5 | 
 6 | 	while (left < right) {
 7 | 		if (nums[left] + nums[right] <= T) {
 8 | 			count += (right - left);
 9 | 			left++;
10 | 		} else {
11 | 			right--;
12 | 		}
13 | 	}
14 | 	return count;
15 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 | 	int left = 0;
 4 | 	int right = nums.length - 1;
 5 | 	int count = 0;
 6 | 
 7 | 	while (left < right) {
 8 | 		if (nums[left] + nums[right] <= T) {
 9 | 			count += (right - left);
10 | 			left++;
11 | 		} else {
12 | 			right--;
13 | 		}
14 | 	}
15 | 	return count;
16 | }
17 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01073119 — Ivan Cheung

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01073119

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |         windowSum =  sum(nums[:k])
 3 |         countNeg = sum(1 for x in nums[:k] if x < 0)
 4 | 
 5 |         maxSum = windowSum if countNeg <= 1 else 0
 6 | 
 7 |         for i in range(k, len(nums)):
 8 |            incoming = nums[i]
 9 |            outgoing = nums[i - k]
10 | 
11 |            windowSum += incoming - outgoing
12 | 
13 |            if incoming < 0:
14 |                countNeg += 1
15 |            if outgoing < 0:
16 |                countNeg -= 1
17 |            if countNeg <= 1:
18 |                maxSum = max(maxSum, windowSum)
19 | 
20 |         return maxSum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |         windowSum =  sum(nums[:k])
 3 |         countNeg = sum(1 for x in nums[:k] if x < 0)
 4 | 
 5 |         maxSum = windowSum if countNeg <= 1 else 0
 6 | 
 7 |         for i in range(k, len(nums)):
 8 |            incoming = nums[i]
 9 |            outgoing = nums[i - k]
10 | 
11 |            windowSum += incoming - outgoing
12 | 
13 |            if incoming < 0:
14 |                countNeg += 1
15 |            if outgoing < 0:
16 |                countNeg -= 1
17 |            if countNeg <= 1:
18 |                maxSum = max(maxSum, windowSum)
19 | 
20 |         return maxSum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01073119

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01074783 — Noel Maldonado

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01074783

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     neg_count = sum(1 for x in nums[:k] if x < 0)
 3 |     window_sum = sum(nums[:k])
 4 |     max_sum = window_sum if neg_count <= 1 else float('-inf')
 5 |     
 6 |     for i in range(1, len(nums) - k + 1):
 7 |         window_sum += nums[i + k - 1] - nums[i - 1]
 8 |         if nums[i + k - 1] < 0:
 9 |             neg_count += 1
10 |         if nums[i - 1] < 0:
11 |             neg_count -= 1
12 |         if neg_count <= 1:
13 |             max_sum = max(max_sum, window_sum)
14 |     return 0 if max_sum == float('-inf') else max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     neg_count = sum(1 for x in nums[:k] if x < 0)
 3 |     window_sum = sum(nums[:k])
 4 |     max_sum = window_sum if neg_count <= 1 else float('-inf')
 5 |     
 6 |     for i in range(1, len(nums) - k + 1):
 7 |         window_sum += nums[i + k - 1] - nums[i - 1]
 8 |         if nums[i + k - 1] < 0:
 9 |             neg_count += 1
10 |         if nums[i - 1] < 0:
11 |             neg_count -= 1
12 |         if neg_count <= 1:
13 |             max_sum = max(max_sum, window_sum)
14 |     return 0 if max_sum == float('-inf') else max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01074783

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left, right = 0, len(nums) - 1
 3 |     count = 0
 4 |     
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += right - left
 8 |             left += 1
 9 |         else: 
10 |             right -= 1
11 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left, right = 0, len(nums) - 1
 3 |     count = 0
 4 |     
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += right - left
 8 |             left += 1
 9 |         else: 
10 |             right -= 1
11 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         indices = {}
 4 |         for idx, val in enumerate(nums):
 5 |             if val not in indices:
 6 |                 indices[val] = []
 7 |             indices[val].append(idx)
 8 |         min_dist = float('inf')
 9 | 
10 |         for positions in indices.values():
11 |             if len(positions) < 3:
12 |                 continue
13 |             for i in range(len(positions) - 2):
14 |                 dist = 2 * (positions[i + 2] - positions[i])
15 |                 min_dist = min(min_dist, dist)
16 |         return -1 if min_dist == float('inf') else min_dist
17 | 
18 | The time complexity of this program is O(n). Only does one pass for the indices dictionary. It solved the problem by completing the math correctly to find the indexes. 
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01077946 — Xinlin Wu

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01077946

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     left = 0
 3 |     curr_sum = 0
 4 |     res = 0
 5 |     neg_counter = 0
 6 |     valid = False
 7 | 
 8 |     for right in range(len(nums)):
 9 |         curr_sum += nums[right]
10 | 
11 |         if nums[right] < 0:
12 |             neg_counter += 1
13 | 
14 |         if (right - left + 1) > k:
15 |             if nums[left] < 0:
16 |                 neg_counter -= 1
17 |             curr_sum -= nums[left]
18 |             left += 1
19 |         
20 |         if (right - left + 1) < k:
21 |             continue
22 | 
23 |         if neg_counter > 1:
24 |             continue
25 | 
26 |         if not valid:
27 |             res = curr_sum
28 |             valid = True
29 |         else:
30 |             if curr_sum > res:
31 |                 res = curr_sum
32 | 
33 |     return res if valid else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     left = 0
 3 |     curr_sum = 0
 4 |     res = 0
 5 |     neg_counter = 0
 6 |     valid = False
 7 | 
 8 |     for right in range(len(nums)):
 9 |         curr_sum += nums[right]
10 | 
11 |         if nums[right] < 0:
12 |             neg_counter += 1
13 | 
14 |         if (right - left + 1) > k:
15 |             if nums[left] < 0:
16 |                 neg_counter -= 1
17 |             curr_sum -= nums[left]
18 |             left += 1
19 |         
20 |         if (right - left + 1) < k:
21 |             continue
22 | 
23 |         if neg_counter > 1:
24 |             continue
25 | 
26 |         if not valid:
27 |             res = curr_sum
28 |             valid = True
29 |         else:
30 |             if curr_sum > res:
31 |                 res = curr_sum
32 | 
33 |     return res if valid else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01077946

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     res = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             res += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 |     
13 |     return res
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     res = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             res += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 |     
13 |     return res
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01084139 — Jin Noh

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01084139

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k: return 0 
 4 |     
 5 |     curr_sum = sum(nums[:k])
 6 |     neg_count = sum(1 for x in nums[:k] if x < 0)
 7 |     
 8 |     max_ans = -float('inf')
 9 |     found = False
10 |     
11 |     if neg_count <= 1:
12 |         max_ans = curr_sum
13 |         found = True
14 |         
15 |     for i in range(k, n):
16 |         if nums[i] < 0: neg_count += 1
17 |         curr_sum += nums[i]
18 |         
19 |         if nums[i-k] < 0: neg_count -= 1
20 |         curr_sum -= nums[i-k]
21 |         
22 |         if neg_count <= 1:
23 |             max_ans = max(max_ans, curr_sum)
24 |             found = True
25 |             
26 |     return max_ans if found else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k: return 0 
 4 |     
 5 |     curr_sum = sum(nums[:k])
 6 |     neg_count = sum(1 for x in nums[:k] if x < 0)
 7 |     
 8 |     max_ans = -float('inf')
 9 |     found = False
10 |     
11 |     if neg_count <= 1:
12 |         max_ans = curr_sum
13 |         found = True
14 |         
15 |     for i in range(k, n):
16 |         if nums[i] < 0: neg_count += 1
17 |         curr_sum += nums[i]
18 |         
19 |         if nums[i-k] < 0: neg_count -= 1
20 |         curr_sum -= nums[i-k]
21 |         
22 |         if neg_count <= 1:
23 |             max_ans = max(max_ans, curr_sum)
24 |             found = True
25 |             
26 |     return max_ans if found else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01084139

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         
 9 |         if current_sum <= T:
10 | 
11 |             count += (right - left)
12 |             left += 1
13 | 
14 |         else:
15 |             right -= 1
16 |             
17 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         
 9 |         if current_sum <= T:
10 | 
11 |             count += (right - left)
12 |             left += 1
13 | 
14 |         else:
15 |             right -= 1
16 |             
17 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01084354 — Reginald Juance

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01084354

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     negative_count = 0
 4 |     max_sum = 0
 5 | 
 6 |     for i in range(k):
 7 |         window_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             negative_count += 1
10 | 
11 |     if negative_count <= 1:
12 |         max_sum = window_sum
13 | 
14 |     for i in range(k, len(nums)):
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             negative_count += 1
18 | 
19 |         if nums[i - k] < 0:
20 |             negative_count -= 1
21 | 
22 |         window_sum -= nums[i - k]
23 | 
24 |         if negative_count <= 1:
25 |             max_sum = max(max_sum, window_sum)
26 | 
27 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     negative_count = 0
 4 |     max_sum = 0
 5 | 
 6 |     for i in range(k):
 7 |         window_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             negative_count += 1
10 | 
11 |     if negative_count <= 1:
12 |         max_sum = window_sum
13 | 
14 |     for i in range(k, len(nums)):
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             negative_count += 1
18 | 
19 |         if nums[i - k] < 0:
20 |             negative_count -= 1
21 | 
22 |         window_sum -= nums[i - k]
23 | 
24 |         if negative_count <= 1:
25 |             max_sum = max(max_sum, window_sum)
26 | 
27 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01084354

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | N/A
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01090335 — Jake Steck

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01090335

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = float('-inf')
 3 |     current_sum = 0
 4 |     neg_count = 0
 5 |     found_valid = False
 6 | 
 7 |     for i in range(len(nums)):
 8 |         current_sum += nums[i]
 9 |         if nums[i] < 0:
10 |             neg_count += 1
11 |         
12 |         if i >= k:
13 |             outgoing = nums[i - k]
14 |             current_sum -= outgoing
15 |             if outgoing < 0:
16 |                 neg_count -= 1
17 |         
18 |         if i >= k - 1:
19 |             if neg_count <= 1:
20 |                 max_sum = max(max_sum, current_sum)
21 |                 found_valid = True
22 |                 
23 |     return max_sum if found_valid else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = float('-inf')
 3 |     current_sum = 0
 4 |     neg_count = 0
 5 |     found_valid = False
 6 | 
 7 |     for i in range(len(nums)):
 8 |         current_sum += nums[i]
 9 |         if nums[i] < 0:
10 |             neg_count += 1
11 |         
12 |         if i >= k:
13 |             outgoing = nums[i - k]
14 |             current_sum -= outgoing
15 |             if outgoing < 0:
16 |                 neg_count -= 1
17 |         
18 |         if i >= k - 1:
19 |             if neg_count <= 1:
20 |                 max_sum = max(max_sum, current_sum)
21 |                 found_valid = True
22 |                 
23 |     return max_sum if found_valid else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01090335

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         if current_sum <= T:
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |             
14 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         if current_sum <= T:
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |             
14 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01126559 — Shunyi Chen

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01126559

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     negative_count = 0
 4 |     max_sum = 0
 5 | 
 6 |     for i in range(k):
 7 |         window_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             negative_count += 1
10 | 
11 |     if negative_count <= 1:
12 |         max_sum = window_sum
13 | 
14 |     for i in range(k, len(nums)):
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             negative_count += 1
18 | 
19 |         if nums[i - k] < 0:
20 |             negative_count -= 1
21 |         window_sum -= nums[i - k]
22 | 
23 |         if negative_count <= 1:
24 |             max_sum = max(max_sum, window_sum)
25 | 
26 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     negative_count = 0
 4 |     max_sum = 0
 5 | 
 6 |     for i in range(k):
 7 |         window_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             negative_count += 1
10 | 
11 |     if negative_count <= 1:
12 |         max_sum = window_sum
13 | 
14 |     for i in range(k, len(nums)):
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             negative_count += 1
18 | 
19 |         if nums[i - k] < 0:
20 |             negative_count -= 1
21 |         window_sum -= nums[i - k]
22 | 
23 |         if negative_count <= 1:
24 |             max_sum = max(max_sum, window_sum)
25 | 
26 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01126559

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | class Solution(object):
 2 |     def minimumDistance(self, nums):
 3 |         positions = {}
 4 |         
 5 |         for i in range(len(nums)):
 6 |             val = nums[i]
 7 |             if val not in positions:
 8 |                 positions[val] = []
 9 |             positions[val].append(i)
10 |         
11 |         ans = -1 
12 |         
13 |         for val in positions:
14 |             idxs = positions[val]
15 |             
16 |             if len(idxs) < 3:
17 |                 continue
18 |             
19 |             for i in range(len(idxs) - 2):
20 |                 distance = 2 * (idxs[i + 2] - idxs[i])
21 |                 
22 |                 if ans == -1 or distance < ans:
23 |                     ans = distance
24 |         
25 |         return ans
26 | 
27 | explanation:
28 | time complexity of O(n^2) but since constraint is that num.lengh is <= 100 time complexity will never actually be that big at least in the context of this problem.
29 | this solves the problem because what this code does is it groups the indices of every equal value, but it will only check the values that appear 3 times, then it will check which has the smallest possible span of those values that appear 3 times. and i also managed to shorten down the formula because i realized the index of the 2nd occurrence of the number doesnt actually matter in the end, and this also made it so i didnt actually have to check every truple in my 2d array, only consecutive ones so i just used a sliding window of size 3
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01131708 — Jason Seng

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01131708

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k:
 4 |         return 0
 5 |     
 6 |     current_sum = 0
 7 |     neg_count = 0
 8 |     max_sum = float('-inf')
 9 |     found_valid = False
10 |     
11 |     for i in range(k):
12 |         current_sum += nums[i]
13 |         if nums[i] < 0:
14 |             neg_count += 1
15 |             
16 |     if neg_count <= 1:
17 |         max_sum = current_sum
18 |         found_valid = True
19 |         
20 |     for i in range(k, n):
21 |         current_sum += nums[i]
22 |         if nums[i] < 0:
23 |             neg_count += 1
24 |             
25 |         outgoing = nums[i - k]
26 |         current_sum -= outgoing
27 |         if outgoing < 0:
28 |             neg_count -= 1
29 |             
30 |         if neg_count <= 1:
31 |             max_sum = max(max_sum, current_sum)
32 |             found_valid = True
33 |             
34 |     return max_sum if found_valid else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k:
 4 |         return 0
 5 |     
 6 |     current_sum = 0
 7 |     neg_count = 0
 8 |     max_sum = float('-inf')
 9 |     found_valid = False
10 |     
11 |     for i in range(k):
12 |         current_sum += nums[i]
13 |         if nums[i] < 0:
14 |             neg_count += 1
15 |             
16 |     if neg_count <= 1:
17 |         max_sum = current_sum
18 |         found_valid = True
19 |         
20 |     for i in range(k, n):
21 |         current_sum += nums[i]
22 |         if nums[i] < 0:
23 |             neg_count += 1
24 |             
25 |         outgoing = nums[i - k]
26 |         current_sum -= outgoing
27 |         if outgoing < 0:
28 |             neg_count -= 1
29 |             
30 |         if neg_count <= 1:
31 |             max_sum = max(max_sum, current_sum)
32 |             found_valid = True
33 |             
34 |     return max_sum if found_valid else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01131708

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 |             
13 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 |             
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01132822 — Matthew Park

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01132822

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | # Online Python - IDE, Editor, Compiler, Interpreter
 2 | def max_valid_window_sum(nums, k):
 3 |     #debug
 4 |     # print("nums = ", nums)
 5 |     # print("k = ", k)
 6 |     #if empty/None/0/negative
 7 |     if (k <= 0) or (not nums):
 8 |         return 0
 9 |     sum = 0
10 |     negativeCount = 0
11 |     maxSum = 0
12 |     maxSumExists = False#maxSum may be < 0
13 |     #initialize vars
14 |     for n in range(k):
15 |         sum += nums[n]
16 |         if nums[n] < 0:
17 |             negativeCount += 1
18 |     if negativeCount <= 1:
19 |         maxSum = sum
20 |         maxSumExists = True
21 |     rightPointer = k - 1
22 |     #leftPointer = r - k + 1
23 |     while rightPointer + 1 < len(nums):
24 |         rightPointer += 1
25 |         #right
26 |         sum += nums[rightPointer]
27 |         if nums[rightPointer] < 0:
28 |             negativeCount += 1
29 |         #left
30 |         sum -= nums[rightPointer - k]
31 |         if nums[rightPointer - k] < 0:
32 |             negativeCount -= 1
33 |         if negativeCount <= 1:
34 |             maxSum = max(maxSum, sum)
35 |             maxSumExists = True
36 |             
37 |         #debug
38 |         # print("rightPointer = ", rightPointer)
39 |         # print("negativeCount = ", negativeCount)
40 |         # print("sum = ", sum)
41 |         # print("maxSum = ", maxSum)
42 |         # print("maxSumExists = ", maxSumExists)
43 |     if maxSumExists:
44 |         return maxSum
45 |     else:
46 |         return 0
47 |         
```

**Fixed input:**

```
 1 | # Online Python - IDE, Editor, Compiler, Interpreter
 2 | def max_valid_window_sum(nums, k):
 3 |     #debug
 4 |     # print("nums = ", nums)
 5 |     # print("k = ", k)
 6 |     #if empty/None/0/negative
 7 |     if (k <= 0) or (not nums):
 8 |         return 0
 9 |     sum = 0
10 |     negativeCount = 0
11 |     maxSum = 0
12 |     maxSumExists = False#maxSum may be < 0
13 |     #initialize vars
14 |     for n in range(k):
15 |         sum += nums[n]
16 |         if nums[n] < 0:
17 |             negativeCount += 1
18 |     if negativeCount <= 1:
19 |         maxSum = sum
20 |         maxSumExists = True
21 |     rightPointer = k - 1
22 |     #leftPointer = r - k + 1
23 |     while rightPointer + 1 < len(nums):
24 |         rightPointer += 1
25 |         #right
26 |         sum += nums[rightPointer]
27 |         if nums[rightPointer] < 0:
28 |             negativeCount += 1
29 |         #left
30 |         sum -= nums[rightPointer - k]
31 |         if nums[rightPointer - k] < 0:
32 |             negativeCount -= 1
33 |         if negativeCount <= 1:
34 |             maxSum = max(maxSum, sum)
35 |             maxSumExists = True
36 |             
37 |         #debug
38 |         # print("rightPointer = ", rightPointer)
39 |         # print("negativeCount = ", negativeCount)
40 |         # print("sum = ", sum)
41 |         # print("maxSum = ", maxSum)
42 |         # print("maxSumExists = ", maxSumExists)
43 |     if maxSumExists:
44 |         return maxSum
45 |     else:
46 |         return 0
47 |         
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01132822

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     #print("nums = ", nums, "T = ", T)
 3 |     #problem does not say what to happens if T is uninitialized, so i'm returning -1
 4 |     if T is None:
 5 |         return -1
 6 |     l = 0
 7 |     r = len(nums) - 1
 8 |     numPairs = 0
 9 |     while l < r:
10 |         sum = nums[l] + nums[r]
11 |         if sum <= T:
12 |             #all pairs (l, x) work l < x <= r
13 |             numPairs += r - l
14 |             #print("numPairs += ", str(r - l), ", r = ", r, "l = ", l)
15 |             
16 |             #inc l
17 |             l += 1
18 |         else:
19 |             #dec r
20 |             r -= 1
21 |             #print("dec r")
22 |     return numPairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     #print("nums = ", nums, "T = ", T)
 3 |     #problem does not say what to happens if T is uninitialized, so i'm returning -1
 4 |     if T is None:
 5 |         return -1
 6 |     l = 0
 7 |     r = len(nums) - 1
 8 |     numPairs = 0
 9 |     while l < r:
10 |         sum = nums[l] + nums[r]
11 |         if sum <= T:
12 |             #all pairs (l, x) work l < x <= r
13 |             numPairs += r - l
14 |             #print("numPairs += ", str(r - l), ", r = ", r, "l = ", l)
15 |             
16 |             #inc l
17 |             l += 1
18 |         else:
19 |             #dec r
20 |             r -= 1
21 |             #print("dec r")
22 |     return numPairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | https://i.postimg.cc/m2J1ws86/image.png
 2 | class Solution:
 3 |     def minimumDistance(self, nums: List[int]) -> int:
 4 |         #create dic
 5 |         dic = {key: list() for key in nums} #line 4
 6 |         #print(dic)
 7 |         for i, key in enumerate(nums):
 8 |             dic[key].append(i) #line 8
 9 |             #print(dic)
10 |         #print(dic)
11 |         minDistance = 1000000 #line 11
12 |         for value in dic.values():
13 |             if(len(value) >= 3):
14 |                 #find distance
15 |                 #2 pointer sliding window
16 |                 i = 2#index of value - represents right index
17 |                 while i < len(value):
18 |                     minDistance = min((value[i] - value[i-2]) * 2, minDistance)
19 |                     i += 1
20 |         if minDistance == 1000000:
21 |             return -1 #line 21
22 |         return minDistance
23 | 
24 | 
25 | My solution is broken down into two parts: create a dictionary from which I can easily find all good tuples (lines 4-8), and find the minimum of all good tuples (lines 11-21). The dictionary's keys are all values in nums, and the dictionary's values are the indicies of nums at which those values appear. Appending to the end of a list has a time complexity of O(1), and since I iterate through nums, the time complexity of part 1 is O(1 * n) = O(n).
26 | 
27 | I initialize minDistance with 1,000,000 because n is at most 100,000, which is less than 1,000,000.
28 | 
29 | To find the distance, I only need to find the lowest and highest values of the tuple. Since the list (the value of the dictionary) comes pre-sorted, I use a sliding window and iterate through the list to find the value. Finding the minimum distance is time complexity O(1) since random access and arithmetic operations are both O(1). Iterating through the list is time complexity O(1 * n) = O(n), and iterating through dictionary is still O(n) because the number of elements in the list is a grand total of n, not n^2. Therefore, the time complexity of part 2 is O(n).
30 | 
31 | The time complexity for the whole program is O(n) + O(n) = O(n).
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01143122 — Kartik Wahlin

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01143122

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     lengthNow = 0
 3 |     numNegatives = 0
 4 |     maxm = float('-inf')
 5 |     foundValid = False
 6 |     for i in range(k):
 7 |         lengthNow += nums[i]
 8 |         if nums[i] < 0:
 9 |             numNegatives += 1
10 |     if numNegatives <= 1:
11 |         maxm = lengthNow
12 |         foundValid = True
13 |     for i in range(k, len(nums)):
14 |         lengthNow += nums[i]
15 |         if nums[i] < 0:
16 |             numNegatives += 1
17 |         lengthNow -= nums[i - k]
18 |         if nums[i - k] < 0:
19 |             numNegatives -= 1
20 |         if numNegatives <= 1:
21 |             maxm = max(maxm, lengthNow)
22 |             foundValid = True
23 | 
24 |     return maxm if foundValid else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     lengthNow = 0
 3 |     numNegatives = 0
 4 |     maxm = float('-inf')
 5 |     foundValid = False
 6 |     for i in range(k):
 7 |         lengthNow += nums[i]
 8 |         if nums[i] < 0:
 9 |             numNegatives += 1
10 |     if numNegatives <= 1:
11 |         maxm = lengthNow
12 |         foundValid = True
13 |     for i in range(k, len(nums)):
14 |         lengthNow += nums[i]
15 |         if nums[i] < 0:
16 |             numNegatives += 1
17 |         lengthNow -= nums[i - k]
18 |         if nums[i - k] < 0:
19 |             numNegatives -= 1
20 |         if numNegatives <= 1:
21 |             maxm = max(maxm, lengthNow)
22 |             foundValid = True
23 | 
24 |     return maxm if foundValid else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01143122

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 | 
12 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 | 
12 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | def minimumDistance(self, nums: List[int]) -> int:
 2 |     valToIndex = defaultdict(list)
 3 | 
 4 |     for i, num in enumerate(nums):
 5 |         valToIndex[num].append(i) 
 6 |     minDist = float('inf')
 7 |     for val, indices in valToIndex.items():
 8 |         for i in range(2, len(indices)):
 9 |             minDist = min(minDist, 2 * (indices[i] - indices[i - 2]))
10 |     if minDist < float('inf'):
11 |         return minDist
12 |     return -1
13 | 
14 | #given: array nums
15 | #find: triplets where values are equal and total distance is largest
16 | 
17 | #Brute force: O(n^3)
18 | #hash map:  O(n) space
19 | # Keep a list of indices and iterate through. For each one, the min has to be 3 consecutive ones in the hashmap's list
20 | 
21 | EXPLANATION:
22 | my solution creates a hash map using elements' values as their keys, with the map values containing a list of their indices. This allows us to quickly access the indices of potential solutions(good pairs) once it is built.
23 | It then iterates through each of these 
24 | 
25 | This solution runs with a time complexity of O(n). It iterates over the full list once, when creating the hash map. It then iterates over the created lists, but will not visit more than n triplets. This is less than O(2n), resulting in a big o of O(n).
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01144790 — Lilian Yuan

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01144790

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k:
 4 |         return 0
 5 |     current_sum = 0
 6 |     neg_count = 0
 7 |     max_sum = float('-inf')
 8 |     found_valid = False
 9 | 
10 |     for i in range(k):
11 |         current_sum += nums[i]
12 |         if nums[i] < 0:
13 |             neg_count += 1     
14 |     if neg_count <= 1:
15 |         max_sum = current_sum
16 |         found_valid = True
17 | 
18 |     for i in range(k, n):
19 |         left_val = nums[i - k]
20 |         if left_val < 0:
21 |             neg_count -= 1
22 |         current_sum -= left_val
23 |         right_val = nums[i]
24 |         if right_val < 0:
25 |             neg_count += 1
26 |         current_sum += right_val
27 |         if neg_count <= 1:
28 |             if not found_valid:
29 |                 max_sum = current_sum
30 |                 found_valid = True
31 |             else:
32 |                 max_sum = max(max_sum, current_sum)
33 |     return max_sum if found_valid else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k:
 4 |         return 0
 5 |     current_sum = 0
 6 |     neg_count = 0
 7 |     max_sum = float('-inf')
 8 |     found_valid = False
 9 | 
10 |     for i in range(k):
11 |         current_sum += nums[i]
12 |         if nums[i] < 0:
13 |             neg_count += 1     
14 |     if neg_count <= 1:
15 |         max_sum = current_sum
16 |         found_valid = True
17 | 
18 |     for i in range(k, n):
19 |         left_val = nums[i - k]
20 |         if left_val < 0:
21 |             neg_count -= 1
22 |         current_sum -= left_val
23 |         right_val = nums[i]
24 |         if right_val < 0:
25 |             neg_count += 1
26 |         current_sum += right_val
27 |         if neg_count <= 1:
28 |             if not found_valid:
29 |                 max_sum = current_sum
30 |                 found_valid = True
31 |             else:
32 |                 max_sum = max(max_sum, current_sum)
33 |     return max_sum if found_valid else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01144790

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | N/A
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01171535 — Kushagra Singh

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01171535

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     # Initialize variables for the first window
 3 |     window_sum = sum(nums[0:k])
 4 |     neg_count = 0
 5 |     for i in range(k):
 6 |         if nums[i] < 0:
 7 |             neg_count += 1
 8 |     # Track the maximum valid sum, start at 0 (return 0 if no valid window)
 9 |     max_sum = 0
10 |     # Check if first window is valid
11 |     if neg_count <= 1:
12 |         max_sum = window_sum
13 |     # Slide the window across the rest of the array
14 |     for i in range(1, len(nums) - k + 1):
15 |         # Add the new element entering the window (right side)
16 |         window_sum += nums[i + k - 1]
17 |         # Remove the element leaving the window (left side)
18 |         window_sum -= nums[i - 1]
19 |         # Update negative count based on what left and what entered
20 |         if nums[i - 1] < 0:
21 |             neg_count -= 1
22 |         if nums[i + k - 1] < 0:
23 |             neg_count += 1
24 |         # If valid window, check against current max
25 |         if neg_count <= 1:
26 |             max_sum = max(max_sum, window_sum)
27 |     
28 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     # Initialize variables for the first window
 3 |     window_sum = sum(nums[0:k])
 4 |     neg_count = 0
 5 |     for i in range(k):
 6 |         if nums[i] < 0:
 7 |             neg_count += 1
 8 |     # Track the maximum valid sum, start at 0 (return 0 if no valid window)
 9 |     max_sum = 0
10 |     # Check if first window is valid
11 |     if neg_count <= 1:
12 |         max_sum = window_sum
13 |     # Slide the window across the rest of the array
14 |     for i in range(1, len(nums) - k + 1):
15 |         # Add the new element entering the window (right side)
16 |         window_sum += nums[i + k - 1]
17 |         # Remove the element leaving the window (left side)
18 |         window_sum -= nums[i - 1]
19 |         # Update negative count based on what left and what entered
20 |         if nums[i - 1] < 0:
21 |             neg_count -= 1
22 |         if nums[i + k - 1] < 0:
23 |             neg_count += 1
24 |         # If valid window, check against current max
25 |         if neg_count <= 1:
26 |             max_sum = max(max_sum, window_sum)
27 |     
28 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01171535

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     count = 0
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         if current_sum <= T:
 9 |             # All pairs between left and right are valid
10 |             # (left, left+1), (left, left+2) ... (left, right)
11 |             count += (right - left)
12 |             left += 1
13 |         else:
14 |             # Sum is too big, move right pointer inward
15 |             right -= 1
16 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     count = 0
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 |         if current_sum <= T:
 9 |             # All pairs between left and right are valid
10 |             # (left, left+1), (left, left+2) ... (left, right)
11 |             count += (right - left)
12 |             left += 1
13 |         else:
14 |             # Sum is too big, move right pointer inward
15 |             right -= 1
16 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `java`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | class Solution {
 2 | public:
 3 | 
 4 | int minimumDistance(vector<int>& nums) {
 5 |     unordered_map<int, vector<int>> indexMap;
 6 |     for (int i = 0; i < nums.size(); i++) {
 7 |         indexMap[nums[i]].push_back(i);
 8 |     }
 9 |     int minDist = INT_MAX;
10 |     for (auto& [val, indices] : indexMap) {
11 |         if (indices.size() < 3) continue;
12 |         for (int t = 0; t + 2 < indices.size(); t++) {
13 |             int i = indices[t];
14 |             int j = indices[t + 1];
15 |             int k = indices[t + 2];
16 |             int dist = 2 * (k - i);
17 |             minDist = min(minDist, dist);
18 |         }
19 |     }
20 |     return minDist == INT_MAX ? -1 : minDist;
21 | }
22 | };
23 | 
24 | 
25 | 
26 | I group indices by value using a hash map, then for each value with at least 3 occurrences, I slide over consecutive triples and compute 2 * (k - i) as the simplified distance. Since indices are stored in sorted order, consecutive triples always minimize k - i, guaranteeing the optimal result. Overall time complexity is O(n) since every index is visited at most once.
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01171723 — Sude Genc

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01171723

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     negative_count = 0
 4 |     max_sum = float('-inf')
 5 |     for i in range(k):
 6 |         window_sum += nums[i]
 7 |         if nums[i] < 0:
 8 |             negative_count += 1
 9 |     if negative_count <= 1:
10 |         max_sum = window_sum
11 |     for i in range(k, len(nums)):
12 |         if nums[i - k] < 0:
13 |             negative_count -= 1
14 |         window_sum -= nums[i - k]
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             negative_count += 1
18 |         if negative_count <= 1:
19 |             max_sum = max(max_sum, window_sum)
20 |     if max_sum == float('-inf'):
21 |         return 0
22 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     negative_count = 0
 4 |     max_sum = float('-inf')
 5 |     for i in range(k):
 6 |         window_sum += nums[i]
 7 |         if nums[i] < 0:
 8 |             negative_count += 1
 9 |     if negative_count <= 1:
10 |         max_sum = window_sum
11 |     for i in range(k, len(nums)):
12 |         if nums[i - k] < 0:
13 |             negative_count -= 1
14 |         window_sum -= nums[i - k]
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             negative_count += 1
18 |         if negative_count <= 1:
19 |             max_sum = max(max_sum, window_sum)
20 |     if max_sum == float('-inf'):
21 |         return 0
22 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01171723

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01172719 — Varun Karamchandani

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01172719

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     neg_count = 0
 4 |     
 5 |     # first window
 6 |     for i in range(k):
 7 |         window_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             neg_count += 1
10 |     
11 |     if neg_count <= 1:
12 |         max_sum = window_sum
13 |     else:
14 |         max_sum = float('-inf')
15 |     
16 |     # slide window
17 |     for i in range(k, len(nums)):
18 |         window_sum += nums[i]
19 |         if nums[i] < 0:
20 |             neg_count += 1
21 |         
22 |         old = nums[i - k]
23 |         window_sum -= old
24 |         if old < 0:
25 |             neg_count -= 1
26 |         
27 |         if neg_count <= 1:
28 |             max_sum = max(max_sum, window_sum)
29 |     
30 |     return max_sum if max_sum != float('-inf') else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     neg_count = 0
 4 |     
 5 |     # first window
 6 |     for i in range(k):
 7 |         window_sum += nums[i]
 8 |         if nums[i] < 0:
 9 |             neg_count += 1
10 |     
11 |     if neg_count <= 1:
12 |         max_sum = window_sum
13 |     else:
14 |         max_sum = float('-inf')
15 |     
16 |     # slide window
17 |     for i in range(k, len(nums)):
18 |         window_sum += nums[i]
19 |         if nums[i] < 0:
20 |             neg_count += 1
21 |         
22 |         old = nums[i - k]
23 |         window_sum -= old
24 |         if old < 0:
25 |             neg_count -= 1
26 |         
27 |         if neg_count <= 1:
28 |             max_sum = max(max_sum, window_sum)
29 |     
30 |     return max_sum if max_sum != float('-inf') else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01172719

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             # all pairs b/w left and right work cause sorted
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |     
14 |     return count
15 | # Note: I believe the correct output for Example 1 is 5 not 4 the pair (2,4) with sum 6 is also valid but missing from the problem.
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             # all pairs b/w left and right work cause sorted
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |     
14 |     return count
15 | # Note: I believe the correct output for Example 1 is 5 not 4 the pair (2,4) with sum 6 is also valid but missing from the problem.
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         indices = {}
 4 |         for i in range(len(nums)):
 5 |             if nums[i] not in indices:
 6 |                 indices[nums[i]] = []
 7 |             indices[nums[i]].append(i)
 8 |         
 9 |         min_dist = float('inf')
10 |         
11 |         for value in indices:
12 |             idx_list = indices[value]
13 |             if len(idx_list) < 3:
14 |                 continue
15 |             
16 |             for i in range(len(idx_list) - 2):
17 |                 p = idx_list[i]
18 |                 q = idx_list[i + 1]
19 |                 r = idx_list[i + 2]
20 |                 dist = 2 * (r - p)
21 |                 min_dist = min(min_dist, dist)
22 |         
23 |         return min_dist if min_dist != float('inf') else -1
24 | 
25 | Time Complexity: O(n) because we loop through the array once to build the dictionary then check the consecutive triplets.
26 | I grouped all the indices by their values using a dictionary. Then for each value that appears 3+ times I checked every three consecutive indices and calculated the distance using the formula from the hint (2 * (max - min)) and Kept track of the minimum distance found.
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01063628 — Monica Gnajewski

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01063628

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |      curr = 0
 3 |      maxSum = 0
 4 |      neg = 0
 5 |      left = 0
 6 | 
 7 |      for right in range(len(nums)):
 8 |           curr = curr + nums[right]
 9 |           if nums[right] < 0:
10 |                     neg += 1
11 | 
12 |           if (right - left) + 1 > k:
13 |                     if nums[left] < 0:
14 |                               neg -= 1
15 |                     curr -= nums[left]
16 |                     left += 1
17 | 
18 |           if (right - left) + 1 == k and neg <= 1:
19 |                     maxSum = max(maxSum, curr)
20 |      
21 |      return maxSum
22 | 
23 | 
24 | 
25 |               
26 | 
27 | 
28 | 
29 |      
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |      curr = 0
 3 |      maxSum = 0
 4 |      neg = 0
 5 |      left = 0
 6 | 
 7 |      for right in range(len(nums)):
 8 |           curr = curr + nums[right]
 9 |           if nums[right] < 0:
10 |                     neg += 1
11 | 
12 |           if (right - left) + 1 > k:
13 |                     if nums[left] < 0:
14 |                               neg -= 1
15 |                     curr -= nums[left]
16 |                     left += 1
17 | 
18 |           if (right - left) + 1 == k and neg <= 1:
19 |                     maxSum = max(maxSum, curr)
20 |      
21 |      return maxSum
22 | 
23 | 
24 | 
25 |               
26 | 
27 | 
28 | 
29 |      
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01063628

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,13 +1,13 @@
 def count_pairs(nums, T):
-	left = 0
-	right = len(nums) - 1
-	count = 0
+    left = 0
+    right = len(nums) - 1
+    count = 0
 
-	while left < right:
-		if nums[left] + nums[right] <= T:
-			count += right-left
-			left += 1
-		else:
-			right -= 1
+    while left < right:
+        if nums[left] + nums[right] <= T:
+            count += right-left
+            left += 1
+        else:
+            right -= 1
 
-	return count
+    return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 	left = 0
 3 | 	right = len(nums) - 1
 4 | 	count = 0
 5 | 
 6 | 	while left < right:
 7 | 		if nums[left] + nums[right] <= T:
 8 | 			count += right-left
 9 | 			left += 1
10 | 		else:
11 | 			right -= 1
12 | 
13 | 	return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right-left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01072761 — Andrew McBean

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01072761

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     neg_count = 0
 4 |     best = 0
 5 |     left = 0
 6 | 
 7 |     for right in range(len(nums)):
 8 |         window_sum += nums[right]
 9 |         if nums[right] < 0:
10 |             neg_count += 1
11 | 
12 |         # Shrink if window is too big
13 |         if right - left + 1 > k:
14 |             if nums[left] < 0:
15 |                 neg_count -= 1
16 |             window_sum -= nums[left]
17 |             left += 1
18 | 
19 |         # Check valid window of exact size k
20 |         if right - left + 1 == k and neg_count <= 1:
21 |             best = max(best, window_sum)
22 | 
23 |     return best
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     window_sum = 0
 3 |     neg_count = 0
 4 |     best = 0
 5 |     left = 0
 6 | 
 7 |     for right in range(len(nums)):
 8 |         window_sum += nums[right]
 9 |         if nums[right] < 0:
10 |             neg_count += 1
11 | 
12 |         # Shrink if window is too big
13 |         if right - left + 1 > k:
14 |             if nums[left] < 0:
15 |                 neg_count -= 1
16 |             window_sum -= nums[left]
17 |             left += 1
18 | 
19 |         # Check valid window of exact size k
20 |         if right - left + 1 == k and neg_count <= 1:
21 |             best = max(best, window_sum)
22 | 
23 |     return best
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01072761

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01096960 — Brian Lin

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01096960

| Tag | Change |
|---|---|
| [syntax-only] | added missing semicolons (1 line(s)) |
| [syntax-only] | fixed `.length()` -> `.length` (1x) |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,7 +1,8 @@
+public class Solution {
 public static int maxValidWindowSum(int[] nums, int k) {
    int max = 0;
    int sum = 0;
    int negatives = 0;
-   int size = nums.length();
+   int size = nums.length;
 
 
@@ -15,7 +16,7 @@
          negatives++;
       }
-      
+
       if(negatives <= 1){
-         max = sum
+         max = sum;
       }
    }
@@ -31,5 +32,5 @@
          negatives--;
       }
-      
+
       if(negatives <= 1){
          if(max < sum){
@@ -43,2 +44,3 @@
 
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) {
 2 |    int max = 0;
 3 |    int sum = 0;
 4 |    int negatives = 0;
 5 |    int size = nums.length();
 6 | 
 7 | 
 8 |    if(k > size){
 9 |       return 0;
10 |    }
11 | 
12 |    for(int i=0;i<k;i++){
13 |       sum += nums[i];
14 |       if(nums[i] < 0){
15 |          negatives++;
16 |       }
17 |       
18 |       if(negatives <= 1){
19 |          max = sum
20 |       }
21 |    }
22 | 
23 |    for(int i=k;i<size;i++){
24 |       sum += nums[i];
25 |       if(nums[i] < 0){
26 |          negatives++;
27 |       }
28 | 
29 |       sum -= nums[i-k];
30 |       if(nums[i-k] < 0){
31 |          negatives--;
32 |       }
33 |       
34 |       if(negatives <= 1){
35 |          if(max < sum){
36 |             max = sum;
37 |          }
38 |       }
39 | 
40 |    }
41 |    return max;
42 | 
43 | 
44 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int maxValidWindowSum(int[] nums, int k) {
 3 |    int max = 0;
 4 |    int sum = 0;
 5 |    int negatives = 0;
 6 |    int size = nums.length;
 7 | 
 8 | 
 9 |    if(k > size){
10 |       return 0;
11 |    }
12 | 
13 |    for(int i=0;i<k;i++){
14 |       sum += nums[i];
15 |       if(nums[i] < 0){
16 |          negatives++;
17 |       }
18 | 
19 |       if(negatives <= 1){
20 |          max = sum;
21 |       }
22 |    }
23 | 
24 |    for(int i=k;i<size;i++){
25 |       sum += nums[i];
26 |       if(nums[i] < 0){
27 |          negatives++;
28 |       }
29 | 
30 |       sum -= nums[i-k];
31 |       if(nums[i-k] < 0){
32 |          negatives--;
33 |       }
34 | 
35 |       if(negatives <= 1){
36 |          if(max < sum){
37 |             max = sum;
38 |          }
39 |       }
40 | 
41 |    }
42 |    return max;
43 | 
44 | 
45 | }
46 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01096960

| Tag | Change |
|---|---|
| [syntax-only] | added missing semicolons (2 line(s)) |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,4 +1,5 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
-   int left = 0
+   int left = 0;
    int right = nums.length - 1;
    int count = 0;
@@ -12,4 +13,5 @@
       }
    }
-   return count
+   return count;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 |    int left = 0
 3 |    int right = nums.length - 1;
 4 |    int count = 0;
 5 | 
 6 |    while(left < right){
 7 |       if(nums[left] + nums[right] <= T){
 8 |          count += right - left;
 9 |          left++;
10 |       }else{
11 |          right--;
12 |       }
13 |    }
14 |    return count
15 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 |    int left = 0;
 4 |    int right = nums.length - 1;
 5 |    int count = 0;
 6 | 
 7 |    while(left < right){
 8 |       if(nums[left] + nums[right] <= T){
 9 |          count += right - left;
10 |          left++;
11 |       }else{
12 |          right--;
13 |       }
14 |    }
15 |    return count;
16 | }
17 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01109304 — Ryan Zhang

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01109304

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     max_sum = 0
 4 |     
 5 |     for i in range(n - k + 1):
 6 |         current_sum = sum(nums[i:i+k])
 7 |         negatives = 0
 8 |         for x in nums[i:i+k]:
 9 |             if x < 0:
10 |                 negatives += 1
11 |         
12 |         if negatives <= 1:
13 |             max_sum = max(max_sum, current_sum)
14 |     
15 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     max_sum = 0
 4 |     
 5 |     for i in range(n - k + 1):
 6 |         current_sum = sum(nums[i:i+k])
 7 |         negatives = 0
 8 |         for x in nums[i:i+k]:
 9 |             if x < 0:
10 |                 negatives += 1
11 |         
12 |         if negatives <= 1:
13 |             max_sum = max(max_sum, current_sum)
14 |     
15 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01109304

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left, right = 0, len(nums) - 1
 3 |     count = 0
 4 |     
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |     
12 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left, right = 0, len(nums) - 1
 3 |     count = 0
 4 |     
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |     
12 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01143466 — Santiago Zuluaga

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01143466

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = 0
 3 |     curr = sum(nums[0:k])
 4 |     nc = 0
 5 |     
 6 |     for x in nums[0:k]:
 7 |         if x < 0:
 8 |             nc += 1
 9 |     
10 |     if nc <= 1:
11 |         max_sum = max(max_sum, curr)
12 |     
13 |     for i in range(len(nums) - k):
14 |         curr = curr - nums[i] + nums[i + k]
15 |         
16 |         if nums[i] < 0:
17 |             nc -= 1
18 |         if nums[i + k] < 0:
19 |             nc += 1
20 |         
21 |         if nc <= 1:
22 |             max_sum = max(max_sum, curr)
23 |     
24 |     return max_sum
25 |         
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = 0
 3 |     curr = sum(nums[0:k])
 4 |     nc = 0
 5 |     
 6 |     for x in nums[0:k]:
 7 |         if x < 0:
 8 |             nc += 1
 9 |     
10 |     if nc <= 1:
11 |         max_sum = max(max_sum, curr)
12 |     
13 |     for i in range(len(nums) - k):
14 |         curr = curr - nums[i] + nums[i + k]
15 |         
16 |         if nums[i] < 0:
17 |             nc -= 1
18 |         if nums[i + k] < 0:
19 |             nc += 1
20 |         
21 |         if nc <= 1:
22 |             max_sum = max(max_sum, curr)
23 |     
24 |     return max_sum
25 |         
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01143466

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,13 +1,13 @@
 def count_pairs(nums, T):
-	n_pairs = 0 
-	
-	l = 0 
-	r = len(nums) - 1 
-	while l < r:
-		if nums[l] + nums[r] > T:
-			r -= 1
-		elif nums[l] + nums[r] <= T:
-			n_pairs += r - l
-			l += 1
-	
-	return n_pairs
+    n_pairs = 0 
+    
+    l = 0 
+    r = len(nums) - 1 
+    while l < r:
+        if nums[l] + nums[r] > T:
+            r -= 1
+        elif nums[l] + nums[r] <= T:
+            n_pairs += r - l
+            l += 1
+    
+    return n_pairs
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 	n_pairs = 0 
 3 | 	
 4 | 	l = 0 
 5 | 	r = len(nums) - 1 
 6 | 	while l < r:
 7 | 		if nums[l] + nums[r] > T:
 8 | 			r -= 1
 9 | 		elif nums[l] + nums[r] <= T:
10 | 			n_pairs += r - l
11 | 			l += 1
12 | 	
13 | 	return n_pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     n_pairs = 0 
 3 |     
 4 |     l = 0 
 5 |     r = len(nums) - 1 
 6 |     while l < r:
 7 |         if nums[l] + nums[r] > T:
 8 |             r -= 1
 9 |         elif nums[l] + nums[r] <= T:
10 |             n_pairs += r - l
11 |             l += 1
12 |     
13 |     return n_pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01159005 — Abdoul Razakou Mahaman Sani

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01159005

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     i = 0
 3 |     j = k 
 4 |     result = 0
 5 |     while j <= len(nums):
 6 |         negative = 0 
 7 |         placeholder = 0
 8 |         for x in range(i,j):
 9 |             if nums[x]<0:
10 |                 negative = negative +1 
11 |             placeholder = placeholder + nums[x] 
12 |         if negative < 2:
13 |             result = placeholder
14 |         i = i +1 
15 |         j = j+1
16 |     return result
17 |                 
18 |         
19 |             
20 |             
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     i = 0
 3 |     j = k 
 4 |     result = 0
 5 |     while j <= len(nums):
 6 |         negative = 0 
 7 |         placeholder = 0
 8 |         for x in range(i,j):
 9 |             if nums[x]<0:
10 |                 negative = negative +1 
11 |             placeholder = placeholder + nums[x] 
12 |         if negative < 2:
13 |             result = placeholder
14 |         i = i +1 
15 |         j = j+1
16 |     return result
17 |                 
18 |         
19 |             
20 |             
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01159005

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 | 
11 |         else:
12 |            
13 |             right -= 1
14 |             
15 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 | 
11 |         else:
12 |            
13 |             right -= 1
14 |             
15 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01164020 — Justin Yu

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01164020

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -9,18 +9,18 @@
     
     
-	# Go through all indexes within nums
+    # Go through all indexes within nums
     for left in range(len(nums)-(k)):
         right = left + k 
 
         
-		# Check if window is valid
+        # Check if window is valid
         if negative <= 1 and window_sum > max_sum:
             max_sum = window_sum
             
-		# Summing the Window
+        # Summing the Window
         window_sum = window_sum - nums[left] + nums[right]
         
         
-		# Changing Negative counter
+        # Changing Negative counter
         if nums[left] < 0:
             negative = negative - 1
@@ -28,5 +28,5 @@
             negative = negative + 1
     
-	# Check last window
+    # Check last window
     if negative <= 1 and window_sum > max_sum:
             max_sum = window_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = 0
 3 |     negative = 0
 4 |     window_sum = 0
 5 |     for o in range(k):
 6 |         window_sum = window_sum + nums[o]
 7 |         if nums[o] < 0:
 8 |             negative = negative + 1
 9 |     
10 |     
11 | 	# Go through all indexes within nums
12 |     for left in range(len(nums)-(k)):
13 |         right = left + k 
14 | 
15 |         
16 | 		# Check if window is valid
17 |         if negative <= 1 and window_sum > max_sum:
18 |             max_sum = window_sum
19 |             
20 | 		# Summing the Window
21 |         window_sum = window_sum - nums[left] + nums[right]
22 |         
23 |         
24 | 		# Changing Negative counter
25 |         if nums[left] < 0:
26 |             negative = negative - 1
27 |         if nums[right] <0:
28 |             negative = negative + 1
29 |     
30 | 	# Check last window
31 |     if negative <= 1 and window_sum > max_sum:
32 |             max_sum = window_sum
33 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = 0
 3 |     negative = 0
 4 |     window_sum = 0
 5 |     for o in range(k):
 6 |         window_sum = window_sum + nums[o]
 7 |         if nums[o] < 0:
 8 |             negative = negative + 1
 9 |     
10 |     
11 |     # Go through all indexes within nums
12 |     for left in range(len(nums)-(k)):
13 |         right = left + k 
14 | 
15 |         
16 |         # Check if window is valid
17 |         if negative <= 1 and window_sum > max_sum:
18 |             max_sum = window_sum
19 |             
20 |         # Summing the Window
21 |         window_sum = window_sum - nums[left] + nums[right]
22 |         
23 |         
24 |         # Changing Negative counter
25 |         if nums[left] < 0:
26 |             negative = negative - 1
27 |         if nums[right] <0:
28 |             negative = negative + 1
29 |     
30 |     # Check last window
31 |     if negative <= 1 and window_sum > max_sum:
32 |             max_sum = window_sum
33 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01164020

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     num_pair = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             num_pair = num_pair + (right - left)
 9 |             left = left + 1
10 |         else:
11 |             right = right - 1
12 | 
13 |     return num_pair
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     num_pair = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             num_pair = num_pair + (right - left)
 9 |             left = left + 1
10 |         else:
11 |             right = right - 1
12 | 
13 |     return num_pair
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01132918 — Kenneth Ng

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01132918

| Tag | Change |
|---|---|
| [syntax-only] | line 31: added missing colon |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -29,5 +29,5 @@
   do {
     const isValid = window.filter((num) => num < 0).length === 1;
-    if (isValid) {
+    if (isValid) {:
         const sum = window.reduce((acc, curr) => acc + curr, 0);
         max = Math.max(max, sum);
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |   window = nums[:k]
 3 |   max_num = 0
 4 | 
 5 |   while True:
 6 |     num_negatives = 0
 7 |     sum = 0
 8 |     for num in window:
 9 |       if num < 0: num_negatives += 1
10 |       if num_negatives > 1: break
11 |       sum += num
12 | 
13 |     if num_negatives > 1: break
14 |     max_num = max(sum, max_num)
15 | 
16 |     window.pop(0)
17 |     if k <= len(nums) - 1: window.append(nums[k])
18 |     k += 1
19 |     if k > len(nums): break
20 | 
21 |   return max_num
22 |   
23 | 
24 | """ typescript code i poorly translated to python:
25 | function maxValidWIndowSum(nums: number[], k: number): number {
26 |   const window = nums.slice(0, k);
27 |   let max = 0;
28 | 
29 |   do {
30 |     const isValid = window.filter((num) => num < 0).length === 1;
31 |     if (isValid) {
32 |         const sum = window.reduce((acc, curr) => acc + curr, 0);
33 |         max = Math.max(max, sum);
34 |     }
35 | 
36 |     window.splice(0, 1);
37 |     window.push(nums[k]);
38 |     k++;
39 |   } while (k <= nums.length);
40 | 
41 |   return max;
42 | } """
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |   window = nums[:k]
 3 |   max_num = 0
 4 | 
 5 |   while True:
 6 |     num_negatives = 0
 7 |     sum = 0
 8 |     for num in window:
 9 |       if num < 0: num_negatives += 1
10 |       if num_negatives > 1: break
11 |       sum += num
12 | 
13 |     if num_negatives > 1: break
14 |     max_num = max(sum, max_num)
15 | 
16 |     window.pop(0)
17 |     if k <= len(nums) - 1: window.append(nums[k])
18 |     k += 1
19 |     if k > len(nums): break
20 | 
21 |   return max_num
22 |   
23 | 
24 | """ typescript code i poorly translated to python:
25 | function maxValidWIndowSum(nums: number[], k: number): number {
26 |   const window = nums.slice(0, k);
27 |   let max = 0;
28 | 
29 |   do {
30 |     const isValid = window.filter((num) => num < 0).length === 1;
31 |     if (isValid) {:
32 |         const sum = window.reduce((acc, curr) => acc + curr, 0);
33 |         max = Math.max(max, sum);
34 |     }
35 | 
36 |     window.splice(0, 1);
37 |     window.push(nums[k]);
38 |     k++;
39 |   } while (k <= nums.length);
40 | 
41 |   return max;
42 | } """
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01132918

| Tag | Change |
|---|---|
| [syntax-only] | line 26: added missing colon |
| [syntax-only] | line 27: added missing colon |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -24,6 +24,6 @@
   let right = nums.length - 1;
 
-  while (left < right) {
-    if (nums[left] + nums[right] > T) {
+  while (left < right) {:
+    if (nums[left] + nums[right] > T) {:
         right--;
         continue;
```

</details>

**Raw extracted input:**

```
 1 | # note: example 1's output should totally be 5 instead of 4?
 2 | # since (2,4) should be a valid pair too
 3 | 
 4 | def count_pairs(nums, T):
 5 |   num_pairs = 0
 6 |   left = 0
 7 |   right = len(nums) - 1
 8 | 
 9 |   while left < right:
10 |     if nums[left] + nums[right] > T:
11 |       right -= 1
12 |       continue
13 | 
14 |     num_pairs += right - left
15 |     left += 1
16 | 
17 |   return num_pairs
18 | 
19 | """ typescript :D
20 | function countPairs(nums: number[], T: number): number {
21 |   let numPairs = 0;
22 | 
23 |   let left = 0;
24 |   let right = nums.length - 1;
25 | 
26 |   while (left < right) {
27 |     if (nums[left] + nums[right] > T) {
28 |         right--;
29 |         continue;
30 |     }
31 | 
32 |     numPairs += right - left;
33 |     left++;
34 |   }
35 | 
36 |   return numPairs;
37 | } """
```

**Fixed input:**

```
 1 | # note: example 1's output should totally be 5 instead of 4?
 2 | # since (2,4) should be a valid pair too
 3 | 
 4 | def count_pairs(nums, T):
 5 |   num_pairs = 0
 6 |   left = 0
 7 |   right = len(nums) - 1
 8 | 
 9 |   while left < right:
10 |     if nums[left] + nums[right] > T:
11 |       right -= 1
12 |       continue
13 | 
14 |     num_pairs += right - left
15 |     left += 1
16 | 
17 |   return num_pairs
18 | 
19 | """ typescript :D
20 | function countPairs(nums: number[], T: number): number {
21 |   let numPairs = 0;
22 | 
23 |   let left = 0;
24 |   let right = nums.length - 1;
25 | 
26 |   while (left < right) {:
27 |     if (nums[left] + nums[right] > T) {:
28 |         right--;
29 |         continue;
30 |     }
31 | 
32 |     numPairs += right - left;
33 |     left++;
34 |   }
35 | 
36 |   return numPairs;
37 | } """
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `java`
- **status:** `needs-manual-review`

**Raw bonus code:**

````
 1 | ```ts
 2 | // 3740. Minimum Distance Between Three Equal Elements I
 3 | // TypeScript solution
 4 | function minimumDistance(nums: number[]): number {
 5 |     const lastSeen = new Map<number, number[]>();
 6 |     let minDistance = Infinity;
 7 | 
 8 |     for (let i = 0; i < nums.length; i++) {
 9 |         const num = nums[i];
10 | 
11 |         if (!lastSeen.has(num)) {
12 |             lastSeen.set(num, [i]);
13 |             continue;
14 |         }
15 | 
16 |         const seen = lastSeen.get(num)! as [number, number];
17 |         if (seen.length !== 2) {
18 |             lastSeen.set(num, [seen[0], i]);
19 |             continue;
20 |         }
21 | 
22 |         const [j, k] = seen;
23 |         const distance = Math.abs(i - j) + Math.abs(j - k) + Math.abs(k - i);
24 |         minDistance = Math.min(distance, minDistance);
25 | 
26 |         lastSeen.set(num, [k, i]);
27 |     }
28 | 
29 |     return minDistance === Infinity ? -1 : minDistance;
30 | };
31 | ```
32 | 
33 | My solution has O(n) time complexity because it loops through `nums` once and O(n) space complexity because it uses a hashmap of all previously seen numbers. It works by going through `nums` and checking if it's been seen twice previously; if it hasn't, then store it in the hashmap. If it has, compute the distance of the 3 indices (the current and the 2 stored indices) and store that in `minDistance`. Then, replace the oldest index in the "previously seen" hashmap with the current index, since the furthest index can't possibly produce a smaller distance in the future.
````

## Score Summary

- **Problem 1:** 16.0/20  (20/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01142869 — Treyson Thelusma

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01142869

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |       l = 0
 3 |       r = 0
 4 |       window_sum = nums[0]
 5 |       max_valid = 0
 6 |       negatives = 1 if window_sum < 0 else 0
 7 |       for i in range(k - 1):
 8 |          r += 1
 9 |          window_sum += nums[r]
10 |          if nums[r] < 0:
11 |             negatives += 1
12 |       if negatives <= 1:
13 |          max_valid = max(max_valid, window_sum)
14 |       while r < len(nums) - 1:
15 |          if negatives <= 1:
16 |             max_valid = max(max_valid, window_sum)
17 |          r += 1
18 |          if nums[r] < 0:
19 |             negatives += 1
20 |          window_sum += nums[r]
21 |          if nums[l] < 0:
22 |             negatives -= 1
23 |          window_sum -= nums[l]
24 |          l += 1
25 |       return max_valid
26 |          
27 |      
28 |        
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |       l = 0
 3 |       r = 0
 4 |       window_sum = nums[0]
 5 |       max_valid = 0
 6 |       negatives = 1 if window_sum < 0 else 0
 7 |       for i in range(k - 1):
 8 |          r += 1
 9 |          window_sum += nums[r]
10 |          if nums[r] < 0:
11 |             negatives += 1
12 |       if negatives <= 1:
13 |          max_valid = max(max_valid, window_sum)
14 |       while r < len(nums) - 1:
15 |          if negatives <= 1:
16 |             max_valid = max(max_valid, window_sum)
17 |          r += 1
18 |          if nums[r] < 0:
19 |             negatives += 1
20 |          window_sum += nums[r]
21 |          if nums[l] < 0:
22 |             negatives -= 1
23 |          window_sum -= nums[l]
24 |          l += 1
25 |       return max_valid
26 |          
27 |      
28 |        
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01142869

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,13 +1,13 @@
 def count_pairs(nums, T):
-     l = 0
-     r = len(nums) - 1
-     valid_pairs = 0
+    l = 0
+    r = len(nums) - 1
+    valid_pairs = 0
 
-     while l < r:
-         if nums[l] + nums[r] <= T:
-               valid_pairs += (r - l)
-               l += 1
-         else:
-              r -= 1
+    while l < r:
+        if nums[l] + nums[r] <= T:
+            valid_pairs += (r - l)
+            l += 1
+        else:
+            r -= 1
 
-      return valid_pairs
+    return valid_pairs
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |      l = 0
 3 |      r = len(nums) - 1
 4 |      valid_pairs = 0
 5 | 
 6 |      while l < r:
 7 |          if nums[l] + nums[r] <= T:
 8 |                valid_pairs += (r - l)
 9 |                l += 1
10 |          else:
11 |               r -= 1
12 | 
13 |       return valid_pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     l = 0
 3 |     r = len(nums) - 1
 4 |     valid_pairs = 0
 5 | 
 6 |     while l < r:
 7 |         if nums[l] + nums[r] <= T:
 8 |             valid_pairs += (r - l)
 9 |             l += 1
10 |         else:
11 |             r -= 1
12 | 
13 |     return valid_pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
 3 |         for q in queries:
 4 |             idx = q[0]
 5 | 
 6 |             while idx <= q[1]:
 7 |                 nums[idx] = (nums[idx] * q[3]) % (10**9 + 7)
 8 |                 idx += q[2]
 9 | 
10 |         xor = 0
11 |         for num in nums:
12 |             xor = xor ^ num
13 | 
14 |         return xor
15 | 
16 | This problem gave me an explicit set of instructions, telling me "For each query, you must apply the following operations in order:
17 | 
18 | Set idx = li.
19 | While idx <= ri:
20 | Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
21 | Set idx += ki."
22 | 
23 | With this, the time complexity starts off at O(n * k) where n is the number of queries, and k is the largest value of a query's ri value. After this, the question tells me to return the bitwise XOR of all elements in nums after the queries. To do this, I initialize an xor variable with the value 0, since 0 XOR (any number) equals this number, for example 0000 (0 in 4 bit binary) ^ 1010 (4 in 4 bit binary) equals 1010 (4 in 4 bit binary), where the output has a 1 for each bit where it differs, 1 differs from 0, so each place with a 1 is preserved. Then, I loop through the nums array, and apply the XOR function to the previous value and the current number. Finally, I return the result, which I saved as variable "xor". The part of the solution that I wrote was O(j), where j is the length of the nums array, because we iterate through it once.
```

## Score Summary

- **Problem 1:** 12.8/20  (16/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01156268 — Max Stehura

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01156268

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     negative_count = 0
 3 |     for i in nums[:k]:
 4 |         if i < 0:
 5 |             negative_count += 1
 6 | 
 7 |     final_sum = None
 8 |     temp_sum = sum(nums[:k])
 9 |     
10 |     if negative_count <= 1:
11 |         final_sum = temp_sum
12 |             
13 |     for i in range(k, len(nums)):
14 |         temp_sum += nums[i]
15 |         if nums[i] < 0:
16 |             negative_count += 1
17 | 
18 |         temp_sum -= nums[i - k]
19 |         if nums[i - k] < 0:
20 |             negative_count -= 1
21 | 
22 |         if negative_count <= 1:
23 |             if final_sum is None or temp_sum > final_sum:
24 |                 final_sum = temp_sum
25 |                 return final_sum
26 | 
27 |     if final_sum == None:
28 |         print(f"There are no valid windows of size {k}.")
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     negative_count = 0
 3 |     for i in nums[:k]:
 4 |         if i < 0:
 5 |             negative_count += 1
 6 | 
 7 |     final_sum = None
 8 |     temp_sum = sum(nums[:k])
 9 |     
10 |     if negative_count <= 1:
11 |         final_sum = temp_sum
12 |             
13 |     for i in range(k, len(nums)):
14 |         temp_sum += nums[i]
15 |         if nums[i] < 0:
16 |             negative_count += 1
17 | 
18 |         temp_sum -= nums[i - k]
19 |         if nums[i - k] < 0:
20 |             negative_count -= 1
21 | 
22 |         if negative_count <= 1:
23 |             if final_sum is None or temp_sum > final_sum:
24 |                 final_sum = temp_sum
25 |                 return final_sum
26 | 
27 |     if final_sum == None:
28 |         print(f"There are no valid windows of size {k}.")
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01156268

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     i = 0
 3 |     j = len(nums) - 1
 4 |     pairs = 0
 5 | 
 6 |     while i < j:
 7 |         if nums[i] + nums[j] <= T:
 8 |             pairs += (j - i)
 9 |             i += 1
10 |         else:
11 |             j -= 1
12 | 
13 |     return pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     i = 0
 3 |     j = len(nums) - 1
 4 |     pairs = 0
 5 | 
 6 |     while i < j:
 7 |         if nums[i] + nums[j] <= T:
 8 |             pairs += (j - i)
 9 |             i += 1
10 |         else:
11 |             j -= 1
12 | 
13 |     return pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 4.8/20  (6/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01125201 — Kathryn Schauber

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01125201

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     cnt = 0
 3 |     negcnt = 0
 4 | 
 5 |     for i in range(k):
 6 |         if nums[i] < 0:
 7 |             negcnt += 1
 8 |     if negcnt <= 1:
 9 |         cnt += 1
10 | 
11 |     for i in range(1, len(nums) - k + 1):
12 |         if nums[i - 1] < 0:
13 |             negcnt -= 1
14 |         if nums[i + k - 1] < 0:
15 |             negcnt += 1
16 |         if negcnt <= 1:
17 |             cnt += 1
18 |     
19 |     return cnt
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     cnt = 0
 3 |     negcnt = 0
 4 | 
 5 |     for i in range(k):
 6 |         if nums[i] < 0:
 7 |             negcnt += 1
 8 |     if negcnt <= 1:
 9 |         cnt += 1
10 | 
11 |     for i in range(1, len(nums) - k + 1):
12 |         if nums[i - 1] < 0:
13 |             negcnt -= 1
14 |         if nums[i + k - 1] < 0:
15 |             negcnt += 1
16 |         if negcnt <= 1:
17 |             cnt += 1
18 |     
19 |     return cnt
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01125201

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | #for the first example shouldn't the output be 5 because 2 + 4 = 6 <= T?
 2 | 
 3 | def count_pairs(nums, T):
 4 |     cnt = 0
 5 |     i = 0
 6 |     j = len(nums) - 1
 7 | 
 8 |     while i < j:
 9 |         if nums[i] + nums[j] > T:
10 |             j -= 1
11 |         else:
12 |             cnt += j - i
13 |             i += 1
14 | 
15 |     return cnt
```

**Fixed input:**

```
 1 | #for the first example shouldn't the output be 5 because 2 + 4 = 6 <= T?
 2 | 
 3 | def count_pairs(nums, T):
 4 |     cnt = 0
 5 |     i = 0
 6 |     j = len(nums) - 1
 7 | 
 8 |     while i < j:
 9 |         if nums[i] + nums[j] > T:
10 |             j -= 1
11 |         else:
12 |             cnt += j - i
13 |             i += 1
14 | 
15 |     return cnt
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | #4/7, 2069. Walking Robot Simulation II (I chose a bad day to do this)
 2 | 
 3 | class Robot(object):
 4 | 
 5 |     def __init__(self, width, height):
 6 |         """
 7 |         :type width: int
 8 |         :type height: int
 9 |         """
10 | 
11 |         self.dir = "East"
12 |         self.pos = [0, 0]
13 |         self.width = width
14 |         self.height = height
15 |                 
16 |         
17 | 
18 |     def step(self, num):
19 |         """
20 |         :type num: int
21 |         :rtype: None
22 |         """
23 |         og = num
24 |         num = num % ((2 * (self.width - 1)) + (2 * (self.height - 1)))
25 |         if num == 0 and og > 0 and self.pos == [0, 0]:
26 |             self.dir = "South"
27 | 
28 |         while num > 0:
29 |             if self.dir == "East":
30 |                 new = self.pos[0] + num
31 |                 if new < self.width:
32 |                     self.pos = [new, 0]
33 |                     num = 0
34 |                 else:
35 |                     num -= self.width - 1 - self.pos[0]
36 |                     self.dir = "North"
37 |                     self.pos[0] = self.width - 1
38 | 
39 |             if self.dir == "North":
40 |                 new = self.pos[1] + num
41 |                 if new < self.height:
42 |                     self.pos = [self.width - 1, new]
43 |                     num = 0
44 |                 else:
45 |                     num -= self.height - 1 - self.pos[1]
46 |                     self.dir = "West"
47 |                     self.pos[1] = self.height - 1
48 |             
49 |             if self.dir == "West":
50 |                 new = self.pos[0] - num
51 |                 if new >= 0:
52 |                     self.pos = [new, self.height - 1]
53 |                     num = 0
54 |                 else:
55 |                     num -= self.pos[0]
56 |                     self.dir = "South"
57 |                     self.pos[0] = 0
58 | 
59 |             if self.dir == "South":
60 |                 new = self.pos[1] - num
61 |                 if new >= 0:
62 |                     self.pos = [0, new]
63 |                     num = 0
64 |                 else:
65 |                     num -= self.pos[1]
66 |                     self.dir = "East"
67 |                     self.pos[1] = 0
68 | 
69 | 
70 | 
71 |         
72 | 
73 |     def getPos(self):
74 |         """
75 |         :rtype: List[int]
76 |         """
77 |         return self.pos
78 |         
79 | 
80 |     def getDir(self):
81 |         """
82 |         :rtype: str
83 |         """
84 |         return self.dir
85 |         
86 | 
87 | 
88 | # Your Robot object will be instantiated and called as such:
89 | # obj = Robot(width, height)
90 | # obj.step(num)
91 | # param_2 = obj.getPos()
92 | # param_3 = obj.getDir()
93 | 
94 | 
95 | The time complexity of the problem is constant time O(1). even though there is a while loop, it will only execute a maximum of 2 time. This is because the line num = num % ((2 * (self.width - 1)) + (2 * (self.height - 1))) reduces the amount of steps to be within the perimeter and the while loop will always iterate if the robot doesn't end up in the same position and when the robot changes direction from south to east. The body of the while loop are all if statements, which have constant time, and since the while loop will always iterate 0-2 times independent of the value of num, the complexity of the step function is constant. This works because the code calculates it where the amount of steps to get to the correct position is minimized keeping the robot moving in its general path. if the robot goes out of bounds the direction is changed and the amount of steps taken until it hit the edge is subtracted from the number of steps left. the if statements are simply if statements and in the order the robot will walk them in so if the robot changes direction the code moves right on to the next if statement and loops back to the beginning when changing from south to east.
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01074478 — Elaine Zou

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01074478

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |    p1, p2, res = 0, k-1, 0
 3 |    tempSum = sum(nums[:k])
 4 |    for x in nums[p1:p2+1] :
 5 |       if x < 0:
 6 |          numNeg += 1
 7 |    while p2 < len(nums) :
 8 |       if numNeg < 2:
 9 |          res = max(res, tempSum)
10 |       if nums[p1] < 0:
11 |          numNeg -= 1
12 |       tempSum -= nums[p1]
13 |       if nums[p2+1] < 0:
14 |          numNeg += 1
15 |       tempSum += nums[p2+1]
16 |       p1, p2 = p1 + 1, p2 + 1
17 |    return res
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |    p1, p2, res = 0, k-1, 0
 3 |    tempSum = sum(nums[:k])
 4 |    for x in nums[p1:p2+1] :
 5 |       if x < 0:
 6 |          numNeg += 1
 7 |    while p2 < len(nums) :
 8 |       if numNeg < 2:
 9 |          res = max(res, tempSum)
10 |       if nums[p1] < 0:
11 |          numNeg -= 1
12 |       tempSum -= nums[p1]
13 |       if nums[p2+1] < 0:
14 |          numNeg += 1
15 |       tempSum += nums[p2+1]
16 |       p1, p2 = p1 + 1, p2 + 1
17 |    return res
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01074478

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
1 | def count_pairs(nums, T):
2 |    p1, p2, res = 0, len(nums) - 1, 0
3 |    while p1 < p2:
4 |       if nums[p1] + nums[p2] > T :
5 |          p2 -= 1
6 |       else:
7 |          res += p2 - p1
8 |          p1 += 1
9 |    return res
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |    p1, p2, res = 0, len(nums) - 1, 0
3 |    while p1 < p2:
4 |       if nums[p1] + nums[p2] > T :
5 |          p2 -= 1
6 |       else:
7 |          res += p2 - p1
8 |          p1 += 1
9 |    return res
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01121801 — Lilia Diusheyeva

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01121801

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,33 +1,33 @@
 def max_valid_window_sum(nums, k):
-       
-       #initialize the sum and count
-       window_sum = 0
-       max_sum = 0
-       negative_count = 0
-     
-       #set up first window
-       for i in range(k):
-             window_sum += nums[i]
-             if nums[i] < 0:
-                         negative_count += 1
-        
-       if negative_count <=1:
-             max_sum = window_sum
 
-       #set up slide window
-       for i in range(k, len(nums)):
-             #add the new element
-             window_sum += nums[i] 
-             if nums[i] < 0:
-                           negative_count += 1
+    #initialize the sum and count
+    window_sum = 0
+    max_sum = 0
+    negative_count = 0
 
-             #remove the old element
-             window_sum -= nums[i - k] 
-             if nums[i - k] < 0:
-                           negative_count -= 1
+    #set up first window
+    for i in range(k):
+        window_sum += nums[i]
+        if nums[i] < 0:
+            negative_count += 1
 
-              #check if the window is valid
-              if negative_count <=1:
-                           max_sum = max(max_sum, window_sum)
+    if negative_count <=1:
+        max_sum = window_sum
 
-        return max_sum
+    #set up slide window
+    for i in range(k, len(nums)):
+        #add the new element
+        window_sum += nums[i]
+        if nums[i] < 0:
+            negative_count += 1
+
+        #remove the old element
+        window_sum -= nums[i - k]
+        if nums[i - k] < 0:
+            negative_count -= 1
+
+        #check if the window is valid
+        if negative_count <=1:
+            max_sum = max(max_sum, window_sum)
+
+    return max_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |        
 3 |        #initialize the sum and count
 4 |        window_sum = 0
 5 |        max_sum = 0
 6 |        negative_count = 0
 7 |      
 8 |        #set up first window
 9 |        for i in range(k):
10 |              window_sum += nums[i]
11 |              if nums[i] < 0:
12 |                          negative_count += 1
13 |         
14 |        if negative_count <=1:
15 |              max_sum = window_sum
16 | 
17 |        #set up slide window
18 |        for i in range(k, len(nums)):
19 |              #add the new element
20 |              window_sum += nums[i] 
21 |              if nums[i] < 0:
22 |                            negative_count += 1
23 | 
24 |              #remove the old element
25 |              window_sum -= nums[i - k] 
26 |              if nums[i - k] < 0:
27 |                            negative_count -= 1
28 | 
29 |               #check if the window is valid
30 |               if negative_count <=1:
31 |                            max_sum = max(max_sum, window_sum)
32 | 
33 |         return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 
 3 |     #initialize the sum and count
 4 |     window_sum = 0
 5 |     max_sum = 0
 6 |     negative_count = 0
 7 | 
 8 |     #set up first window
 9 |     for i in range(k):
10 |         window_sum += nums[i]
11 |         if nums[i] < 0:
12 |             negative_count += 1
13 | 
14 |     if negative_count <=1:
15 |         max_sum = window_sum
16 | 
17 |     #set up slide window
18 |     for i in range(k, len(nums)):
19 |         #add the new element
20 |         window_sum += nums[i]
21 |         if nums[i] < 0:
22 |             negative_count += 1
23 | 
24 |         #remove the old element
25 |         window_sum -= nums[i - k]
26 |         if nums[i - k] < 0:
27 |             negative_count -= 1
28 | 
29 |         #check if the window is valid
30 |         if negative_count <=1:
31 |             max_sum = max(max_sum, window_sum)
32 | 
33 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01121801

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,15 +1,15 @@
 def count_pairs(nums, T):
-       
-       #set up left/right and initialize count
-       left = 0
-       right = len(nums - 1)
-       count = 0
 
-       while left < right:
-                 if (nums[left] + nums[right]) <=T:
-                          count += (right - left)
-                          left += 1
-                 else:
-                          right -= 1
+    #set up left/right and initialize count
+    left = 0
+    right = len(nums - 1)
+    count = 0
 
-        return count
+    while left < right:
+        if (nums[left] + nums[right]) <=T:
+            count += (right - left)
+            left += 1
+        else:
+            right -= 1
+
+    return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |        
 3 |        #set up left/right and initialize count
 4 |        left = 0
 5 |        right = len(nums - 1)
 6 |        count = 0
 7 | 
 8 |        while left < right:
 9 |                  if (nums[left] + nums[right]) <=T:
10 |                           count += (right - left)
11 |                           left += 1
12 |                  else:
13 |                           right -= 1
14 | 
15 |         return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 | 
 3 |     #set up left/right and initialize count
 4 |     left = 0
 5 |     right = len(nums - 1)
 6 |     count = 0
 7 | 
 8 |     while left < right:
 9 |         if (nums[left] + nums[right]) <=T:
10 |             count += (right - left)
11 |             left += 1
12 |         else:
13 |             right -= 1
14 | 
15 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 0.0/20  (0/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01126541 — Cheong Ting Eland Chan

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 2

**Diff:**

# Diff for B01126541

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     curr_sum = 0
 3 |     max_sum = -1 * math.inf
 4 |     num_neg = 0
 5 | 
 6 |     
 7 |     for i, num in enumerate(nums):
 8 |         curr_sum += num 
 9 | 
10 |         if num < 0:
11 |             num_neg += 1
12 | 
13 |         if i >= k - 1:
14 |             if num_neg == 1:
15 |                 print("i = " + str(i) + " sum = " + str(curr_sum))
16 |                 max_sum = max(max_sum, curr_sum)
17 | 
18 |             curr_sum -= nums[i - k + 1]
19 | 
20 |             if nums[i - k + 1] < 0:
21 |                 num_neg -= 1
22 | 
23 | 
24 |     if max_sum == -1 * math.inf:
25 |         max_sum = 0
26 |     
27 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     curr_sum = 0
 3 |     max_sum = -1 * math.inf
 4 |     num_neg = 0
 5 | 
 6 |     
 7 |     for i, num in enumerate(nums):
 8 |         curr_sum += num 
 9 | 
10 |         if num < 0:
11 |             num_neg += 1
12 | 
13 |         if i >= k - 1:
14 |             if num_neg == 1:
15 |                 print("i = " + str(i) + " sum = " + str(curr_sum))
16 |                 max_sum = max(max_sum, curr_sum)
17 | 
18 |             curr_sum -= nums[i - k + 1]
19 | 
20 |             if nums[i - k + 1] < 0:
21 |                 num_neg -= 1
22 | 
23 | 
24 |     if max_sum == -1 * math.inf:
25 |         max_sum = 0
26 |     
27 |     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 2

**Diff:**

# Diff for B01126541

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     num_pairs = 0
 3 |     i =  0
 4 |     j = len(nums) - 1
 5 | 
 6 |     while i < j: 
 7 |         sum = nums[i] + nums[j]
 8 |         if sum <= T:
 9 |             num_pairs += j - i
10 |             i += 1
11 |         else:
12 |             j -= 1
13 | 
14 |     return num_pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     num_pairs = 0
 3 |     i =  0
 4 |     j = len(nums) - 1
 5 | 
 6 |     while i < j: 
 7 |         sum = nums[i] + nums[j]
 8 |         if sum <= T:
 9 |             num_pairs += j - i
10 |             i += 1
11 |         else:
12 |             j -= 1
13 | 
14 |     return num_pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `pseudocode`
- **status:** `pseudocode`

**Raw bonus code:**

```
1 | The time complexity is O(n) because I used only a single loop. I just iterate through the array and record the three most recent indices at which the element appears in the list using the hash table. When the list length reached 3, I calculated the distance and compared it with the existing minimum distance. All of the above are constant-time operations. 
```

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01138859 — Sean Carhart

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01138859

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,3 +1,4 @@
-public static int maxValidWindowSum(int[] nums, int k) 
+public class Solution {
+public static int maxValidWindowSum(int[] nums, int k)
     {
         boolean first = true;
@@ -49,5 +50,6 @@
         {
             ans = Math.max(ans,sum);
-        } 
+        }
         return ans;
     }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) 
 2 |     {
 3 |         boolean first = true;
 4 |         int sum = 0;
 5 |         int ans = 0;
 6 |         int numNeg = 0;
 7 |         int left = 0;
 8 |         int right = 0;
 9 |         while (right < nums.length)
10 |         {
11 |             if (right - left < k)
12 |             {
13 |                 if (nums[right] < 0)
14 |                 {
15 |                     numNeg++;
16 |                 }
17 |                 sum += nums[right];
18 |                 right++;
19 |             }
20 |             else
21 |             {
22 |                 if (numNeg <= 1)
23 |                 {
24 |                     if (first)
25 |                     {
26 |                         ans = sum;
27 |                     }
28 |                     else
29 |                     {
30 |                         ans = Math.max(ans,sum);
31 |                     }
32 |                     first = false;
33 |                 }
34 |                 if (nums[left] < 0)
35 |                 {
36 |                     numNeg--;
37 |                 }
38 |                 if (nums[right] < 0)
39 |                 {
40 |                     numNeg++;
41 |                 }
42 |                 sum -= nums[left];
43 |                 sum += nums[right];
44 |                 left++;
45 |                 right++;
46 |             }
47 |         }
48 |         if (numNeg <= 1)
49 |         {
50 |             ans = Math.max(ans,sum);
51 |         } 
52 |         return ans;
53 |     }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int maxValidWindowSum(int[] nums, int k)
 3 |     {
 4 |         boolean first = true;
 5 |         int sum = 0;
 6 |         int ans = 0;
 7 |         int numNeg = 0;
 8 |         int left = 0;
 9 |         int right = 0;
10 |         while (right < nums.length)
11 |         {
12 |             if (right - left < k)
13 |             {
14 |                 if (nums[right] < 0)
15 |                 {
16 |                     numNeg++;
17 |                 }
18 |                 sum += nums[right];
19 |                 right++;
20 |             }
21 |             else
22 |             {
23 |                 if (numNeg <= 1)
24 |                 {
25 |                     if (first)
26 |                     {
27 |                         ans = sum;
28 |                     }
29 |                     else
30 |                     {
31 |                         ans = Math.max(ans,sum);
32 |                     }
33 |                     first = false;
34 |                 }
35 |                 if (nums[left] < 0)
36 |                 {
37 |                     numNeg--;
38 |                 }
39 |                 if (nums[right] < 0)
40 |                 {
41 |                     numNeg++;
42 |                 }
43 |                 sum -= nums[left];
44 |                 sum += nums[right];
45 |                 left++;
46 |                 right++;
47 |             }
48 |         }
49 |         if (numNeg <= 1)
50 |         {
51 |             ans = Math.max(ans,sum);
52 |         }
53 |         return ans;
54 |     }
55 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01138859

| Tag | Change |
|---|---|
| [ambiguous] | wrapped code in method signature `countPairs(int[] nums, int T)` |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,3 +1,5 @@
-public static int maxValidWindowSum(int[] nums, int k) 
+public class Solution {
+    public static int countPairs(int[] nums, int T) {
+public static int maxValidWindowSum(int[] nums, int k)
     {
         boolean first = true;
@@ -56,5 +58,7 @@
                 ans = Math.max(ans,sum);
             }
-        } 
+        }
         return ans;
     }
+    }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) 
 2 |     {
 3 |         boolean first = true;
 4 |         int sum = 0;
 5 |         int ans = 0;
 6 |         int numNeg = 0;
 7 |         int left = 0;
 8 |         int right = 0;
 9 |         while (right < nums.length)
10 |         {
11 |             if (right - left < k)
12 |             {
13 |                 if (nums[right] < 0)
14 |                 {
15 |                     numNeg++;
16 |                 }
17 |                 sum += nums[right];
18 |                 right++;
19 |             }
20 |             else
21 |             {
22 |                 if (numNeg <= 1)
23 |                 {
24 |                     if (first)
25 |                     {
26 |                         ans = sum;
27 |                     }
28 |                     else
29 |                     {
30 |                         ans = Math.max(ans,sum);
31 |                     }
32 |                     first = false;
33 |                 }
34 |                 if (nums[left] < 0)
35 |                 {
36 |                     numNeg--;
37 |                 }
38 |                 if (nums[right] < 0)
39 |                 {
40 |                     numNeg++;
41 |                 }
42 |                 sum -= nums[left];
43 |                 sum += nums[right];
44 |                 left++;
45 |                 right++;
46 |             }
47 |         }
48 |         if (numNeg <= 1)
49 |         {
50 |             if (first)
51 |             {
52 |                 ans = sum;
53 |             }
54 |             else
55 |             {
56 |                 ans = Math.max(ans,sum);
57 |             }
58 |         } 
59 |         return ans;
60 |     }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 |     public static int countPairs(int[] nums, int T) {
 3 | public static int maxValidWindowSum(int[] nums, int k)
 4 |     {
 5 |         boolean first = true;
 6 |         int sum = 0;
 7 |         int ans = 0;
 8 |         int numNeg = 0;
 9 |         int left = 0;
10 |         int right = 0;
11 |         while (right < nums.length)
12 |         {
13 |             if (right - left < k)
14 |             {
15 |                 if (nums[right] < 0)
16 |                 {
17 |                     numNeg++;
18 |                 }
19 |                 sum += nums[right];
20 |                 right++;
21 |             }
22 |             else
23 |             {
24 |                 if (numNeg <= 1)
25 |                 {
26 |                     if (first)
27 |                     {
28 |                         ans = sum;
29 |                     }
30 |                     else
31 |                     {
32 |                         ans = Math.max(ans,sum);
33 |                     }
34 |                     first = false;
35 |                 }
36 |                 if (nums[left] < 0)
37 |                 {
38 |                     numNeg--;
39 |                 }
40 |                 if (nums[right] < 0)
41 |                 {
42 |                     numNeg++;
43 |                 }
44 |                 sum -= nums[left];
45 |                 sum += nums[right];
46 |                 left++;
47 |                 right++;
48 |             }
49 |         }
50 |         if (numNeg <= 1)
51 |         {
52 |             if (first)
53 |             {
54 |                 ans = sum;
55 |             }
56 |             else
57 |             {
58 |                 ans = Math.max(ans,sum);
59 |             }
60 |         }
61 |         return ans;
62 |     }
63 |     }
64 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 19.2/20  (24/25 tests passed)
- **Problem 2:** 0/20  (0/0 tests passed)  — load error: compile error: C:\Users\danz3\AppData\Local\Temp\jgrade_B01138859_cyf0qtzk\Solution.java:3: error: illegal start of expr
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01043907 — Samuel Halsband

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01043907

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -6,18 +6,17 @@
     numNegative = 0
     for i in range(0,k): #initial check to get value of numNegative for first window
-         currentSum += nums[i]
-         if nums[i] < 0:
-              numNegative +=1
-   while r < len(nums):
-         if numNegative <=1:
-                 maxSum = max(maxSum, currentSum)
-         if nums[l] <0:
-              numNegative -=1
+        currentSum += nums[i]
+        if nums[i] < 0:
+            numNegative +=1
+    while r < len(nums):
+        if numNegative <=1:
+                maxSum = max(maxSum, currentSum)
+        if nums[l] <0:
+            numNegative -=1
         if r < len(nums)-1: #edge case for when r is at the end of the array to avoid out of bounds error
-              if nums[r+1] <0:
-                   numNegative +=1
-              currentSum = currentSum - nums[l] + nums[r+1]
-         l+=1
-         r+=1
+            if nums[r+1] <0:
+                numNegative +=1
+            currentSum = currentSum - nums[l] + nums[r+1]
+        l+=1
+        r+=1
     return maxSum
-         
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     l = 0
 3 |     r = k - 1
 4 |     currentSum = 0
 5 |     maxSum = 0
 6 |     numNegative = 0
 7 |     for i in range(0,k): #initial check to get value of numNegative for first window
 8 |          currentSum += nums[i]
 9 |          if nums[i] < 0:
10 |               numNegative +=1
11 |    while r < len(nums):
12 |          if numNegative <=1:
13 |                  maxSum = max(maxSum, currentSum)
14 |          if nums[l] <0:
15 |               numNegative -=1
16 |         if r < len(nums)-1: #edge case for when r is at the end of the array to avoid out of bounds error
17 |               if nums[r+1] <0:
18 |                    numNegative +=1
19 |               currentSum = currentSum - nums[l] + nums[r+1]
20 |          l+=1
21 |          r+=1
22 |     return maxSum
23 |          
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     l = 0
 3 |     r = k - 1
 4 |     currentSum = 0
 5 |     maxSum = 0
 6 |     numNegative = 0
 7 |     for i in range(0,k): #initial check to get value of numNegative for first window
 8 |         currentSum += nums[i]
 9 |         if nums[i] < 0:
10 |             numNegative +=1
11 |     while r < len(nums):
12 |         if numNegative <=1:
13 |                 maxSum = max(maxSum, currentSum)
14 |         if nums[l] <0:
15 |             numNegative -=1
16 |         if r < len(nums)-1: #edge case for when r is at the end of the array to avoid out of bounds error
17 |             if nums[r+1] <0:
18 |                 numNegative +=1
19 |             currentSum = currentSum - nums[l] + nums[r+1]
20 |         l+=1
21 |         r+=1
22 |     return maxSum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01043907

| Tag | Change |
|---|---|
| [syntax-only] | line 1: added missing colon |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,3 +1,3 @@
-def count_pairs(nums, T)
+def count_pairs(nums, T):
     l = 0
     r = 1
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T)
 2 |     l = 0
 3 |     r = 1
 4 |     numPairs = 0
 5 |     while l < len(nums):
 6 |         if nums[l] + nums[r] <= T:
 7 |             numPairs +=1
 8 |             r +=1
 9 |             if r == len(nums):
10 |                  l = l + 1
11 |                  r = l+1
12 |         else:
13 |            l+=1
14 |            r+=1
15 |            
16 |            
17 |  
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     l = 0
 3 |     r = 1
 4 |     numPairs = 0
 5 |     while l < len(nums):
 6 |         if nums[l] + nums[r] <= T:
 7 |             numPairs +=1
 8 |             r +=1
 9 |             if r == len(nums):
10 |                  l = l + 1
11 |                  r = l+1
12 |         else:
13 |            l+=1
14 |            r+=1
15 |            
16 |            
17 |  
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 0.0/20  (0/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01111528 — Ian Porto

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01111528

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -5,3 +5,3 @@
                max = sum(nums[i:k])
     return max
-	
+    
```

</details>

**Raw extracted input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     max = 0
3 |     for i in range(len(nums)-k):
4 |          if sum(nums[i:k]) > max:
5 |                max = sum(nums[i:k])
6 |     return max
7 | 	
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     max = 0
3 |     for i in range(len(nums)-k):
4 |          if sum(nums[i:k]) > max:
5 |                max = sum(nums[i:k])
6 |     return max
7 |     
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `empty`
- **status:** `empty`
- **attempt #:** 1

**Diff:**

_(no diff file)_

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(empty)_

</details>

**Raw extracted input:**

_(empty)_

**Fixed input:**

_(empty)_

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 6.4/20  (8/25 tests passed)
- **Problem 2:** no results
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01123621 — Maddie Broderick

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01123621

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |      max = 0
 3 |      current = 0
 4 |      neg = 0
 5 |      valid = False
 6 |      for i in range(k):
 7 |           current += nums[i]
 8 |           if nums[i] < 0:
 9 |                neg += 1
10 |      if neg == 1:
11 |           max_sum += current
12 |           valid = True
13 |      for i in range(k, len(nums)):
14 |           if nums[i] < 0:
15 |                neg += 1
16 |           current += nums[i]
17 |           if nums[i-k] < 0:
18 |                neg -= 1
19 |           current -= nums[i-k]
20 |           if neg == 1:
21 |                if current >= max_sum:
22 |                     max_sum = current
23 |                valid = True
24 |      if valid:
25 |           return max_sum
26 |      return 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |      max = 0
 3 |      current = 0
 4 |      neg = 0
 5 |      valid = False
 6 |      for i in range(k):
 7 |           current += nums[i]
 8 |           if nums[i] < 0:
 9 |                neg += 1
10 |      if neg == 1:
11 |           max_sum += current
12 |           valid = True
13 |      for i in range(k, len(nums)):
14 |           if nums[i] < 0:
15 |                neg += 1
16 |           current += nums[i]
17 |           if nums[i-k] < 0:
18 |                neg -= 1
19 |           current -= nums[i-k]
20 |           if neg == 1:
21 |                if current >= max_sum:
22 |                     max_sum = current
23 |                valid = True
24 |      if valid:
25 |           return max_sum
26 |      return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01123621

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |      left = 0
 3 |      right = len(nums)-1
 4 |      num_pairs = 0
 5 |      while left < right:
 6 |           if nums[left] + nums[right] <= T:
 7 |                nums_pairs += (right - left)
 8 |                left += 1
 9 |           else:
10 |                right -= 1
11 |      return num_pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |      left = 0
 3 |      right = len(nums)-1
 4 |      num_pairs = 0
 5 |      while left < right:
 6 |           if nums[left] + nums[right] <= T:
 7 |                nums_pairs += (right - left)
 8 |                left += 1
 9 |           else:
10 |                right -= 1
11 |      return num_pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 2.4/20  (3/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01019743 — Juan Moran

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01019743

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | converted `//` line comments to `#` (2 lines) |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,17 +1,17 @@
 def max_valid_window_sum(nums, k):
-	# Paste this into your answer if you want to use python
-     max_sum = 0
-     valid = 0
-     for i in range(len(nums) - k + 1):  // iterate through possible windows
-          window_sum = 0
-          neg_count = 0
-          for j in range(j+k): // check each value in the window
-              window_sum += nums[j]
-              if nums[i] < 0:
-                   neg_count += 1
-           if neg_count <= 1:
-               max_sum = max(max_sum, window_sum)
-           return max_sum
-  
+    # Paste this into your answer if you want to use python
+    max_sum = 0
+    valid = 0
+    for i in range(len(nums) - k + 1):  #  iterate through possible windows
+        window_sum = 0
+        neg_count = 0
+        for j in range(j+k): #  check each value in the window
+            window_sum += nums[j]
+            if nums[i] < 0:
+                neg_count += 1
+        if neg_count <= 1:
+            max_sum = max(max_sum, window_sum)
+        return max_sum
 
 
+
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 	# Paste this into your answer if you want to use python
 3 |      max_sum = 0
 4 |      valid = 0
 5 |      for i in range(len(nums) - k + 1):  // iterate through possible windows
 6 |           window_sum = 0
 7 |           neg_count = 0
 8 |           for j in range(j+k): // check each value in the window
 9 |               window_sum += nums[j]
10 |               if nums[i] < 0:
11 |                    neg_count += 1
12 |            if neg_count <= 1:
13 |                max_sum = max(max_sum, window_sum)
14 |            return max_sum
15 |   
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     # Paste this into your answer if you want to use python
 3 |     max_sum = 0
 4 |     valid = 0
 5 |     for i in range(len(nums) - k + 1):  #  iterate through possible windows
 6 |         window_sum = 0
 7 |         neg_count = 0
 8 |         for j in range(j+k): #  check each value in the window
 9 |             window_sum += nums[j]
10 |             if nums[i] < 0:
11 |                 neg_count += 1
12 |         if neg_count <= 1:
13 |             max_sum = max(max_sum, window_sum)
14 |         return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01019743

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | converted `//` line comments to `#` (3 lines) |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,12 +1,12 @@
 def count_pairs(nums, T):
-	# Paste this into your answer if you want to use Python
+    # Paste this into your answer if you want to use Python
         left = 0
         right = len(nums) - 1
         total_pairs = 0
         while left < right:
-              if nums[left] + nums[right] <= T:
-                      total_pairs = right - left // updates with pointers
-                      left += 1 // shift left
-              else:
-                      right+=1 // shift right if not
-          return total_pairs
+            if nums[left] + nums[right] <= T:
+                total_pairs = right - left #  updates with pointers
+                left += 1 #  shift left
+            else:
+                right+=1 #  shift right if not
+        return total_pairs
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 	# Paste this into your answer if you want to use Python
 3 |         left = 0
 4 |         right = len(nums) - 1
 5 |         total_pairs = 0
 6 |         while left < right:
 7 |               if nums[left] + nums[right] <= T:
 8 |                       total_pairs = right - left // updates with pointers
 9 |                       left += 1 // shift left
10 |               else:
11 |                       right+=1 // shift right if not
12 |           return total_pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     # Paste this into your answer if you want to use Python
 3 |         left = 0
 4 |         right = len(nums) - 1
 5 |         total_pairs = 0
 6 |         while left < right:
 7 |             if nums[left] + nums[right] <= T:
 8 |                 total_pairs = right - left #  updates with pointers
 9 |                 left += 1 #  shift left
10 |             else:
11 |                 right+=1 #  shift right if not
12 |         return total_pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 1.82/20  (2/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01075554 — Alison Batz

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `pseudocode`
- **status:** `pseudocode`
- **attempt #:** 1

**Diff:**

_(no diff file)_

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,18 +0,0 @@
-Initialize all variables / pointers
-maxVar, result, negCount = 0 
-l = 0, r = k -1 
-
-Check validity of window
-
-if len(array) % k, it is valid
-else return 0 
-
-While r is less than the len of array
- check for more than one neg num in the valid window (updating negCount)
-   if there is more than 1 neg num in the window, return 0
-
-else add up all the elements in the num, save in result 
-
-if maxVar < result, update maxVar
-
-Out of the loop, return maxVar 
```

</details>

**Raw extracted input:**

```
 1 | Initialize all variables / pointers
 2 | maxVar, result, negCount = 0 
 3 | l = 0, r = k -1 
 4 | 
 5 | Check validity of window
 6 | 
 7 | if len(array) % k, it is valid
 8 | else return 0 
 9 | 
10 | While r is less than the len of array
11 |  check for more than one neg num in the valid window (updating negCount)
12 |    if there is more than 1 neg num in the window, return 0
13 | 
14 | else add up all the elements in the num, save in result 
15 | 
16 | if maxVar < result, update maxVar
17 | 
18 | Out of the loop, return maxVar 
```

**Fixed input:**

_(empty)_

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `pseudocode`
- **status:** `pseudocode`
- **attempt #:** 1

**Diff:**

_(no diff file)_

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,11 +0,0 @@
-Initialize all vars / pointers 
-n = len(nums), l = 0, r = n -1, count = 0
-
-while l is less than r
- using an if statement check to see if nums[l] + nums[r] <= T
-   if true -> increment count to r - 1and left ++
-   else decrement right by 1
-
-Out of loop, return count
-
- 
```

</details>

**Raw extracted input:**

```
 1 | Initialize all vars / pointers 
 2 | n = len(nums), l = 0, r = n -1, count = 0
 3 | 
 4 | while l is less than r
 5 |  using an if statement check to see if nums[l] + nums[r] <= T
 6 |    if true -> increment count to r - 1and left ++
 7 |    else decrement right by 1
 8 | 
 9 | Out of loop, return count
10 | 
11 |  
```

**Fixed input:**

_(empty)_

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** no results
- **Problem 2:** no results
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01055680 — William Conroy

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01055680

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,8 +1,9 @@
+public class Solution {
 public static int maxValidWindowSum(int[] nums, int k) {
     int windowSum = 0;
     int negativeCount = 0;
     int maxSum = Integer.MIN_VALUE;
-   
-   
+
+
     for (int i = 0; i < k; i++) {
         windowSum += nums[i];
@@ -30,7 +31,6 @@
     }
 
-   
+
     return maxSum == Integer.MIN_VALUE ? 0 : maxSum;
 }
-
-
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) {
 2 |     int windowSum = 0;
 3 |     int negativeCount = 0;
 4 |     int maxSum = Integer.MIN_VALUE;
 5 |    
 6 |    
 7 |     for (int i = 0; i < k; i++) {
 8 |         windowSum += nums[i];
 9 |         if (nums[i] < 0) {
10 |             negativeCount++;
11 |         }
12 |     }
13 | 
14 |     if (negativeCount <= 1) {
15 |         maxSum = windowSum;
16 |     }
17 | 
18 |     for (int i = k; i < nums.length; i++) {
19 |         if (nums[i - k] < 0) {
20 |             negativeCount--;
21 |         }
22 |         windowSum -= nums[i - k];
23 |         windowSum += nums[i];
24 |         if (nums[i] < 0) {
25 |             negativeCount++;
26 |         }
27 |         if (negativeCount <= 1) {
28 |             maxSum = Math.max(maxSum, windowSum);
29 |         }
30 |     }
31 | 
32 |    
33 |     return maxSum == Integer.MIN_VALUE ? 0 : maxSum;
34 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int maxValidWindowSum(int[] nums, int k) {
 3 |     int windowSum = 0;
 4 |     int negativeCount = 0;
 5 |     int maxSum = Integer.MIN_VALUE;
 6 | 
 7 | 
 8 |     for (int i = 0; i < k; i++) {
 9 |         windowSum += nums[i];
10 |         if (nums[i] < 0) {
11 |             negativeCount++;
12 |         }
13 |     }
14 | 
15 |     if (negativeCount <= 1) {
16 |         maxSum = windowSum;
17 |     }
18 | 
19 |     for (int i = k; i < nums.length; i++) {
20 |         if (nums[i - k] < 0) {
21 |             negativeCount--;
22 |         }
23 |         windowSum -= nums[i - k];
24 |         windowSum += nums[i];
25 |         if (nums[i] < 0) {
26 |             negativeCount++;
27 |         }
28 |         if (negativeCount <= 1) {
29 |             maxSum = Math.max(maxSum, windowSum);
30 |         }
31 |     }
32 | 
33 | 
34 |     return maxSum == Integer.MIN_VALUE ? 0 : maxSum;
35 | }
36 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01055680

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
     int left = 0;
@@ -7,5 +8,5 @@
         if (nums[left] + nums[right] <= T) {
             count += (right - left);
-            left++;  
+            left++;
         } else {
             right--;
@@ -14,3 +15,3 @@
     return count;
 }
-
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 |     int left = 0;
 3 |     int right = nums.length - 1;
 4 |     int count = 0;
 5 | 
 6 |     while (left < right) {
 7 |         if (nums[left] + nums[right] <= T) {
 8 |             count += (right - left);
 9 |             left++;  
10 |         } else {
11 |             right--;
12 |         }
13 |     }
14 |     return count;
15 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 |     int left = 0;
 4 |     int right = nums.length - 1;
 5 |     int count = 0;
 6 | 
 7 |     while (left < right) {
 8 |         if (nums[left] + nums[right] <= T) {
 9 |             count += (right - left);
10 |             left++;
11 |         } else {
12 |             right--;
13 |         }
14 |     }
15 |     return count;
16 | }
17 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01095016 — Jiarong Zhang

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01095016

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int maxValidWindowSum(int[] nums, int k) {
      int max = 0;
@@ -22,2 +23,3 @@
      return max;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) {
 2 |      int max = 0;
 3 |      int numNegatives = 0;
 4 |      int curr = 0;
 5 |      for(int i = 0; i<k; i++){
 6 |            if(nums[i] < 0){
 7 |                 numNegatives++;
 8 |            }
 9 |            curr += nums[i];
10 |      }
11 |      if(numNegatives > 0){max = curr;}
12 |      for(int i = 1; i<nums.length-k; i++){
13 |            curr = curr + nums[i+k-1] - nums[i-1];
14 |            if(nums[i-1] < 0){
15 |                  numNegatives--;
16 |            }
17 |            if(nums[i+k] < 0){
18 |                  numNegatives++;
19 |            }
20 |            max = numNegatives > 0 ? Math.max(curr, max) : max;
21 |      }
22 |      return max;
23 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int maxValidWindowSum(int[] nums, int k) {
 3 |      int max = 0;
 4 |      int numNegatives = 0;
 5 |      int curr = 0;
 6 |      for(int i = 0; i<k; i++){
 7 |            if(nums[i] < 0){
 8 |                 numNegatives++;
 9 |            }
10 |            curr += nums[i];
11 |      }
12 |      if(numNegatives > 0){max = curr;}
13 |      for(int i = 1; i<nums.length-k; i++){
14 |            curr = curr + nums[i+k-1] - nums[i-1];
15 |            if(nums[i-1] < 0){
16 |                  numNegatives--;
17 |            }
18 |            if(nums[i+k] < 0){
19 |                  numNegatives++;
20 |            }
21 |            max = numNegatives > 0 ? Math.max(curr, max) : max;
22 |      }
23 |      return max;
24 | }
25 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01095016

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
     int count = 0;
@@ -13,2 +14,3 @@
     return count;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 |     int count = 0;
 3 |     int l = 0;
 4 |     int r = nums.length-1;
 5 |     while(l < r){
 6 |            if(nums[l] + nums[r] <= T){
 7 |                  count += (r-l);
 8 |                   l++;
 9 |            }else{
10 |                  r--;
11 |            }
12 |     }
13 |     return count;
14 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 |     int count = 0;
 4 |     int l = 0;
 5 |     int r = nums.length-1;
 6 |     while(l < r){
 7 |            if(nums[l] + nums[r] <= T){
 8 |                  count += (r-l);
 9 |                   l++;
10 |            }else{
11 |                  r--;
12 |            }
13 |     }
14 |     return count;
15 | }
16 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 8.8/20  (11/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01074900 — Ved Patel

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01074900

| Tag | Change |
|---|---|
| [syntax-only] | added missing semicolons (1 line(s)) |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,40 +1,41 @@
+public class Solution {
 public static int maxValidWindowSum(int[] nums, int k) {
-    
-    int size = k - 1; 
-    int sum = 0; 
-    int negativeCount = 0; 
-    boolean firstValid = false; 
+
+    int size = k - 1;
+    int sum = 0;
+    int negativeCount = 0;
+    boolean firstValid = false;
 
     //Check the first window
     for(int j = 0; j < k; j++){
           if(nums[j] < 0){
-                     negativeCount++; 
+                     negativeCount++;
            }
-           sum += nums[j]; 
+           sum += nums[j];
 
     }
 
     //Starting a valid window
-    int greatestSum = 0; 
+    int greatestSum = 0;
     if(negativeCount <= 1){
-          firstValid = true; 
-          greatestSum = sum; 
+          firstValid = true;
+          greatestSum = sum;
     }
 
     //Start Moving the window
     for(int i = size+1; i < nums.length; i++){
-          
+
 
           //Check the leaving num
           sum -= nums[i-size-1];
           if(nums[i-size-1] < 0){
-               negativeCount--; 
+               negativeCount--;
           }
 
 
-         //Check incoming Num 
-          sum += nums[i]; 
+         //Check incoming Num
+          sum += nums[i];
           if(nums[i] < 0){
-                 negativeCount++; 
+                 negativeCount++;
           }
 
@@ -46,9 +47,10 @@
            //Found bigger sum
            if(sum > greatestSum || firstValid){
-                  greatestSum = sum; 
-                   firstValid = false; //Found first valid window (EDGE CASE)
+                  greatestSum = sum;
+                   firstValid = false; //Found first valid window (EDGE CASE);
            }
     }
 
-    return greatestSum; 
+    return greatestSum;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) {
 2 |     
 3 |     int size = k - 1; 
 4 |     int sum = 0; 
 5 |     int negativeCount = 0; 
 6 |     boolean firstValid = false; 
 7 | 
 8 |     //Check the first window
 9 |     for(int j = 0; j < k; j++){
10 |           if(nums[j] < 0){
11 |                      negativeCount++; 
12 |            }
13 |            sum += nums[j]; 
14 | 
15 |     }
16 | 
17 |     //Starting a valid window
18 |     int greatestSum = 0; 
19 |     if(negativeCount <= 1){
20 |           firstValid = true; 
21 |           greatestSum = sum; 
22 |     }
23 | 
24 |     //Start Moving the window
25 |     for(int i = size+1; i < nums.length; i++){
26 |           
27 | 
28 |           //Check the leaving num
29 |           sum -= nums[i-size-1];
30 |           if(nums[i-size-1] < 0){
31 |                negativeCount--; 
32 |           }
33 | 
34 | 
35 |          //Check incoming Num 
36 |           sum += nums[i]; 
37 |           if(nums[i] < 0){
38 |                  negativeCount++; 
39 |           }
40 | 
41 |            //not valid window
42 |            if(negativeCount > 1){
43 |                  continue;
44 |            }
45 | 
46 |            //Found bigger sum
47 |            if(sum > greatestSum || firstValid){
48 |                   greatestSum = sum; 
49 |                    firstValid = false; //Found first valid window (EDGE CASE)
50 |            }
51 |     }
52 | 
53 |     return greatestSum; 
54 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int maxValidWindowSum(int[] nums, int k) {
 3 | 
 4 |     int size = k - 1;
 5 |     int sum = 0;
 6 |     int negativeCount = 0;
 7 |     boolean firstValid = false;
 8 | 
 9 |     //Check the first window
10 |     for(int j = 0; j < k; j++){
11 |           if(nums[j] < 0){
12 |                      negativeCount++;
13 |            }
14 |            sum += nums[j];
15 | 
16 |     }
17 | 
18 |     //Starting a valid window
19 |     int greatestSum = 0;
20 |     if(negativeCount <= 1){
21 |           firstValid = true;
22 |           greatestSum = sum;
23 |     }
24 | 
25 |     //Start Moving the window
26 |     for(int i = size+1; i < nums.length; i++){
27 | 
28 | 
29 |           //Check the leaving num
30 |           sum -= nums[i-size-1];
31 |           if(nums[i-size-1] < 0){
32 |                negativeCount--;
33 |           }
34 | 
35 | 
36 |          //Check incoming Num
37 |           sum += nums[i];
38 |           if(nums[i] < 0){
39 |                  negativeCount++;
40 |           }
41 | 
42 |            //not valid window
43 |            if(negativeCount > 1){
44 |                  continue;
45 |            }
46 | 
47 |            //Found bigger sum
48 |            if(sum > greatestSum || firstValid){
49 |                   greatestSum = sum;
50 |                    firstValid = false; //Found first valid window (EDGE CASE);
51 |            }
52 |     }
53 | 
54 |     return greatestSum;
55 | }
56 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01074900

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
     // Paste this into your answer if you want to use Java
@@ -5,5 +6,5 @@
    int left = 0;
    int right = nums.length-1;
-   int sum = 0;    
+   int sum = 0;
 
    //Check for pairs
@@ -12,13 +13,14 @@
       if((nums[left] + nums[right]) <= T){
             sum = (right - left);
-            left++; 
+            left++;
       }
       else if((nums[left] + nums[right]) > T){
-            right--; 
+            right--;
       }
 
    }
 
-   return sum; 
+   return sum;
 
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 |     // Paste this into your answer if you want to use Java
 3 | 
 4 |    //Set up two pointers
 5 |    int left = 0;
 6 |    int right = nums.length-1;
 7 |    int sum = 0;    
 8 | 
 9 |    //Check for pairs
10 |    while(left <= right){
11 | 
12 |       if((nums[left] + nums[right]) <= T){
13 |             sum = (right - left);
14 |             left++; 
15 |       }
16 |       else if((nums[left] + nums[right]) > T){
17 |             right--; 
18 |       }
19 | 
20 |    }
21 | 
22 |    return sum; 
23 | 
24 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 |     // Paste this into your answer if you want to use Java
 4 | 
 5 |    //Set up two pointers
 6 |    int left = 0;
 7 |    int right = nums.length-1;
 8 |    int sum = 0;
 9 | 
10 |    //Check for pairs
11 |    while(left <= right){
12 | 
13 |       if((nums[left] + nums[right]) <= T){
14 |             sum = (right - left);
15 |             left++;
16 |       }
17 |       else if((nums[left] + nums[right]) > T){
18 |             right--;
19 |       }
20 | 
21 |    }
22 | 
23 |    return sum;
24 | 
25 | }
26 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `java`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | This was the Problem of the Day for Sunday April 12th (Minimum Distance to the Target Element), which was when I started it (I grabbed my screenshot the next day.) The time complexity should be O(n) as I iterated through the array and checked the conditions at each index. I keep track of the minimum value of abs(i - start) I checked at each iteration if the conditions are smaller than the saved minimum value. If it was then I updated it. I started the minimum as -1 as this was an invalid distance, to look for the first case. 
 2 | 
 3 | 
 4 | 
 5 | class Solution {
 6 | public:
 7 |     int getMinDistance(vector<int>& nums, int target, int start) {
 8 | 
 9 |         int distance;
10 |         int minDistance = -1;  
11 |         
12 |         for(int i = 0; i < nums.size(); i++){
13 |             if(nums[i] == target){
14 | 
15 |                 distance = i - start; 
16 |                 if(distance <= 0){
17 |                     distance *= -1; 
18 |                 }
19 | 
20 |                 if(minDistance == -1){
21 |                     minDistance = distance; 
22 |                 }
23 | 
24 |                 if (distance < minDistance) {
25 |                     minDistance = distance;
26 |                 }
27 | 
28 |                 if(distance == 0){ return 0;}
29 |             }
30 |         }
31 | 
32 |         if(minDistance == -1){
33 |             return 0; 
34 |         }
35 | 
36 |         return minDistance; 
37 |     }
38 | };
```

## Score Summary

- **Problem 1:** 18.4/20  (23/25 tests passed)
- **Problem 2:** 6.36/20  (7/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01061829 — Clare Calandra

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01061829

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     sum = 0
 3 |     num_negative = 0
 4 |     max_sum = float('-inf')
 5 |     valid_window = False
 6 | 
 7 |     for i in range(k):
 8 |         sum += nums[i]
 9 |         if nums[i] < 0:
10 |             num_negative += 1
11 | 
12 |     if num_negative <= 1:
13 |         max_sum = sum
14 |         valid_window = True
15 | 
16 |     for i in range(k, len(nums)):
17 |         outgoing = nums[i - k]
18 |         sum -= outgoing
19 |         if outgoing < 0:
20 |             num_negative -= 1
21 | 
22 |         incoming = nums[i]
23 |         sum += incoming
24 |         if incoming < 0:
25 |             num_negative += 1
26 | 
27 |         if num_negative <= 1:
28 |             max_sum = max(max_sum, sum)
29 |             valid_window = True
30 | 
31 |     return max_sum if valid_window else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     sum = 0
 3 |     num_negative = 0
 4 |     max_sum = float('-inf')
 5 |     valid_window = False
 6 | 
 7 |     for i in range(k):
 8 |         sum += nums[i]
 9 |         if nums[i] < 0:
10 |             num_negative += 1
11 | 
12 |     if num_negative <= 1:
13 |         max_sum = sum
14 |         valid_window = True
15 | 
16 |     for i in range(k, len(nums)):
17 |         outgoing = nums[i - k]
18 |         sum -= outgoing
19 |         if outgoing < 0:
20 |             num_negative -= 1
21 | 
22 |         incoming = nums[i]
23 |         sum += incoming
24 |         if incoming < 0:
25 |             num_negative += 1
26 | 
27 |         if num_negative <= 1:
28 |             max_sum = max(max_sum, sum)
29 |             valid_window = True
30 | 
31 |     return max_sum if valid_window else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01061829

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,11 +1,11 @@
 def count_pairs(nums, T):
-     left = 0
-     right = len(nums) - 1
-     count = 0
+    left = 0
+    right = len(nums) - 1
+    count = 0
 
-     while left < right:
-          current_sum = nums[left] + nums[right]
+    while left < right:
+        current_sum = nums[left] + nums[right]
 
-           if current_sum <= T:
+        if current_sum <= T:
             count += right - left
             left += 1
@@ -13,3 +13,3 @@
             right -= 1
 
-    return count
+            return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |      left = 0
 3 |      right = len(nums) - 1
 4 |      count = 0
 5 | 
 6 |      while left < right:
 7 |           current_sum = nums[left] + nums[right]
 8 | 
 9 |            if current_sum <= T:
10 |             count += right - left
11 |             left += 1
12 |         else:
13 |             right -= 1
14 | 
15 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         current_sum = nums[left] + nums[right]
 8 | 
 9 |         if current_sum <= T:
10 |             count += right - left
11 |             left += 1
12 |         else:
13 |             right -= 1
14 | 
15 |             return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | Python Answer: 
 2 | 
 3 | class Solution(object):
 4 |     def minimumDistance(self, nums):
 5 |         """
 6 |         :type nums: List[int]
 7 |         :rtype: int
 8 |         """
 9 |         from collections import defaultdict
10 |         index_map = defaultdict(list)
11 |         for i, num in enumerate(nums):
12 |             index_map[num].append(i)
13 | 
14 |         min_distance = float('inf')
15 | 
16 |         for indices in index_map.values():
17 |             if len(indices) >= 3:
18 |                 for i in range(len(indices) - 2):
19 |                     distance = 2 * (indices[i + 2] - indices[i])
20 |                     min_distance = min(min_distance, distance)
21 |         return min_distance if min_distance != float('inf') else -1
22 | 
23 | Explanation: 
24 | My response runs in linear time(O(n) because it scans the input array once to group indices by their values using a hash map. Then, for each value, it checks consecutive triples of indices. Since each index is processed a maximum of one time, the total work across all groups remains proportional to the size of the array. 
25 | The response I gave groups identical values together and records their positions. A tuple is considered "good" when three distinct indices contain the same number. By iterating through each group of indices, the solution I gave evaluates consecutive triples to find the minimum distance. If no value appears at least three times, the function returns -1, indicating that no good tuple exists.
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 4.55/20  (5/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01042677 — Evan Weisberg

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01042677

| Tag | Change |
|---|---|
| [syntax-only] | line 18: added missing colon |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 21) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,23 +1,2 @@
 def max_valid_window_sum(nums, k):
-   maxSum = 0
-   windowSum = 0
-   for n in nums[:k]:
-      windowSum += k
-   countNeg = 0
-   for n in nums[:k]:
-      if n < 0:
-         countNeg += 1
-   if countNeg <= 1:
-      maxSum = windowSum
-
-   for i in range(k, len(nums)):
-      lastEl = i-k
-      windowSum += nums[i] - nums[lastEl]
-      if nums[i] < 0:
-         countNeg += 1
-      if nums[lastEl] < 0
-         countNeg -= 1
-      if countNeg <= 1:
-         maxSum max(maxSum, windowSum)
-
-   return maxSum
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |    maxSum = 0
 3 |    windowSum = 0
 4 |    for n in nums[:k]:
 5 |       windowSum += k
 6 |    countNeg = 0
 7 |    for n in nums[:k]:
 8 |       if n < 0:
 9 |          countNeg += 1
10 |    if countNeg <= 1:
11 |       maxSum = windowSum
12 | 
13 |    for i in range(k, len(nums)):
14 |       lastEl = i-k
15 |       windowSum += nums[i] - nums[lastEl]
16 |       if nums[i] < 0:
17 |          countNeg += 1
18 |       if nums[lastEl] < 0
19 |          countNeg -= 1
20 |       if countNeg <= 1:
21 |          maxSum max(maxSum, windowSum)
22 | 
23 |    return maxSum
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01042677

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 
 3 |    count = 0
 4 |    left = 0
 5 |    right = len(nums)-1
 6 | 
 7 |    while left < right:
 8 |       if nums[left] + nums[right] <= T:
 9 |          count += right-left
10 |          left += 1
11 |       else:
12 |          right -= 1
13 |    return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 | 
 3 |    count = 0
 4 |    left = 0
 5 |    right = len(nums)-1
 6 | 
 7 |    while left < right:
 8 |       if nums[left] + nums[right] <= T:
 9 |          count += right-left
10 |          left += 1
11 |       else:
12 |          right -= 1
13 |    return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         dicton = {} # mmm map
 4 |         for i in range(len(nums)):
 5 |             if nums[i] not in dicton:
 6 |                 dicton[nums[i]] = [] # make array at nums[i] in dicton to store copies
 7 |             dicton[nums[i]].append(i) # put i as entry
 8 | 
 9 |         minDist = -1 # in case find nothing
10 |         for pos in dicton.values(): # just the lists
11 |             if len(pos) >= 3: # skip non triples
12 |                 for i in range(len(pos) - 2): # -2 to avoid out of bounds
13 |                     first = pos[i]
14 |                     third = pos[i+2]
15 |                     dist = 2*(third-first)
16 |                     if minDist == -1 or dist < minDist:
17 |                         minDist = dist
18 |         return minDist
19 | 
20 | 
21 | I believe this solution to be time complexity n. The reason for this is that the time spent should scale linearly with n for a few reasons. The first loop goes through each term in nums once. The second loop is technically a nested loop but since each element gets added to the dictionary only one time the inner loop should only see each element of nums one time ever (across all iterations of the outer loop) so it's really more like just looping through nums more times separately, which while it makes this problem a multiple of n, we remove constant multiples and thus can still call this an O(n) time. The way this solves the problem is by making a dictionary in python and for every new element making a new list entry in that dictionary and adding it. Then every time it sees a repeat of that element in the future it adds that element to the list. Then we establish the minimum distance if nothing else fits as -1 for edge cases and go through the dictionary and look at each list that's got at least 3 elements (since below that there can't be a tuple by definition). Since the middle element gets cancelled out in the distance formula, it turns out you can just look at the sets of 3 and, specifically take the third minus the first twice (since k-i happens twice if you simplify the distance formula to 2(k-i)) to get the distance. You then simply compare it to the minimum distance, and if either the current one is less or you haven't found a real distance yet (hence checking if it's -1), you set the current distance to our new minimum distance for now. Once we check all the sets of 3 in these lists, we end the for loop and return the minimum distance we found.
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01121023 — Danila Safronov

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01121023

| Tag | Change |
|---|---|
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: unmatched ')' (line 1) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,49 +1,2 @@
-Question 7.)
-def fizz_buzz(arr):
-    for num in arr:
-        if num < 0:
-            continue
-
-        if num % 3 == 0 and num % 5 == 0:
-            print("FizzBuzz")
-        elif num % 3 == 0:
-            print("Fizz")
-        elif num % 5 == 0:
-            print("Buzz")
-        else:
-            print(num)
-
-
-Question 8.)
-
 def max_valid_window_sum(nums, k):
-    window_sum = 0
-    negative_count = 0
-    max_sum = 0
-    found_valid = False
-
-    for i in range(k):
-        window_sum += nums[i]
-        if nums[i] < 0:
-            negative_count += 1
-
-    if negative_count <= 1:
-        max_sum = window_sum
-        found_valid = True
-
-    for i in range(k, len(nums)):
-        # Remove left element
-        if nums[i - k] < 0:
-            negative_count -= 1
-        window_sum -= nums[i - k]
-
-        if nums[i] < 0:
-            negative_count += 1
-        window_sum += nums[i]
-
-        if negative_count <= 1:
-            if not found_valid or window_sum > max_sum:
-                max_sum = window_sum
-                found_valid = True
-
-    return max_sum if found_valid else 0
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | Question 7.)
 2 | def fizz_buzz(arr):
 3 |     for num in arr:
 4 |         if num < 0:
 5 |             continue
 6 | 
 7 |         if num % 3 == 0 and num % 5 == 0:
 8 |             print("FizzBuzz")
 9 |         elif num % 3 == 0:
10 |             print("Fizz")
11 |         elif num % 5 == 0:
12 |             print("Buzz")
13 |         else:
14 |             print(num)
15 | 
16 | 
17 | Question 8.)
18 | 
19 | def max_valid_window_sum(nums, k):
20 |     window_sum = 0
21 |     negative_count = 0
22 |     max_sum = 0
23 |     found_valid = False
24 | 
25 |     for i in range(k):
26 |         window_sum += nums[i]
27 |         if nums[i] < 0:
28 |             negative_count += 1
29 | 
30 |     if negative_count <= 1:
31 |         max_sum = window_sum
32 |         found_valid = True
33 | 
34 |     for i in range(k, len(nums)):
35 |         # Remove left element
36 |         if nums[i - k] < 0:
37 |             negative_count -= 1
38 |         window_sum -= nums[i - k]
39 | 
40 |         if nums[i] < 0:
41 |             negative_count += 1
42 |         window_sum += nums[i]
43 | 
44 |         if negative_count <= 1:
45 |             if not found_valid or window_sum > max_sum:
46 |                 max_sum = window_sum
47 |                 found_valid = True
48 | 
49 |     return max_sum if found_valid else 0
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01121023

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             # Every index from left+1 to right works
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 | 
14 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             # Every index from left+1 to right works
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 | 
14 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         positions = {}
 4 |         ans = float('inf')
 5 | 
 6 |         # Store all positions of each number
 7 |         for i, num in enumerate(nums):
 8 |             if num not in positions:
 9 |                 positions[num] = []
10 |             positions[num].append(i)
11 | 
12 |         # Check every consecutive group of 3 equal elements
13 |         for indices in positions.values():
14 |             if len(indices) >= 3:
15 |                 for i in range(len(indices) - 2):
16 |                     ans = min(ans, 2 * (indices[i + 2] - indices[i]))
17 | 
18 |         return -1 if ans == float('inf') else ans
19 | 
20 | 
21 | 
22 | This solution runs in O(n) time because we make one pass through the array to store the positions of each number in a hash map, and then another pass through all stored indices to check groups of three consecutive equal elements. Since each index is processed only a constant number of times, the total work is linear in the size of the array.
23 | 
24 | The solution works by first storing every position where each number appears in the array. For example, if the number 5 appears at indices [1, 4, 7], we save those positions together.
25 | Then, for each number that appears at least 3 times, we check every group of 3 consecutive positions and calculate the distance using the first and third index. By checking all such groups, we can find the smallest possible distance.
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01046152 — Ashley Carozza

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01046152

| Tag | Change |
|---|---|
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -5,22 +5,22 @@
     for x in nums[:k]:
         if x < 0:
-        neg_count += 1
-
-    if neg_count <= 1:
-        max_sum = window_sum
-
-    for i in range(k, len(nums)):
-        # add incoming element
-        window_sum += nums[i]
-        if nums[i] < 0:
             neg_count += 1
 
-        # remove outgoing element
-        window_sum -= nums[i - k]
-        if nums[i - k] < 0:
-            neg_count -= 1
+            if neg_count <= 1:
+                max_sum = window_sum
 
-        if neg_count <= 1:
-            max_sum = max(max_sum, window_sum)
+                for i in range(k, len(nums)):
+                    # add incoming element
+                    window_sum += nums[i]
+                    if nums[i] < 0:
+                        neg_count += 1
 
-    return max_sum
+                        # remove outgoing element
+                        window_sum -= nums[i - k]
+                        if nums[i - k] < 0:
+                            neg_count -= 1
+
+                            if neg_count <= 1:
+                                max_sum = max(max_sum, window_sum)
+
+                                return max_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = 0
 3 |     window_sum = sum(nums[:k])
 4 |     neg_count = 0
 5 |     for x in nums[:k]:
 6 |         if x < 0:
 7 |         neg_count += 1
 8 | 
 9 |     if neg_count <= 1:
10 |         max_sum = window_sum
11 | 
12 |     for i in range(k, len(nums)):
13 |         # add incoming element
14 |         window_sum += nums[i]
15 |         if nums[i] < 0:
16 |             neg_count += 1
17 | 
18 |         # remove outgoing element
19 |         window_sum -= nums[i - k]
20 |         if nums[i - k] < 0:
21 |             neg_count -= 1
22 | 
23 |         if neg_count <= 1:
24 |             max_sum = max(max_sum, window_sum)
25 | 
26 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     max_sum = 0
 3 |     window_sum = sum(nums[:k])
 4 |     neg_count = 0
 5 |     for x in nums[:k]:
 6 |         if x < 0:
 7 |             neg_count += 1
 8 | 
 9 |             if neg_count <= 1:
10 |                 max_sum = window_sum
11 | 
12 |                 for i in range(k, len(nums)):
13 |                     # add incoming element
14 |                     window_sum += nums[i]
15 |                     if nums[i] < 0:
16 |                         neg_count += 1
17 | 
18 |                         # remove outgoing element
19 |                         window_sum -= nums[i - k]
20 |                         if nums[i - k] < 0:
21 |                             neg_count -= 1
22 | 
23 |                             if neg_count <= 1:
24 |                                 max_sum = max(max_sum, window_sum)
25 | 
26 |                                 return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01046152

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += right - left
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | N/A
```

## Score Summary

- **Problem 1:** 0.8/20  (1/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01092729 — Dominic Vega

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01092729

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     totalSum = 0
 3 |     leftptr = 0
 4 |     rightptr = 0
 5 |     tempSum = nums[0]
 6 |     negCount = 0
 7 |     if (tempSum < 0):
 8 |         negCount = 1
 9 | 
10 |     while (rightptr < len(nums)-1):
11 |         if ((rightptr - leftptr + 1) == k):
12 |             if (nums[leftptr] < 0):
13 |                 negCount-=1
14 |             tempSum -= nums[leftptr]
15 |             leftptr+=1
16 |         rightptr+=1
17 |         if (nums[rightptr] < 0):
18 |             negCount+=1
19 |         tempSum += nums[rightptr]
20 |         if (negCount <= 1 and (rightptr - leftptr + 1) == k):
21 |             totalSum = max(totalSum, tempSum)
22 |     return totalSum;
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     totalSum = 0
 3 |     leftptr = 0
 4 |     rightptr = 0
 5 |     tempSum = nums[0]
 6 |     negCount = 0
 7 |     if (tempSum < 0):
 8 |         negCount = 1
 9 | 
10 |     while (rightptr < len(nums)-1):
11 |         if ((rightptr - leftptr + 1) == k):
12 |             if (nums[leftptr] < 0):
13 |                 negCount-=1
14 |             tempSum -= nums[leftptr]
15 |             leftptr+=1
16 |         rightptr+=1
17 |         if (nums[rightptr] < 0):
18 |             negCount+=1
19 |         tempSum += nums[rightptr]
20 |         if (negCount <= 1 and (rightptr - leftptr + 1) == k):
21 |             totalSum = max(totalSum, tempSum)
22 |     return totalSum;
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01092729

| Tag | Change |
|---|---|
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 1) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,18 +1,2 @@
-Slight issue, the question says that valid pairs are <= T, but the first example answer excludes pairs where the sum is equal to T. In the version I wrote, these pairs are included to match the question.
-
 def count_pairs(nums, T):
-    leftptr = 0;
-    rightptr = 1;
-    validPairs = 0;
-    while (leftptr < len(nums) - 1):
-        if (nums[leftptr] + nums[rightptr] <= T):
-            if (nums[leftptr] < nums[rightptr]):
-                validPairs+=1;
-            rightptr+=1;
-            if(rightptr >= len(nums)):
-                leftptr += 1;
-                rightptr = leftptr+1;
-        else:
-            leftptr += 1;
-            rightptr = leftptr+1;
-    return validPairs;
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | Slight issue, the question says that valid pairs are <= T, but the first example answer excludes pairs where the sum is equal to T. In the version I wrote, these pairs are included to match the question.
 2 | 
 3 | def count_pairs(nums, T):
 4 |     leftptr = 0;
 5 |     rightptr = 1;
 6 |     validPairs = 0;
 7 |     while (leftptr < len(nums) - 1):
 8 |         if (nums[leftptr] + nums[rightptr] <= T):
 9 |             if (nums[leftptr] < nums[rightptr]):
10 |                 validPairs+=1;
11 |             rightptr+=1;
12 |             if(rightptr >= len(nums)):
13 |                 leftptr += 1;
14 |                 rightptr = leftptr+1;
15 |         else:
16 |             leftptr += 1;
17 |             rightptr = leftptr+1;
18 |     return validPairs;
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 16.8/20  (21/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01129735 — Solomon Coverdale

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01129735

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,33 +1,34 @@
-def max_value_window_sums(nums, k):
-    max_sum = 0
-    curr_sum = 0
-    negs = 0
-    start = 0
-    end = k
+def max_valid_window_sum(nums, k):
+    def max_value_window_sums(nums, k):
+        max_sum = 0
+        curr_sum = 0
+        negs = 0
+        start = 0
+        end = k
 
-    for i in range(k):
-        curr_sum += nums[i]
-        if nums[i] < 0:
-            negs+=1
+        for i in range(k):
+            curr_sum += nums[i]
+            if nums[i] < 0:
+                negs+=1
         
-    if negs <= 1:
-        max_sum = curr_sum
+        if negs <= 1:
+            max_sum = curr_sum
 
 
-    while(end < len(nums)):
-        curr_sum += nums[end]
-        if nums[end] < 0:
-            negs += 1
+        while(end < len(nums)):
+            curr_sum += nums[end]
+            if nums[end] < 0:
+                negs += 1
         
-        curr_sum -= nums[start]
-        if nums[start] < 0:
-            negs -= 1
+            curr_sum -= nums[start]
+            if nums[start] < 0:
+                negs -= 1
         
-        if negs <= 1:
-            if curr_sum > max_sum:
-                max_sum = curr_sum
+            if negs <= 1:
+                if curr_sum > max_sum:
+                    max_sum = curr_sum
         
-        start += 1
-        end += 1
+            start += 1
+            end += 1
     
-    return max_sum
+        return max_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_value_window_sums(nums, k):
 2 |     max_sum = 0
 3 |     curr_sum = 0
 4 |     negs = 0
 5 |     start = 0
 6 |     end = k
 7 | 
 8 |     for i in range(k):
 9 |         curr_sum += nums[i]
10 |         if nums[i] < 0:
11 |             negs+=1
12 |         
13 |     if negs <= 1:
14 |         max_sum = curr_sum
15 | 
16 | 
17 |     while(end < len(nums)):
18 |         curr_sum += nums[end]
19 |         if nums[end] < 0:
20 |             negs += 1
21 |         
22 |         curr_sum -= nums[start]
23 |         if nums[start] < 0:
24 |             negs -= 1
25 |         
26 |         if negs <= 1:
27 |             if curr_sum > max_sum:
28 |                 max_sum = curr_sum
29 |         
30 |         start += 1
31 |         end += 1
32 |     
33 |     return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     def max_value_window_sums(nums, k):
 3 |         max_sum = 0
 4 |         curr_sum = 0
 5 |         negs = 0
 6 |         start = 0
 7 |         end = k
 8 | 
 9 |         for i in range(k):
10 |             curr_sum += nums[i]
11 |             if nums[i] < 0:
12 |                 negs+=1
13 |         
14 |         if negs <= 1:
15 |             max_sum = curr_sum
16 | 
17 | 
18 |         while(end < len(nums)):
19 |             curr_sum += nums[end]
20 |             if nums[end] < 0:
21 |                 negs += 1
22 |         
23 |             curr_sum -= nums[start]
24 |             if nums[start] < 0:
25 |                 negs -= 1
26 |         
27 |             if negs <= 1:
28 |                 if curr_sum > max_sum:
29 |                     max_sum = curr_sum
30 |         
31 |             start += 1
32 |             end += 1
33 |     
34 |         return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01129735

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     start= 0
 3 |     end = len(nums) -1
 4 |     pairs = 0
 5 | 
 6 |     
 7 |     while start < end:
 8 |         if nums[start] + nums[end] <= T:
 9 |             pairs += (end - start)
10 |             start += 1
11 |         else:
12 |             end -= 1
13 | 
14 |     
15 |     return pairs
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     start= 0
 3 |     end = len(nums) -1
 4 |     pairs = 0
 5 | 
 6 |     
 7 |     while start < end:
 8 |         if nums[start] + nums[end] <= T:
 9 |             pairs += (end - start)
10 |             start += 1
11 |         else:
12 |             end -= 1
13 | 
14 |     
15 |     return pairs
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         seen = {}
 4 |         min_dist = float('inf')
 5 | 
 6 |         for i, val in enumerate(nums):
 7 |             if val not in seen:
 8 |                 seen[val] = []
 9 |             seen[val].append(i)
10 | 
11 |             if len(seen[val]) >= 3:
12 |                 curr_dist = 2 * (seen[va][-1] - seen[val][-3])
13 |                 if curr_dist < min_dist:
14 |                     min_dist = curr_dist
15 |                 
16 |         if min_dist != float('inf'):
17 |             return min_dist
18 |         else:
19 |             return -1
20 | 
21 | The time complexity would be O(n) since there is only one for loop to go through the list one time, then they get put into a dictionary. This solves the Evalute in UMPIRE because it is basically explaining the thought process behind it.
```

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01133126 — Tiffany Lin

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01133126

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k:
 4 |         return 0
 5 |     
 6 |     windowsum = 0
 7 |     negcount = 0
 8 |  
 9 |     for i in range(k):
10 |         windowsum += nums[i]
11 |         if nums[i] < 0:
12 |             negcount += 1
13 | 
14 | 
15 |     maxsum = windowsum if negcount <= 1 else float('-inf')
16 |     
17 | 
18 |     for i in range(k, n):
19 |         windowsum += nums[i]
20 |         if nums[i] < 0:
21 |             negcount += 1
22 |   
23 | 
24 |         left = nums[i - k]
25 |         windowsum -= left
26 |         if left < 0:
27 |             negcount -= 1
28 |         
29 |         if negcount <= 1:
30 |             maxsum = max(maxsum, windowsum)
31 |     
32 |     return maxsum if maxsum != float('-inf') else 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     if n < k:
 4 |         return 0
 5 |     
 6 |     windowsum = 0
 7 |     negcount = 0
 8 |  
 9 |     for i in range(k):
10 |         windowsum += nums[i]
11 |         if nums[i] < 0:
12 |             negcount += 1
13 | 
14 | 
15 |     maxsum = windowsum if negcount <= 1 else float('-inf')
16 |     
17 | 
18 |     for i in range(k, n):
19 |         windowsum += nums[i]
20 |         if nums[i] < 0:
21 |             negcount += 1
22 |   
23 | 
24 |         left = nums[i - k]
25 |         windowsum -= left
26 |         if left < 0:
27 |             negcount -= 1
28 |         
29 |         if negcount <= 1:
30 |             maxsum = max(maxsum, windowsum)
31 |     
32 |     return maxsum if maxsum != float('-inf') else 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01133126

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def count_pairs(nums, T)` |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,16 +1,17 @@
-def count_valid_pairs(nums, T):
+def count_pairs(nums, T):
+    def count_valid_pairs(nums, T):
 
-    left = 0
-    right = len(nums) - 1
-    count = 0
+        left = 0
+        right = len(nums) - 1
+        count = 0
     
-    while left < right:
-        currentsum = nums[left] + nums[right]
+        while left < right:
+            currentsum = nums[left] + nums[right]
         
-        if currentsum <= T:
-            count += (right - left)
-            left += 1
-        else:
-            right -= 1
+            if currentsum <= T:
+                count += (right - left)
+                left += 1
+            else:
+                right -= 1
     
-    return count
+        return count
```

</details>

**Raw extracted input:**

```
 1 | def count_valid_pairs(nums, T):
 2 | 
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     count = 0
 6 |     
 7 |     while left < right:
 8 |         currentsum = nums[left] + nums[right]
 9 |         
10 |         if currentsum <= T:
11 |             count += (right - left)
12 |             left += 1
13 |         else:
14 |             right -= 1
15 |     
16 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     def count_valid_pairs(nums, T):
 3 | 
 4 |         left = 0
 5 |         right = len(nums) - 1
 6 |         count = 0
 7 |     
 8 |         while left < right:
 9 |             currentsum = nums[left] + nums[right]
10 |         
11 |             if currentsum <= T:
12 |                 count += (right - left)
13 |                 left += 1
14 |             else:
15 |                 right -= 1
16 |     
17 |         return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 0.0/20  (0/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01140660 — Naman Kukreti

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01140660

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     currsum = sum(nums[:k])
 3 |     numofnegs = sum(1 for x in nums[:k] if x < 0)
 4 |     max_sum = -float('inf')
 5 |     found_valid = False
 6 |     if numofnegs <= 1:
 7 |         max_sum = currsum
 8 |         found_valid = True    
 9 |     for i in range(k, len(nums)):
10 |         currsum += nums[i]
11 |         if nums[i] < 0:
12 |             numofnegs += 1            
13 |         old_val = nums[i - k]
14 |         currsum -= old_val
15 |         if old_val < 0:
16 |             numofnegs -= 1        
17 |         if numofnegs <= 1:
18 |             if currsum > max_sum:
19 |                 max_sum = currsum
20 |             found_valid = True
21 |     if found_valid:
22 |         return max_sum
23 |     else:
24 |         return 0
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     currsum = sum(nums[:k])
 3 |     numofnegs = sum(1 for x in nums[:k] if x < 0)
 4 |     max_sum = -float('inf')
 5 |     found_valid = False
 6 |     if numofnegs <= 1:
 7 |         max_sum = currsum
 8 |         found_valid = True    
 9 |     for i in range(k, len(nums)):
10 |         currsum += nums[i]
11 |         if nums[i] < 0:
12 |             numofnegs += 1            
13 |         old_val = nums[i - k]
14 |         currsum -= old_val
15 |         if old_val < 0:
16 |             numofnegs -= 1        
17 |         if numofnegs <= 1:
18 |             if currsum > max_sum:
19 |                 max_sum = currsum
20 |             found_valid = True
21 |     if found_valid:
22 |         return max_sum
23 |     else:
24 |         return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01140660

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def count_pairs(nums, T)` |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,15 +1,16 @@
-def count_valid_pairs(nums, T):
-    count = 0
-    L = 0
-    R = len(nums) - 1
+def count_pairs(nums, T):
+    def count_valid_pairs(nums, T):
+        count = 0
+        L = 0
+        R = len(nums) - 1
     
-    while L < R:
-        current_sum = nums[L] + nums[R]
+        while L < R:
+            current_sum = nums[L] + nums[R]
         
-        if current_sum <= T:
-            count += (R - L)
-            L += 1
-        else:
-            R -= 1
+            if current_sum <= T:
+                count += (R - L)
+                L += 1
+            else:
+                R -= 1
             
-    return count
+        return count
```

</details>

**Raw extracted input:**

```
 1 | def count_valid_pairs(nums, T):
 2 |     count = 0
 3 |     L = 0
 4 |     R = len(nums) - 1
 5 |     
 6 |     while L < R:
 7 |         current_sum = nums[L] + nums[R]
 8 |         
 9 |         if current_sum <= T:
10 |             count += (R - L)
11 |             L += 1
12 |         else:
13 |             R -= 1
14 |             
15 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     def count_valid_pairs(nums, T):
 3 |         count = 0
 4 |         L = 0
 5 |         R = len(nums) - 1
 6 |     
 7 |         while L < R:
 8 |             current_sum = nums[L] + nums[R]
 9 |         
10 |             if current_sum <= T:
11 |                 count += (R - L)
12 |                 L += 1
13 |             else:
14 |                 R -= 1
15 |             
16 |         return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | #ok I don't really know how to find this, but I'm pretty sure the question of the day is a hard...
 2 | There was this one I was gonna do that I finished called container with most water
 3 |     
 4 | def maxArea(self, height: List[int]) -> int:
 5 |         L = 0
 6 |         R = len(height) - 1
 7 |         area = 0
 8 | 
 9 |         while L < R:
10 |             area = max(area, (R-L)*min(height[L], height[R]))
11 |             if height[L] < height[R]:
12 |                 L+=1
13 |             elif height[R] < height[L]:
14 |                 R-=1
15 |             else:
16 |                 L+=1
17 |                 R-=1
18 |         return area
19 | #because of the two pointer L, R system, it is an O(n) algorithm. Because multiplication, and therefore area is commutative, we can multiply the area each time through the loop, and move through it depending on which height is bigger than the other. And if they're the same, we increment both. This will cover the max heights. *Also I realize this is a bonus question, so I guess asking to finish a hard was reasonable, regardless this is what I ended up with.*
```

## Score Summary

- **Problem 1:** 20.0/20  (25/25 tests passed)
- **Problem 2:** 0.0/20  (0/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01170355 — Vincent Zheng

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01170355

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,19 +1,20 @@
-from collections import deque
-class Solution(object):
-    def maxSlidingWindow(self, nums, k):
-        q = deque()
-        ans = []
+def max_valid_window_sum(nums, k):
+    from collections import deque
+    class Solution(object):
+        def maxSlidingWindow(self, nums, k):
+            q = deque()
+            ans = []
 
-        for i in range(len(nums)):
-            if q and q[0] <= i -k:
-                q.popleft()
+            for i in range(len(nums)):
+                if q and q[0] <= i -k:
+                    q.popleft()
 
-            while q and nums[q[-1]] < nums[i]:
-                q.pop()
+                while q and nums[q[-1]] < nums[i]:
+                    q.pop()
 
-            q.append(i)
+                q.append(i)
 
-            if i >= k - 1:
-                ans.append(nums[q[0]])
+                if i >= k - 1:
+                    ans.append(nums[q[0]])
 
-        return ans        
+            return ans        
```

</details>

**Raw extracted input:**

```
 1 | from collections import deque
 2 | class Solution(object):
 3 |     def maxSlidingWindow(self, nums, k):
 4 |         q = deque()
 5 |         ans = []
 6 | 
 7 |         for i in range(len(nums)):
 8 |             if q and q[0] <= i -k:
 9 |                 q.popleft()
10 | 
11 |             while q and nums[q[-1]] < nums[i]:
12 |                 q.pop()
13 | 
14 |             q.append(i)
15 | 
16 |             if i >= k - 1:
17 |                 ans.append(nums[q[0]])
18 | 
19 |         return ans        
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     from collections import deque
 3 |     class Solution(object):
 4 |         def maxSlidingWindow(self, nums, k):
 5 |             q = deque()
 6 |             ans = []
 7 | 
 8 |             for i in range(len(nums)):
 9 |                 if q and q[0] <= i -k:
10 |                     q.popleft()
11 | 
12 |                 while q and nums[q[-1]] < nums[i]:
13 |                     q.pop()
14 | 
15 |                 q.append(i)
16 | 
17 |                 if i >= k - 1:
18 |                     ans.append(nums[q[0]])
19 | 
20 |             return ans        
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01170355

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | # Paste this into your answer if you want to use Python
 3 |     count = 0
 4 |     left = 0
 5 |     right = len(nums) - 1
 6 |     
 7 |     while left < right:
 8 |         if nums[left] + nums[right] <= T:
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |             
14 |     return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 | # Paste this into your answer if you want to use Python
 3 |     count = 0
 4 |     left = 0
 5 |     right = len(nums) - 1
 6 |     
 7 |     while left < right:
 8 |         if nums[left] + nums[right] <= T:
 9 |             count += (right - left)
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |             
14 |     return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/?envType=daily-question&envId=2026-04-11
 2 | 
 3 | class Solution:
 4 |     def minimumDistance(self, nums):
 5 |         from collections import defaultdict
 6 | 
 7 |         mp = defaultdict(list)
 8 | 
 9 |         for i, val in enumerate(nums):
10 |             mp[val].append(i)
11 | 
12 |         ans = float('inf')
13 | 
14 |         for v in mp.values():
15 |             if len(v) >= 3:
16 |                 for i in range(len(v) - 2):
17 |                     d = 2 * (v[i + 2] - v[i])
18 |                     ans = min(ans, d)
19 | 
20 |         return -1 if ans == float('inf') else ans
```

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 20.0/20  (22/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01146794 — Albert Chen

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01146794

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,3 +1,4 @@
-  left=0
+def max_valid_window_sum(nums, k):
+    left=0
     right=k-1 # fixed window of length k
     sum=0
@@ -24,6 +25,6 @@
         if sum >maxSum and negCount <=1: #checks if the sum of the current window is greater than our maximum if so set max to sum and if it's valid
             validWindow = True
-            maxSum=sum            
+            maxSum=sum
     if not validWindow:
-        return "Window of length k could not be found"                
+        return "Window of length k could not be found"
     return maxSum
```

</details>

**Raw extracted input:**

```
 1 |   left=0
 2 |     right=k-1 # fixed window of length k
 3 |     sum=0
 4 |     negCount=0
 5 |     validWindow=False
 6 |     maxSum=0
 7 |     for i in range(0,right+1): #initializes sum to be the sum of all values in the starting window
 8 |         sum+=nums[i]
 9 |         if (nums[i]< 0):
10 |             negCount +=1
11 |     if negCount <= 1:#check if initial window's valid
12 |         maxSum = sum
13 |         validWindow = True
14 | 
15 |     while right < len(nums)-1:#until we reach the end of the list
16 |         if nums[left] <0: #changes count of negatives if the removed element is negative
17 |             negCount-=1
18 |         sum-=nums[left]
19 |         left+=1
20 |         right+=1 #increments right side of window
21 |         sum+=nums[right]
22 |         if (nums[right]< 0):
23 |                 negCount +=1
24 |         if sum >maxSum and negCount <=1: #checks if the sum of the current window is greater than our maximum if so set max to sum and if it's valid
25 |             validWindow = True
26 |             maxSum=sum            
27 |     if not validWindow:
28 |         return "Window of length k could not be found"                
29 |     return maxSum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     left=0
 3 |     right=k-1 # fixed window of length k
 4 |     sum=0
 5 |     negCount=0
 6 |     validWindow=False
 7 |     maxSum=0
 8 |     for i in range(0,right+1): #initializes sum to be the sum of all values in the starting window
 9 |         sum+=nums[i]
10 |         if (nums[i]< 0):
11 |             negCount +=1
12 |     if negCount <= 1:#check if initial window's valid
13 |         maxSum = sum
14 |         validWindow = True
15 | 
16 |     while right < len(nums)-1:#until we reach the end of the list
17 |         if nums[left] <0: #changes count of negatives if the removed element is negative
18 |             negCount-=1
19 |         sum-=nums[left]
20 |         left+=1
21 |         right+=1 #increments right side of window
22 |         sum+=nums[right]
23 |         if (nums[right]< 0):
24 |                 negCount +=1
25 |         if sum >maxSum and negCount <=1: #checks if the sum of the current window is greater than our maximum if so set max to sum and if it's valid
26 |             validWindow = True
27 |             maxSum=sum
28 |     if not validWindow:
29 |         return "Window of length k could not be found"
30 |     return maxSum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01146794

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T): #use two pointers
 2 |     pairs = 0 
 3 |     left = 0  
 4 |     right = len(nums)-1
 5 |     while(left < right): # loop until left is less than right
 6 |         if(nums[left] + nums[right] < T): # if nums[left] + nums[right] is less than or equal T  update the number of valid pairs and increment the left 
 7 |             pairs += right-left 
 8 |             left += 1 
 9 |         else: #if not valid pair decrease the right
10 |             right -= 1
11 |     print(pairs)
```

**Fixed input:**

```
 1 | def count_pairs(nums, T): #use two pointers
 2 |     pairs = 0 
 3 |     left = 0  
 4 |     right = len(nums)-1
 5 |     while(left < right): # loop until left is less than right
 6 |         if(nums[left] + nums[right] < T): # if nums[left] + nums[right] is less than or equal T  update the number of valid pairs and increment the left 
 7 |             pairs += right-left 
 8 |             left += 1 
 9 |         else: #if not valid pair decrease the right
10 |             right -= 1
11 |     print(pairs)
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 17.6/20  (22/25 tests passed)
- **Problem 2:** 0.0/20  (0/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01137834 — William Connors

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01137834

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: unterminated string literal (detected at line 4) (line 4) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,16 +1,2 @@
 def max_valid_window_sum(nums, k):
-	curr_sum = sum (nums[:k])
-         neg_count = sum(1 for x in nums[:k] if x < 0)
-         max_sum = curr_sum if neg_count <= 1 else float('-inf)
-
-
-         for i in range (k, len(nums))):
-
-         curr_sum += nums [i] - (nums [i-k] < 0)
-         neg_count += (nums [i] < 0) - (nums[i-k] < 0)
-
-         if neg_count <= 1: 
-              max_sum = max(max_sum, curr_sum)
-
-          return max_sum if max_sum != float('-inf) else 0
-         
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 	curr_sum = sum (nums[:k])
 3 |          neg_count = sum(1 for x in nums[:k] if x < 0)
 4 |          max_sum = curr_sum if neg_count <= 1 else float('-inf)
 5 | 
 6 | 
 7 |          for i in range (k, len(nums))):
 8 | 
 9 |          curr_sum += nums [i] - (nums [i-k] < 0)
10 |          neg_count += (nums [i] < 0) - (nums[i-k] < 0)
11 | 
12 |          if neg_count <= 1: 
13 |               max_sum = max(max_sum, curr_sum)
14 | 
15 |           return max_sum if max_sum != float('-inf) else 0
16 |          
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01137834

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,13 +1,13 @@
 def count_pairs (nums, T):
-       count = 0
-       left, right = 0, len(nums) - 1
+    count = 0
+    left, right = 0, len(nums) - 1
 
-       while left < right:
-       if nums[left] + nums[right] <= T:
-        count += (right - left)
-        left += 1
- 
-         else:
-          right -= 1
- 
-        return count
+    while left < right:
+        if nums[left] + nums[right] <= T:
+            count += (right - left)
+            left += 1
+
+        else:
+            right -= 1
+
+            return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs (nums, T):
 2 |        count = 0
 3 |        left, right = 0, len(nums) - 1
 4 | 
 5 |        while left < right:
 6 |        if nums[left] + nums[right] <= T:
 7 |         count += (right - left)
 8 |         left += 1
 9 |  
10 |          else:
11 |           right -= 1
12 |  
13 |         return count
```

**Fixed input:**

```
 1 | def count_pairs (nums, T):
 2 |     count = 0
 3 |     left, right = 0, len(nums) - 1
 4 | 
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += (right - left)
 8 |             left += 1
 9 | 
10 |         else:
11 |             right -= 1
12 | 
13 |             return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `pseudocode`
- **status:** `pseudocode`

**Raw bonus code:**

```
1 | The time complexity of this solution is O(n). It is O(n) because to build the map, it has to pass through the array once. After it passes through the array, it has to pass through the stored indices. It passes through those twice, making this a linear problem. 
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 4.55/20  (5/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01077623 — Ryan Tsui

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01077623

| Tag | Change |
|---|---|
| [syntax-only] | line 10: added missing colon |
| [syntax-only] | line 15: added missing colon |
| [syntax-only] | line 27: added missing colon |
| [syntax-only] | appended 1 missing closing bracket(s) |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 4) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,30 +1,2 @@
 def max_valid_window_sum(nums, k):
-#how i would go with this
-#sliding window approach b/c it will run in o(n) time complexity
-initialize the values of window, negative count, and max sum to 0
-window = 0
-count = 0
-maxSum = 0
-length = len(nums)
-
-for the first k elements (for i in range(k))
-add each number to the window (meaning window += nums[i])
-if number is less than 0: nums[i] < 0
-increment negative: count += 1
-
-if count is less than or equal to 1
-set maxSum to the window
-if count <= 1:
-maxSum = window
-
-for each index i from k to the end of the array:
-add nums[i] to window
-if nums[i] is less than 0:
-     increment count (+=)
-if nums[i - k] is less than 0:
-     decrement count (-=)
-subtract nums[i - k] from window
-if count is less or equal to 1
-set maxSum to the max sum and window (max(maxSum, window)
-
-return maxSum
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | #how i would go with this
 3 | #sliding window approach b/c it will run in o(n) time complexity
 4 | initialize the values of window, negative count, and max sum to 0
 5 | window = 0
 6 | count = 0
 7 | maxSum = 0
 8 | length = len(nums)
 9 | 
10 | for the first k elements (for i in range(k))
11 | add each number to the window (meaning window += nums[i])
12 | if number is less than 0: nums[i] < 0
13 | increment negative: count += 1
14 | 
15 | if count is less than or equal to 1
16 | set maxSum to the window
17 | if count <= 1:
18 | maxSum = window
19 | 
20 | for each index i from k to the end of the array:
21 | add nums[i] to window
22 | if nums[i] is less than 0:
23 |      increment count (+=)
24 | if nums[i - k] is less than 0:
25 |      decrement count (-=)
26 | subtract nums[i - k] from window
27 | if count is less or equal to 1
28 | set maxSum to the max sum and window (max(maxSum, window)
29 | 
30 | return maxSum
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01077623

| Tag | Change |
|---|---|
| [syntax-only] | line 8: added missing colon |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 8) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,15 +1,2 @@
 def count_pairs(nums, T):
-#kind of similar to two sum but this will run in O(n) b/c its one pass
-#initialize two pointers left on the left side going up the array and right on the right side going down the array, and count
-left = 0
-right = len(nums) - 1
-count = 0
-
-while left is less than right (meaning they dont intersect yet)
-if nums[left] + nums[right] is less than or equal to T:
-add (right - left) to the count (count += (right - left))
-move left pointer one up (left += 1)
-else:
-move the right pointer down (right -= 1)
-
-return count
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | #kind of similar to two sum but this will run in O(n) b/c its one pass
 3 | #initialize two pointers left on the left side going up the array and right on the right side going down the array, and count
 4 | left = 0
 5 | right = len(nums) - 1
 6 | count = 0
 7 | 
 8 | while left is less than right (meaning they dont intersect yet)
 9 | if nums[left] + nums[right] is less than or equal to T:
10 | add (right - left) to the count (count += (right - left))
11 | move left pointer one up (left += 1)
12 | else:
13 | move the right pointer down (right -= 1)
14 | 
15 | return count
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def decodeCiphertext(self, encodedText: str, rows: int) -> str:
 3 |         cols = len(encodedText) // rows
 4 |         result = ""
 5 | 
 6 |         for i in range(cols):
 7 |             x = 0
 8 |             y = i
 9 | 
10 |             while x < rows and y < cols:
11 |                 result = result + encodedText[x * cols + y]
12 |                 x = x + 1
13 |                 y = y + 1
14 |         return result.rstrip(" ")
15 | 
16 | This solution will reconstruct the decoded message in O(n) time complexity where n is the length of encodedText and the space complexity is also O(n) with the result of the string. Through first determining the number of columns, iterating through each starting column and traversing diagonally right while increasing the row and column indexes. And at each step, it will calculate the correct index in the original string with x * cols * y to append the character to the result. The return result.rstrip(" ") takes away any spaces to return the message. 
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01093996 — Rijaa Zaidi

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01093996

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 6) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,35 +1,2 @@
-l = 0
-negatives =  0
-max  =  0
-
-for each index r within nums length:
-            if value at r is less than 0:
-                   increment negatives
-            while num negatives is 2:
-                   if val at l is negative:
-                          decrement negatives
-                          increment l
-             if r + l + 1 = k:
-                   set max to the bigger value between max and the sum of all values from indices l to r
-                   increment l
-
-print max
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+def max_valid_window_sum(nums, k):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | l = 0
 2 | negatives =  0
 3 | max  =  0
 4 | 
 5 | for each index r within nums length:
 6 |             if value at r is less than 0:
 7 |                    increment negatives
 8 |             while num negatives is 2:
 9 |                    if val at l is negative:
10 |                           decrement negatives
11 |                           increment l
12 |              if r + l + 1 = k:
13 |                    set max to the bigger value between max and the sum of all values from indices l to r
14 |                    increment l
15 | 
16 | print max
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01093996

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def count_pairs(nums, T)` |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 2) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,15 +1,2 @@
-r pointer at last index of nums
-l pointer at start index of nums
-pairs = 0
-
-while l is less than r:
-        if value at l plus value at r is greater than T:
-              decrement r
-        else:
-              pairs = r - l
-              increment l
-
-print pairs
-
-
-
+def count_pairs(nums, T):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | r pointer at last index of nums
 2 | l pointer at start index of nums
 3 | pairs = 0
 4 | 
 5 | while l is less than r:
 6 |         if value at l plus value at r is greater than T:
 7 |               decrement r
 8 |         else:
 9 |               pairs = r - l
10 |               increment l
11 | 
12 | print pairs
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01097725 — Parks Rpk

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01097725

| Tag | Change |
|---|---|
| [syntax-only] | converted `//` line comments to `#` (1 lines) |
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 2) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,35 +1,2 @@
-Function max_valid_window_sum(nums, k):
-
-    Set max_sum = 0
-    Set window_sum = 0
-    Set negative_count = 0
-
-    # Build the first window
-    For i from 0 to k-1:
-        Add nums[i] to window_sum
-        If nums[i] < 0:
-            Add 1 to negative_count
-
-    # Check if first window is valid (at most 1 negative)
-    If negative_count <= 1:
-        Set max_sum = window_sum
-
-    #Slide the window across the rest of the array
-    For right from k to len(nums)-1:
-        Set left = right - k   // left is the element being removed
-
-        #Bring in the new right element
-        Add nums[right] to window_sum
-        If nums[right] < 0:
-            Add 1 to negative_count
-
-        #Remove the old left element
-        Subtract nums[left] from window_sum
-        If nums[left] < 0:
-            Subtract 1 from negative_count
-
-        # If window is valid, update max if current sum is larger
-        If negative_count <= 1:
-            Set max_sum = max(max_sum, window_sum)
-
-    Return max_sum
+def max_valid_window_sum(nums, k):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | Function max_valid_window_sum(nums, k):
 2 | 
 3 |     Set max_sum = 0
 4 |     Set window_sum = 0
 5 |     Set negative_count = 0
 6 | 
 7 |     # Build the first window
 8 |     For i from 0 to k-1:
 9 |         Add nums[i] to window_sum
10 |         If nums[i] < 0:
11 |             Add 1 to negative_count
12 | 
13 |     # Check if first window is valid (at most 1 negative)
14 |     If negative_count <= 1:
15 |         Set max_sum = window_sum
16 | 
17 |     #Slide the window across the rest of the array
18 |     For right from k to len(nums)-1:
19 |         Set left = right - k   // left is the element being removed
20 | 
21 |         #Bring in the new right element
22 |         Add nums[right] to window_sum
23 |         If nums[right] < 0:
24 |             Add 1 to negative_count
25 | 
26 |         #Remove the old left element
27 |         Subtract nums[left] from window_sum
28 |         If nums[left] < 0:
29 |             Subtract 1 from negative_count
30 | 
31 |         # If window is valid, update max if current sum is larger
32 |         If negative_count <= 1:
33 |             Set max_sum = max(max_sum, window_sum)
34 | 
35 |     Return max_sum
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01097725

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def count_pairs(nums, T)` |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 2) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,22 +1,2 @@
-Function countPairs(nums, T):
-
-    Set left = 0
-    Set right = len(nums) - 1
-    Set count = 0
-
-    While left < right:
-
-        #Check if the pair at left and right is valid
-        If nums[left] + nums[right] <= T:
-
-            #ALL pairs between left and right are valid
-            # because the array is sorted, everything between
-            # left+1, left+2 ... right-1 paired with left also works
-            Add (right - left) to count
-            Move left forward by 1
-
-        Else:
-            # Sum is too big, bring right inward to get a smaller sum
-            Move right backward by 1
-
-    Return count
+def count_pairs(nums, T):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | Function countPairs(nums, T):
 2 | 
 3 |     Set left = 0
 4 |     Set right = len(nums) - 1
 5 |     Set count = 0
 6 | 
 7 |     While left < right:
 8 | 
 9 |         #Check if the pair at left and right is valid
10 |         If nums[left] + nums[right] <= T:
11 | 
12 |             #ALL pairs between left and right are valid
13 |             # because the array is sorted, everything between
14 |             # left+1, left+2 ... right-1 paired with left also works
15 |             Add (right - left) to count
16 |             Move left forward by 1
17 | 
18 |         Else:
19 |             # Sum is too big, bring right inward to get a smaller sum
20 |             Move right backward by 1
21 | 
22 |     Return count
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `pseudocode`
- **status:** `pseudocode`

**Raw bonus code:**

```
1 | I build the result string step by step. For every 'T', I force that part of the string to match str2. If there's a conflict, I return empty. For every 'F', I check if it accidentally matches str2, and if it does, I change one character (that isn't fixed) to break the match. If I can't change anything, then no valid string exists.
2 | 
3 | The solution runs in O(n × m) time because for each position in str1, I may compare or update up to m characters from str2.
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01132267 — Chuyao Yu

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01132267

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 4) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,32 +1,2 @@
 def max_valid_window_sum(nums, k):
-    n = len(nums)
-    
-   Initialize the first window
-    window_sum = sum(nums[:k])
-    neg_count = sum(1 for x in nums[:k] if x < 0)
-    
-   Track the best result
-    max_sum = window_sum if neg_count <= 1 else 0
-    found_valid = neg_count <= 1
-    
-    Slide the window
-    for i in range(k, n):
-        Add the new element entering the window
-        window_sum += nums[i]
-        if nums[i] < 0:
-            neg_count += 1
-        
-        Remove the element leaving the window
-        window_sum -= nums[i - k]
-        if nums[i - k] < 0:
-            neg_count -= 1
-        
-        Check if this window is valid
-        if neg_count <= 1:
-            if not found_valid:
-                max_sum = window_sum
-                found_valid = True
-            else:
-                max_sum = max(max_sum, window_sum)
-    
-    return max_sum if found_valid else 0
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     
 4 |    Initialize the first window
 5 |     window_sum = sum(nums[:k])
 6 |     neg_count = sum(1 for x in nums[:k] if x < 0)
 7 |     
 8 |    Track the best result
 9 |     max_sum = window_sum if neg_count <= 1 else 0
10 |     found_valid = neg_count <= 1
11 |     
12 |     Slide the window
13 |     for i in range(k, n):
14 |         Add the new element entering the window
15 |         window_sum += nums[i]
16 |         if nums[i] < 0:
17 |             neg_count += 1
18 |         
19 |         Remove the element leaving the window
20 |         window_sum -= nums[i - k]
21 |         if nums[i - k] < 0:
22 |             neg_count -= 1
23 |         
24 |         Check if this window is valid
25 |         if neg_count <= 1:
26 |             if not found_valid:
27 |                 max_sum = window_sum
28 |                 found_valid = True
29 |             else:
30 |                 max_sum = max(max_sum, window_sum)
31 |     
32 |     return max_sum if found_valid else 0
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01132267

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 8) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,14 +1,2 @@
 def count_pairs(nums, T):
-    left = 0
-    right = len(nums) - 1
-    count = 0
-    
-    while left < right:
-        if nums[left] + nums[right] <= T:
-            All pairs (left, left+1), (left, left+2), ..., (left, right) are valid
-            count += right - left
-            left += 1
-        else:
-            right -= 1
-    
-    return count
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 |     
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             All pairs (left, left+1), (left, left+2), ..., (left, right) are valid
 9 |             count += right - left
10 |             left += 1
11 |         else:
12 |             right -= 1
13 |     
14 |     return count
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | /
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01137729 — Jason Guo

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01137729

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 2) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,22 +1,2 @@
-sum = sum of nums[0] through nums[k -1]
-
-negCount = 0
-for i from 0 to k - 1:
-    if nums[i] < 0:
-        negCount++
-
-total= 0
-
-if negCount <= 1:
-    total = sum 
-for i from k to len(nums) - 1:
-    sum += nums[i]       
-    sum -= nums[i - k]     
-    if nums[i] <0: 
-        negCount++  
-    if nums[i - k] < 0: 
-        negCount-- 
-    if negCount <= 1:
-        total = maxOf(total, sum)
-
-return total
+def max_valid_window_sum(nums, k):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | sum = sum of nums[0] through nums[k -1]
 2 | 
 3 | negCount = 0
 4 | for i from 0 to k - 1:
 5 |     if nums[i] < 0:
 6 |         negCount++
 7 | 
 8 | total= 0
 9 | 
10 | if negCount <= 1:
11 |     total = sum 
12 | for i from k to len(nums) - 1:
13 |     sum += nums[i]       
14 |     sum -= nums[i - k]     
15 |     if nums[i] <0: 
16 |         negCount++  
17 |     if nums[i - k] < 0: 
18 |         negCount-- 
19 |     if negCount <= 1:
20 |         total = maxOf(total, sum)
21 | 
22 | return total
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01137729

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def count_pairs(nums, T)` |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 8) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,10 +1,2 @@
-left = 0
-right = lenOf(nums) - 1
-counter = 0
-while left <right:
-    if nums[left]+ nums[right] <= T:
-        counter += right-left 
-        left++
-    else:
-        right--
-return counter 
+def count_pairs(nums, T):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | left = 0
 2 | right = lenOf(nums) - 1
 3 | counter = 0
 4 | while left <right:
 5 |     if nums[left]+ nums[right] <= T:
 6 |         counter += right-left 
 7 |         left++
 8 |     else:
 9 |         right--
10 | return counter 
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `repaired`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         result = float('inf')
 4 |         for num in set(nums):
 5 |             
 6 |             indces = [i for i in range(len(nums)) if nums[i] == num]
 7 |             for m in range(len(indces) - 2):
 8 |                 result = min(result, 2 * (indces[m + 2] - indces[m]))
 9 |         if result != float('inf'):
10 | 
11 |             return result 
12 |         else:
13 |             return -1
14 | 
15 | 
16 | 
17 | It's o(n) time because there is an other loop over the array. Every element is ran over a constant number of times. This solution solves by collecting indices and their triplets. Thus using the min across all valid triplets we can check the minimum distance foundor -1 if no value appeared at least 3 times.
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01145039 — Jack Stevens

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01145039

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 9) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,19 +1,2 @@
 def max_valid_window_sum(nums, k):
-    neg = 0
-    sum = 0
-    maxsum = 0
-    l = 0
-    for r in range(len(nums)):
-        sum += nums[r]
-        if nums[r] > 0:
-            neg++
-        if r - l >= k:
-            if nums[l] < 0:
-                neg--
-            sum -= nums[l]
-            left++
-        if r - l == k - 1:
-            if neg < 2:
-                if sum > maxsum:
-                      maxsum = sum
-    return maxsum
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     neg = 0
 3 |     sum = 0
 4 |     maxsum = 0
 5 |     l = 0
 6 |     for r in range(len(nums)):
 7 |         sum += nums[r]
 8 |         if nums[r] > 0:
 9 |             neg++
10 |         if r - l >= k:
11 |             if nums[l] < 0:
12 |                 neg--
13 |             sum -= nums[l]
14 |             left++
15 |         if r - l == k - 1:
16 |             if neg < 2:
17 |                 if sum > maxsum:
18 |                       maxsum = sum
19 |     return maxsum
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01145039

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 6) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,11 +1,2 @@
 def count_pairs(nums, T):
-    pairs = 0
-    r = 1
-    l = 0
-    while(r >= l):
-        if(nums[r] + nums[l] <= T && r < len(nums) - 1):
-                pairs++
-                r++
-        else:
-                l++
-    return pairs        
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     pairs = 0
 3 |     r = 1
 4 |     l = 0
 5 |     while(r >= l):
 6 |         if(nums[r] + nums[l] <= T && r < len(nums) - 1):
 7 |                 pairs++
 8 |                 r++
 9 |         else:
10 |                 l++
11 |     return pairs        
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | /
```

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01163705 — Ethan Wong

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 2

**Diff:**

# Diff for B01163705

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 6) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,18 +1,2 @@
 def max_valid_window_sum(nums, k):
-     left = 0
-     right = 0
-     negatives = 0
-     while right < len(nums):
-         if left - right < valid window size:
-	 	right ++
-		if right number is negative:
-			negatives++
-         if there is more than one negative:
-	 	if left number is negative:
-			negatives--
-		left++
-         if there is one negative AND size of window < k:
-              	solution = []
-             	for i in range(left, right + 1, 1):
-                	solution.append(num[i])
-              	print solution
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |      left = 0
 3 |      right = 0
 4 |      negatives = 0
 5 |      while right < len(nums):
 6 |          if left - right < valid window size:
 7 | 	 	right ++
 8 | 		if right number is negative:
 9 | 			negatives++
10 |          if there is more than one negative:
11 | 	 	if left number is negative:
12 | 			negatives--
13 | 		left++
14 |          if there is one negative AND size of window < k:
15 |               	solution = []
16 |              	for i in range(left, right + 1, 1):
17 |                 	solution.append(num[i])
18 |               	print solution
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 2

**Diff:**

# Diff for B01163705

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | line 8: added missing colon |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 5) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,9 +1,2 @@
 def count_pairs(nums, T):
-    right = 1
-    left = 0
-    while right > left:
-    	if sum of left and right <= T:
-		print left and right num
-		move right forward one
-	elif sum of left and right > T or right >= length of nums
-		move left one forward and right one back
+    return 0
```

</details>

**Raw extracted input:**

```
1 | def count_pairs(nums, T):
2 |     right = 1
3 |     left = 0
4 |     while right > left:
5 |     	if sum of left and right <= T:
6 | 		print left and right num
7 | 		move right forward one
8 | 	elif sum of left and right > T or right >= length of nums
9 | 		move left one forward and right one back
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01062056 — Gaven Chan

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01062056

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,22 +1,22 @@
 def max_valid_window_sum(nums, k):
-   	left = 0
-   	window_sum = 0
-   	neg_count = 0
-   	max_sum = 0
+    left = 0
+    window_sum = 0
+    neg_count = 0
+    max_sum = 0
 
-   	for right in range(len(nums)):
-  		window_sum += nums[right]
-        	if nums[right] < 0:
-            		neg_count += 1
+    for right in range(len(nums)):
+        window_sum += nums[right]
+        if nums[right] < 0:
+            neg_count += 1
 
-        	if right - left + 1 > k:
-            		if nums[left] < 0:
-                		neg_count -= 1
-            		window_sum -= nums[left]
-            		left += 1
+            if right - left + 1 > k:
+                if nums[left] < 0:
+                    neg_count -= 1
+                    window_sum -= nums[left]
+                    left += 1
 
-        	if right - left + 1 == k:
-            		if neg_count <= 1:
-                		max_sum = max(max_sum, window_sum)
+                    if right - left + 1 == k:
+                        if neg_count <= 1:
+                            max_sum = max(max_sum, window_sum)
 
-    	return max_sum
+                            return max_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |    	left = 0
 3 |    	window_sum = 0
 4 |    	neg_count = 0
 5 |    	max_sum = 0
 6 | 
 7 |    	for right in range(len(nums)):
 8 |   		window_sum += nums[right]
 9 |         	if nums[right] < 0:
10 |             		neg_count += 1
11 | 
12 |         	if right - left + 1 > k:
13 |             		if nums[left] < 0:
14 |                 		neg_count -= 1
15 |             		window_sum -= nums[left]
16 |             		left += 1
17 | 
18 |         	if right - left + 1 == k:
19 |             		if neg_count <= 1:
20 |                 		max_sum = max(max_sum, window_sum)
21 | 
22 |     	return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     left = 0
 3 |     window_sum = 0
 4 |     neg_count = 0
 5 |     max_sum = 0
 6 | 
 7 |     for right in range(len(nums)):
 8 |         window_sum += nums[right]
 9 |         if nums[right] < 0:
10 |             neg_count += 1
11 | 
12 |             if right - left + 1 > k:
13 |                 if nums[left] < 0:
14 |                     neg_count -= 1
15 |                     window_sum -= nums[left]
16 |                     left += 1
17 | 
18 |                     if right - left + 1 == k:
19 |                         if neg_count <= 1:
20 |                             max_sum = max(max_sum, window_sum)
21 | 
22 |                             return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01062056

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,13 +1,13 @@
 def count_pairs(nums, T):
-    	left = 0
-    	right = len(nums) - 1
-    	count = 0
+    left = 0
+    right = len(nums) - 1
+    count = 0
 
-    	while left < right:
-       		if nums[left] + nums[right] <= T:
-  			count += (right - left)
-            		left += 1
-        	else:
-            		right -= 1
+    while left < right:
+        if nums[left] + nums[right] <= T:
+            count += (right - left)
+            left += 1
+        else:
+            right -= 1
 
-    	return count
+            return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |     	left = 0
 3 |     	right = len(nums) - 1
 4 |     	count = 0
 5 | 
 6 |     	while left < right:
 7 |        		if nums[left] + nums[right] <= T:
 8 |   			count += (right - left)
 9 |             		left += 1
10 |         	else:
11 |             		right -= 1
12 | 
13 |     	return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     count = 0
 5 | 
 6 |     while left < right:
 7 |         if nums[left] + nums[right] <= T:
 8 |             count += (right - left)
 9 |             left += 1
10 |         else:
11 |             right -= 1
12 | 
13 |             return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

```
1 | n/a
```

## Score Summary

- **Problem 1:** 0.8/20  (1/25 tests passed)
- **Problem 2:** 4.55/20  (5/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01006183 — Isabella Yang

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01006183

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,19 +1,19 @@
 def max_valid_window_sum(nums, k):
-	# Paste this into your answer if you want to use python
+    # Paste this into your answer if you want to use python
 
-if k > len(nums):
-return 0
+    if k > len(nums):
+        return 0
 
-curr_sum = sum(nums[:k])
-neg_count = sum(1 for i in range(k) if nums[i] <0)
+        curr_sum = sum(nums[:k])
+        neg_count = sum(1 for i in range(k) if nums[i] <0)
 
-max_sum = 0
+        max_sum = 0
 
-for i in range(k, n):
-if nums[i] < 0:
-curr_sum += nums[i]
+        for i in range(k, n):
+            if nums[i] < 0:
+                curr_sum += nums[i]
 
-if nums[i-k] < 0:
-curr_sum -= nums[i-k]
+                if nums[i-k] < 0:
+                    curr_sum -= nums[i-k]
 
-return max_sum
+                    return max_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 	# Paste this into your answer if you want to use python
 3 | 
 4 | if k > len(nums):
 5 | return 0
 6 | 
 7 | curr_sum = sum(nums[:k])
 8 | neg_count = sum(1 for i in range(k) if nums[i] <0)
 9 | 
10 | max_sum = 0
11 | 
12 | for i in range(k, n):
13 | if nums[i] < 0:
14 | curr_sum += nums[i]
15 | 
16 | if nums[i-k] < 0:
17 | curr_sum -= nums[i-k]
18 | 
19 | return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     # Paste this into your answer if you want to use python
 3 | 
 4 |     if k > len(nums):
 5 |         return 0
 6 | 
 7 |         curr_sum = sum(nums[:k])
 8 |         neg_count = sum(1 for i in range(k) if nums[i] <0)
 9 | 
10 |         max_sum = 0
11 | 
12 |         for i in range(k, n):
13 |             if nums[i] < 0:
14 |                 curr_sum += nums[i]
15 | 
16 |                 if nums[i-k] < 0:
17 |                     curr_sum -= nums[i-k]
18 | 
19 |                     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01006183

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,15 +1,15 @@
 def count_pairs(nums, T):
-	# Paste this into your answer if you want to use Python
-count = 0
-left  =0
-right = len(nums) - 1
+    # Paste this into your answer if you want to use Python
+    count = 0
+    left  =0
+    right = len(nums) - 1
 
-while left < right:
-if nums[left] + nums[right] <= T:
-count += ( right - left )
-left += 1
+    while left < right:
+        if nums[left] + nums[right] <= T:
+            count += ( right - left )
+            left += 1
 
-else:
-right -= 1
+        else:
+            right -= 1
 
-return count
+            return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 	# Paste this into your answer if you want to use Python
 3 | count = 0
 4 | left  =0
 5 | right = len(nums) - 1
 6 | 
 7 | while left < right:
 8 | if nums[left] + nums[right] <= T:
 9 | count += ( right - left )
10 | left += 1
11 | 
12 | else:
13 | right -= 1
14 | 
15 | return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     # Paste this into your answer if you want to use Python
 3 |     count = 0
 4 |     left  =0
 5 |     right = len(nums) - 1
 6 | 
 7 |     while left < right:
 8 |         if nums[left] + nums[right] <= T:
 9 |             count += ( right - left )
10 |             left += 1
11 | 
12 |         else:
13 |             right -= 1
14 | 
15 |             return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `pseudocode`
- **status:** `pseudocode`

**Raw bonus code:**

```
1 | im good
```

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 4.55/20  (5/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01050731 — Kyle Godzki

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01050731

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,21 +1,21 @@
 def max_valid_window_sum(nums, k):
-	n = len(nums)
-        window_sum = 0
-        negatives = 0
-        for i in range(k):
-              window_sum += nums[i]
-              if nums[i] < 0:
-                   negatives += 1
-         max_sum = window_sum if negatives <= 1 else None
-         for i in range(k, n):
-             window_sum += nums[i] - nums[i - k]
-             if nums[i] < 0:
-                 negatives += 1
-             if nums[i - k] < 0:
-                  negatives -= 1
-             if negatives <= 1:
-                  if max_sum is None or window_sum > max_sum:
-                        max_sum = window_sum
-         if max_sum is None:
-              return 0
-         return max_sum
+    n = len(nums)
+    window_sum = 0
+    negatives = 0
+    for i in range(k):
+        window_sum += nums[i]
+        if nums[i] < 0:
+            negatives += 1
+            max_sum = window_sum if negatives <= 1 else None
+            for i in range(k, n):
+                window_sum += nums[i] - nums[i - k]
+                if nums[i] < 0:
+                    negatives += 1
+                    if nums[i - k] < 0:
+                        negatives -= 1
+                        if negatives <= 1:
+                            if max_sum is None or window_sum > max_sum:
+                                max_sum = window_sum
+                                if max_sum is None:
+                                    return 0
+                                    return max_sum
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 	n = len(nums)
 3 |         window_sum = 0
 4 |         negatives = 0
 5 |         for i in range(k):
 6 |               window_sum += nums[i]
 7 |               if nums[i] < 0:
 8 |                    negatives += 1
 9 |          max_sum = window_sum if negatives <= 1 else None
10 |          for i in range(k, n):
11 |              window_sum += nums[i] - nums[i - k]
12 |              if nums[i] < 0:
13 |                  negatives += 1
14 |              if nums[i - k] < 0:
15 |                   negatives -= 1
16 |              if negatives <= 1:
17 |                   if max_sum is None or window_sum > max_sum:
18 |                         max_sum = window_sum
19 |          if max_sum is None:
20 |               return 0
21 |          return max_sum
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     n = len(nums)
 3 |     window_sum = 0
 4 |     negatives = 0
 5 |     for i in range(k):
 6 |         window_sum += nums[i]
 7 |         if nums[i] < 0:
 8 |             negatives += 1
 9 |             max_sum = window_sum if negatives <= 1 else None
10 |             for i in range(k, n):
11 |                 window_sum += nums[i] - nums[i - k]
12 |                 if nums[i] < 0:
13 |                     negatives += 1
14 |                     if nums[i - k] < 0:
15 |                         negatives -= 1
16 |                         if negatives <= 1:
17 |                             if max_sum is None or window_sum > max_sum:
18 |                                 max_sum = window_sum
19 |                                 if max_sum is None:
20 |                                     return 0
21 |                                     return max_sum
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01050731

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,11 +1,11 @@
 def count_pairs(nums, T):
-	count = 0
-        left = 0
-        right = len(nums) - 1
-        while left < right:
-            if nums[left] + nums[right] <= T:
-                  count += right - left
-                  left += 1
-            else:
-                  right -= 1
-         return count
+    count = 0
+    left = 0
+    right = len(nums) - 1
+    while left < right:
+        if nums[left] + nums[right] <= T:
+            count += right - left
+            left += 1
+        else:
+            right -= 1
+            return count
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 	count = 0
 3 |         left = 0
 4 |         right = len(nums) - 1
 5 |         while left < right:
 6 |             if nums[left] + nums[right] <= T:
 7 |                   count += right - left
 8 |                   left += 1
 9 |             else:
10 |                   right -= 1
11 |          return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     count = 0
 3 |     left = 0
 4 |     right = len(nums) - 1
 5 |     while left < right:
 6 |         if nums[left] + nums[right] <= T:
 7 |             count += right - left
 8 |             left += 1
 9 |         else:
10 |             right -= 1
11 |             return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `pseudocode`
- **status:** `pseudocode`

**Raw bonus code:**

```
1 | Time complexity is O(n) as we do one pass to group indices and another pass over index triples. O(n) space complexity due to using defaultdict, which I found to automatically create an empty list for any key accessed for the first time. More convenient I think. We are first building the dictionary mapping each value to all the positions it appears in. We make sure to skip values that appear less than 3 times and then use sliding window technique for 4 consecutive indices. Finally, we track minimum and handle the case where there isn't any valid tuples. 
```

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 4.55/20  (5/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01144248 — Gabriel Yang

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01144248

| Tag | Change |
|---|---|
| [syntax-only] | converted tabs to 4-space indentation |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,31 +1,31 @@
 def max_valid_window_sum(nums, k):
-	# Paste this into your answer if you want to use python
-sum = 0
-best = 0
-neg = 0
+    # Paste this into your answer if you want to use python
+    sum = 0
+    best = 0
+    neg = 0
 
-for i in range(k):
-sum += nums[j]
-if nums[j] < 0:
-neg += 1
+    for i in range(k):
+        sum += nums[j]
+        if nums[j] < 0:
+            neg += 1
 
-if neg <= 1:
-best = sum
+            if neg <= 1:
+                best = sum
 
-for j in range(k, len(nums)):
- i = j - k
-sum -= nums[i]
-if nums[i] < 0:
-neg -= 1
+                for j in range(k, len(nums)):
+                    i = j - k
+                    sum -= nums[i]
+                    if nums[i] < 0:
+                        neg -= 1
 
-sum += nums[j]
-if nums[j] < 0:
-neg += 1
+                        sum += nums[j]
+                        if nums[j] < 0:
+                            neg += 1
 
-if neg <= 1:
-best = max(best, sum)
+                            if neg <= 1:
+                                best = max(best, sum)
 
 
 
 
-return best
+                                return best
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 | 	# Paste this into your answer if you want to use python
 3 | sum = 0
 4 | best = 0
 5 | neg = 0
 6 | 
 7 | for i in range(k):
 8 | sum += nums[j]
 9 | if nums[j] < 0:
10 | neg += 1
11 | 
12 | if neg <= 1:
13 | best = sum
14 | 
15 | for j in range(k, len(nums)):
16 |  i = j - k
17 | sum -= nums[i]
18 | if nums[i] < 0:
19 | neg -= 1
20 | 
21 | sum += nums[j]
22 | if nums[j] < 0:
23 | neg += 1
24 | 
25 | if neg <= 1:
26 | best = max(best, sum)
27 | 
28 | 
29 | 
30 | 
31 | return best
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     # Paste this into your answer if you want to use python
 3 |     sum = 0
 4 |     best = 0
 5 |     neg = 0
 6 | 
 7 |     for i in range(k):
 8 |         sum += nums[j]
 9 |         if nums[j] < 0:
10 |             neg += 1
11 | 
12 |             if neg <= 1:
13 |                 best = sum
14 | 
15 |                 for j in range(k, len(nums)):
16 |                     i = j - k
17 |                     sum -= nums[i]
18 |                     if nums[i] < 0:
19 |                         neg -= 1
20 | 
21 |                         sum += nums[j]
22 |                         if nums[j] < 0:
23 |                             neg += 1
24 | 
25 |                             if neg <= 1:
26 |                                 best = max(best, sum)
27 | 
28 | 
29 | 
30 | 
31 |                                 return best
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01144248

| Tag | Change |
|---|---|
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,18 +1,18 @@
 def count_pairs(nums, T):
 
-count = 0
-i = 0
-j = len(nums) - 1
+    count = 0
+    i = 0
+    j = len(nums) - 1
 
-while i < j:
+    while i < j:
 
-if nums[i] + nums[j] <= T:
-count += j - i 
-i += 1
+        if nums[i] + nums[j] <= T:
+            count += j - i
+            i += 1
 
-else:
-j -= 1
+        else:
+            j -= 1
 
-return count
+            return count
 
 
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 | 
 3 | count = 0
 4 | i = 0
 5 | j = len(nums) - 1
 6 | 
 7 | while i < j:
 8 | 
 9 | if nums[i] + nums[j] <= T:
10 | count += j - i 
11 | i += 1
12 | 
13 | else:
14 | j -= 1
15 | 
16 | return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 | 
 3 |     count = 0
 4 |     i = 0
 5 |     j = len(nums) - 1
 6 | 
 7 |     while i < j:
 8 | 
 9 |         if nums[i] + nums[j] <= T:
10 |             count += j - i
11 |             i += 1
12 | 
13 |         else:
14 |             j -= 1
15 | 
16 |             return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 4.55/20  (5/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01077893 — Kevin Yang

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01077893

| Tag | Change |
|---|---|
| [syntax-only] | stripped trailing prose after last `}` |
| [syntax-only] | added missing semicolons (1 line(s)) |
| [ambiguous] | wrapped code in method signature `maxValidWindowSum(int[] nums, int k)` |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,4 @@
+public class Solution {
+    public static int maxValidWindowSum(int[] nums, int k) {
 int n = nums.length; int windowSum = 0; int negativeCount = 0;int maxSum = 0;
 boolean foundValid = false;
@@ -26,5 +28,6 @@
 }
 if(foundValid){
-return maxSum
+return maxSum;
 }
-return 0;
+    }
+}
```

</details>

**Raw extracted input:**

```
 1 | int n = nums.length; int windowSum = 0; int negativeCount = 0;int maxSum = 0;
 2 | boolean foundValid = false;
 3 | for (int i = 0; i < k; i++) {
 4 | windowSum += nums[i];
 5 |  if (nums[i] < 0) {
 6 | negativeCount++;
 7 | }
 8 | }
 9 | if (negativeCount <= 1) {
10 | maxSum = windowSum;
11 |  foundValid = true;
12 | }
13 | for (int i = k; i < n; i++) {
14 | windowSum += nums[i];
15 | if (nums[i] < 0) {
16 | negativeCount++;
17 | }
18 | windowSum -= nums[i - k];
19 | if (nums[i - k] < 0) {
20 | negativeCount--;
21 | }
22 |  if (negativeCount <= 1) {
23 | maxSum = Math.max(maxSum, windowSum);
24 | foundValid = true;
25 | }
26 | }
27 | if(foundValid){
28 | return maxSum
29 | }
30 | return 0;
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 |     public static int maxValidWindowSum(int[] nums, int k) {
 3 | int n = nums.length; int windowSum = 0; int negativeCount = 0;int maxSum = 0;
 4 | boolean foundValid = false;
 5 | for (int i = 0; i < k; i++) {
 6 | windowSum += nums[i];
 7 |  if (nums[i] < 0) {
 8 | negativeCount++;
 9 | }
10 | }
11 | if (negativeCount <= 1) {
12 | maxSum = windowSum;
13 |  foundValid = true;
14 | }
15 | for (int i = k; i < n; i++) {
16 | windowSum += nums[i];
17 | if (nums[i] < 0) {
18 | negativeCount++;
19 | }
20 | windowSum -= nums[i - k];
21 | if (nums[i - k] < 0) {
22 | negativeCount--;
23 | }
24 |  if (negativeCount <= 1) {
25 | maxSum = Math.max(maxSum, windowSum);
26 | foundValid = true;
27 | }
28 | }
29 | if(foundValid){
30 | return maxSum;
31 | }
32 |     }
33 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01077893

| Tag | Change |
|---|---|
| [syntax-only] | stripped trailing prose after last `}` |
| [ambiguous] | wrapped code in method signature `countPairs(int[] nums, int T)` |
| [logic-affecting] | added fallback `return 0;` (no return statement found) |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,4 @@
+public class Solution {
+    public static int countPairs(int[] nums, int T) {
 int left = 0;  int right = nums.length - 1; int count = 0;
 while (left < right) {
@@ -9,3 +11,5 @@
 }
 }
-return count;
+        return 0;
+}
+}
```

</details>

**Raw extracted input:**

```
 1 | int left = 0;  int right = nums.length - 1; int count = 0;
 2 | while (left < right) {
 3 | int sum = nums[left] + nums[right];
 4 | if (sum <= T) {
 5 | count += (right - left);
 6 | left++;
 7 | } else {
 8 | right--;
 9 | }
10 | }
11 | return count;
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 |     public static int countPairs(int[] nums, int T) {
 3 | int left = 0;  int right = nums.length - 1; int count = 0;
 4 | while (left < right) {
 5 | int sum = nums[left] + nums[right];
 6 | if (sum <= T) {
 7 | count += (right - left);
 8 | left++;
 9 | } else {
10 | right--;
11 | }
12 | }
13 |         return 0;
14 | }
15 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0/20  (0/0 tests passed)  — load error: compile error: C:\Users\danz3\AppData\Local\Temp\jgrade_B01077893_jax08304\Solution.java:32: error: missing return state
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01126505 — Carson Carey

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01126505

| Tag | Change |
|---|---|
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int maxValidWindowSum(int[] nums, int k) {
    int l = 0;
@@ -10,5 +11,5 @@
          negative++;
    }
-   
+
    if(r-l+1>k) {
       if(nums[l]<0)
@@ -18,8 +19,9 @@
 }
 
-if(r-l+1 == k && negative <=1) 
+if(r-l+1 == k && negative <=1)
    max = Math.max(max, windowsum);
-   
-   
+
+
    return max;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) {
 2 |    int l = 0;
 3 |    int windowsum = 0;
 4 |    int negative = 0;
 5 |    int max = 0;
 6 | 
 7 |    for(int r = 0; r<nums.length; r++) {
 8 |       windowsum+=nums[r];
 9 |       if(nums[r]<0)
10 |          negative++;
11 |    }
12 |    
13 |    if(r-l+1>k) {
14 |       if(nums[l]<0)
15 |          negative--;
16 |       windowsum -= nums[l];
17 |       l++;
18 | }
19 | 
20 | if(r-l+1 == k && negative <=1) 
21 |    max = Math.max(max, windowsum);
22 |    
23 |    
24 |    return max;
25 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int maxValidWindowSum(int[] nums, int k) {
 3 |    int l = 0;
 4 |    int windowsum = 0;
 5 |    int negative = 0;
 6 |    int max = 0;
 7 | 
 8 |    for(int r = 0; r<nums.length; r++) {
 9 |       windowsum+=nums[r];
10 |       if(nums[r]<0)
11 |          negative++;
12 |    }
13 | 
14 |    if(r-l+1>k) {
15 |       if(nums[l]<0)
16 |          negative--;
17 |       windowsum -= nums[l];
18 |       l++;
19 | }
20 | 
21 | if(r-l+1 == k && negative <=1)
22 |    max = Math.max(max, windowsum);
23 | 
24 | 
25 |    return max;
26 | }
27 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01126505

| Tag | Change |
|---|---|
| [logic-affecting] | added fallback `return 0;` (no return statement found) |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
     int l = 0;
@@ -12,3 +13,5 @@
             r--;
     }
+    return 0;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 |     int l = 0;
 3 |     int r = nums.length-1;
 4 |     int count = 0;
 5 | 
 6 |     while(l>r) {
 7 |         if(nums[l]+nums[r]<=T) {
 8 |             count += (r-l);
 9 |             l++;
10 |         }
11 |         else
12 |             r--;
13 |     }
14 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 |     int l = 0;
 4 |     int r = nums.length-1;
 5 |     int count = 0;
 6 | 
 7 |     while(l>r) {
 8 |         if(nums[l]+nums[r]<=T) {
 9 |             count += (r-l);
10 |             l++;
11 |         }
12 |         else
13 |             r--;
14 |     }
15 |     return 0;
16 | }
17 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0/20  (0/0 tests passed)  — load error: compile error: C:\Users\danz3\AppData\Local\Temp\jgrade_B01126505_ro3968jl\Solution.java:14: error: cannot find symbol
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01143435 — Qianjun Zhou

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01143435

| Tag | Change |
|---|---|
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,5 +1,6 @@
-returnable = -inf
-for i in range(len(nums) - k):
-if nums[i] + nums[i+1] + nums[i+2] > returnable:
-returnable = nums[i] + nums[i+1] + nums[i+2]
-return returnable
+def max_valid_window_sum(nums, k):
+    returnable = -inf
+    for i in range(len(nums) - k):
+        if nums[i] + nums[i+1] + nums[i+2] > returnable:
+            returnable = nums[i] + nums[i+1] + nums[i+2]
+            return returnable
```

</details>

**Raw extracted input:**

```
1 | returnable = -inf
2 | for i in range(len(nums) - k):
3 | if nums[i] + nums[i+1] + nums[i+2] > returnable:
4 | returnable = nums[i] + nums[i+1] + nums[i+2]
5 | return returnable
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     returnable = -inf
3 |     for i in range(len(nums) - k):
4 |         if nums[i] + nums[i+1] + nums[i+2] > returnable:
5 |             returnable = nums[i] + nums[i+1] + nums[i+2]
6 |             return returnable
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01143435

| Tag | Change |
|---|---|
| [syntax-only] | line 8: added missing colon |
| [ambiguous] | wrapped bare code in `def count_pairs(nums, T)` |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def count_pairs(nums, T): return 0` |
| [syntax-only] | parse error before force-runnable fallback: cannot assign to expression here. Maybe you meant '==' instead of '='? (line 6) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,11 +1,2 @@
-start = 0
-end = len(nums) - 1
-returnable = 0
-while start < end:
-if start + end = value:
-returnable++
-end--
-else
-start++
-
-return returnable
+def count_pairs(nums, T):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | start = 0
 2 | end = len(nums) - 1
 3 | returnable = 0
 4 | while start < end:
 5 | if start + end = value:
 6 | returnable++
 7 | end--
 8 | else
 9 | start++
10 | 
11 | return returnable
```

**Fixed input:**

```
1 | def count_pairs(nums, T):
2 |     return 0
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 3.64/20  (4/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01077715 — Hewitt Wang

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 2

**Diff:**

# Diff for B01077715

| Tag | Change |
|---|---|
| [syntax-only] | no changes required (parsed as-is) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(no textual difference)_

</details>

**Raw extracted input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     def ws(w):
3 |         negatives = sum(1 for x in w if x < 0)
4 |         return 0 if negatives > 1 else sum(w)
5 | 
6 |     windows = (nums[i:i+k+1] for i in range(len(nums) - k))
7 |     return max(map(ws, windows), default=float('-inf'))
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     def ws(w):
3 |         negatives = sum(1 for x in w if x < 0)
4 |         return 0 if negatives > 1 else sum(w)
5 | 
6 |     windows = (nums[i:i+k+1] for i in range(len(nums) - k))
7 |     return max(map(ws, windows), default=float('-inf'))
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 2

**Diff:**

# Diff for B01077715

| Tag | Change |
|---|---|
| [syntax-only] | line 12: added missing colon |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,15 +1,14 @@
 def count_pairs(nums, T):
-   l = 0
-   r = len(nums) - 1
-   c = 0
-   while nums[r] > T:
-      if r <= l: break
-      r -= 1
-   while l < r:
-      if nums[l] + nums[r] <= T:
-         c += r - l
-         l += 1
-      else
-         r -= 1
-    return c
-   
+    l = 0
+    r = len(nums) - 1
+    c = 0
+    while nums[r] > T:
+        if r <= l: break
+        r -= 1
+        while l < r:
+            if nums[l] + nums[r] <= T:
+                c += r - l
+                l += 1
+            else:
+                r -= 1
+                return c
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |    l = 0
 3 |    r = len(nums) - 1
 4 |    c = 0
 5 |    while nums[r] > T:
 6 |       if r <= l: break
 7 |       r -= 1
 8 |    while l < r:
 9 |       if nums[l] + nums[r] <= T:
10 |          c += r - l
11 |          l += 1
12 |       else
13 |          r -= 1
14 |     return c
15 |    
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     l = 0
 3 |     r = len(nums) - 1
 4 |     c = 0
 5 |     while nums[r] > T:
 6 |         if r <= l: break
 7 |         r -= 1
 8 |         while l < r:
 9 |             if nums[l] + nums[r] <= T:
10 |                 c += r - l
11 |                 l += 1
12 |             else:
13 |                 r -= 1
14 |                 return c
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `python`
- **status:** `needs-manual-review`

**Raw bonus code:**

```
 1 | class Solution:
 2 |     def minimumDistance(self, nums: List[int]) -> int:
 3 |         if len(nums) < 3:
 4 |             return -1
 5 |         mn = -1
 6 | 
 7 |         dist = {}
 8 |         
 9 |         for i, val in enumerate(nums):
10 |             if val in dist:
11 |                 dist[val].append(i)
12 |             else:
13 |                 dist[val] = [i]
14 |         
15 |             
16 |         for key, val in dist.items():
17 |             if len(val) < 3:
18 |                 continue
19 |             i = 0
20 |             i1 = 2
21 | 
22 |             while (i1 < len(val)):
23 |                 tmp = 2*(val[i1] - val[i])
24 |                 if tmp < mn or mn == -1:
25 |                     mn = tmp
26 |                 i+=1
27 |                 i1+=1
28 |           
29 |         return mn
30 | 
31 | problem:
32 | https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii
33 | 
34 | explanation:
35 | the solution is O(n). it does two big passes over collections with size <= n, all linear. the indices i, j, k monotonically increase, so we can simplify the distance calculation like follows:
36 |  abs(i - j) + abs(j - k) + abs(k - i)
37 |  j - i + k - j + k - i
38 |  - i - i + k + k
39 |  2(k-i)
40 | 
41 |  we remove the dependency on j, so we no longer have to perform a naive search on i, j, and k. to satisfy the condition of nums[i] == nums[j] == nums[k], we reform the statement as 'nums[i] == nums[j] and there exists a j such that i /= j /= k and nums[j] == nums[i], in other words, if nums[i] and nums[j] == 1, there must be one other 1 <=> there must be at least 3 ones. our dict tracks the indices, and implicity the amount of each number that exists in our array.
```

## Score Summary

- **Problem 1:** 2.4/20  (3/25 tests passed)
- **Problem 2:** 0.91/20  (1/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01063375 — Nicholas Friedlander

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01063375

| Tag | Change |
|---|---|
| [syntax-only] | typo `\btrue\b` -> `True` (2x) |
| [syntax-only] | typo `\bfalse\b` -> `False` (1x) |
| [ambiguous] | wrapped bare code in `def max_valid_window_sum(nums, k)` |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | replaced unparseable code with stub `def max_valid_window_sum(nums, k): return 0` |
| [syntax-only] | parse error before force-runnable fallback: invalid syntax (line 4) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,29 +1,2 @@
-Psuedocode
-
-Function max_valid_window_sum(nums, k):
-    initialize integer window_sum to 0
-    initialize integer negative_counter to 0
-    initialize integer max_sum to 0
-    initialize boolean found to false  
-    
-    For i starting at zero for length of nums - 1:
-    Add nums[i] to window_sum
-    If nums[i] is less than zero:
-        Increment negative_counter by 1
-    
-    If i is greater than k - 1:
-        If negative_counter is less than/equal to 1:
-            If found is False || window_sum is greater than max_sum:
-                set max_sum to window_sum
-                set found to true
-        Subtract nums[i - k + 1] from window_sum
-        If nums[i - k + 1] is less than zero:
-            Increment negative_counter by -1
-
-    If found is true:
-        return max_sum
-
-    Else:
-        return zero
-
-
+def max_valid_window_sum(nums, k):
+    return 0
```

</details>

**Raw extracted input:**

```
 1 | Psuedocode
 2 | 
 3 | Function max_valid_window_sum(nums, k):
 4 |     initialize integer window_sum to 0
 5 |     initialize integer negative_counter to 0
 6 |     initialize integer max_sum to 0
 7 |     initialize boolean found to false  
 8 |     
 9 |     For i starting at zero for length of nums - 1:
10 |     Add nums[i] to window_sum
11 |     If nums[i] is less than zero:
12 |         Increment negative_counter by 1
13 |     
14 |     If i is greater than k - 1:
15 |         If negative_counter is less than/equal to 1:
16 |             If found is False || window_sum is greater than max_sum:
17 |                 set max_sum to window_sum
18 |                 set found to true
19 |         Subtract nums[i - k + 1] from window_sum
20 |         If nums[i - k + 1] is less than zero:
21 |             Increment negative_counter by -1
22 | 
23 |     If found is true:
24 |         return max_sum
25 | 
26 |     Else:
27 |         return zero
```

**Fixed input:**

```
1 | def max_valid_window_sum(nums, k):
2 |     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `pseudocode`
- **status:** `pseudocode`
- **attempt #:** 1

**Diff:**

_(no diff file)_

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,17 +0,0 @@
-Psuedocode
-
-Function count_pairs(nums, T):
-    initialize integer left to 0
-    initialize integer right to length of nums - 1
-    initialize integer counter to 0
-
-    While left < right
-
-        If nums[left] + nums[right] is <= T
-            Add (right - left) to counter
-            Increment left by 1
-
-        Else:
-            Increment right by -1
- 
-    return count
```

</details>

**Raw extracted input:**

```
 1 | Psuedocode
 2 | 
 3 | Function count_pairs(nums, T):
 4 |     initialize integer left to 0
 5 |     initialize integer right to length of nums - 1
 6 |     initialize integer counter to 0
 7 | 
 8 |     While left < right
 9 | 
10 |         If nums[left] + nums[right] is <= T
11 |             Add (right - left) to counter
12 |             Increment left by 1
13 | 
14 |         Else:
15 |             Increment right by -1
16 |  
17 |     return count
```

**Fixed input:**

_(empty)_

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 3.2/20  (4/25 tests passed)
- **Problem 2:** no results
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B00993732 — Christian Zuniga

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B00993732

| Tag | Change |
|---|---|
| [syntax-only] | converted `//` line comments to `#` (2 lines) |
| [syntax-only] | line 1: added missing colon |
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |
| [logic-affecting] | inserted `pass` into empty block at line 17 |
| [syntax-only] | parse error before force-runnable fallback: expected an indented block after 'if' statement on line 17 (line 21) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,21 +1,22 @@
-def max_valid_window_sum(nums, k)
-                left = 0
-                right = len(nums) - 1
-                num_negative = 0
-                window_sum = 0
-                final_sum = 0
+def max_valid_window_sum(nums, k):
+    left = 0
+    right = len(nums) - 1
+    num_negative = 0
+    window_sum = 0
+    final_sum = 0
 
-               while left < right:
-                        if num[r] < 0:
-                                 num_negative += 1
-   
-                        if r - l + 1> k:
-                                 window_sum -= nums[1] //Reduce size of array
-                                 left += 1
-                       //Valid window
-                        if r-l + 1 == k:
-                                 if num_negative <= 1:  
+    while left < right:
+        if num[r] < 0:
+            num_negative += 1
 
-                        
+            if r - l + 1> k:
+                window_sum -= nums[1] # Reduce size of array
+                left += 1
+                # Valid window
+                if r-l + 1 == k:
+                    if num_negative <= 1:
+                        pass
 
-                 
+
+
+
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k)
 2 |                 left = 0
 3 |                 right = len(nums) - 1
 4 |                 num_negative = 0
 5 |                 window_sum = 0
 6 |                 final_sum = 0
 7 | 
 8 |                while left < right:
 9 |                         if num[r] < 0:
10 |                                  num_negative += 1
11 |    
12 |                         if r - l + 1> k:
13 |                                  window_sum -= nums[1] //Reduce size of array
14 |                                  left += 1
15 |                        //Valid window
16 |                         if r-l + 1 == k:
17 |                                  if num_negative <= 1:  
18 | 
19 |                         
20 | 
21 |                  
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     left = 0
 3 |     right = len(nums) - 1
 4 |     num_negative = 0
 5 |     window_sum = 0
 6 |     final_sum = 0
 7 | 
 8 |     while left < right:
 9 |         if num[r] < 0:
10 |             num_negative += 1
11 | 
12 |             if r - l + 1> k:
13 |                 window_sum -= nums[1] # Reduce size of array
14 |                 left += 1
15 |                 # Valid window
16 |                 if r-l + 1 == k:
17 |                     if num_negative <= 1:
18 |                         pass
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `empty`
- **status:** `empty`
- **attempt #:** 1

**Diff:**

_(no diff file)_

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

_(empty)_

</details>

**Raw extracted input:**

_(empty)_

**Fixed input:**

_(empty)_

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** no results
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01061084 — Ava Attina

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01061084

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -2,31 +2,30 @@
 
 def max_valid_window_sum(nums, k):
- sum = 0
+    sum = 0
 
-count = 0
-maxSum = 0
-arraySize = len(nums)
+    count = 0
+    maxSum = 0
+    arraySize = len(nums)
 
- for i in range(k):
-  sum += nums[i]
-   if nums[i] < 0:
-    count += 1
+    for i in range(k):
+        sum += nums[i]
+        if nums[i] < 0:
+            count += 1
 
- if count <= 1:
-  maxSum = sum
+            if count <= 1:
+                maxSum = sum
 
- for i in range(k, arraySize):
-  maxSum += nums[i]
-  if nums[i] < 0:
-    count += 1
-  if nums[i-k] < 0:
-    count -= 1
-  sum -= nums[i-k]
+                for i in range(k, arraySize):
+                    maxSum += nums[i]
+                    if nums[i] < 0:
+                        count += 1
+                        if nums[i-k] < 0:
+                            count -= 1
+                            sum -= nums[i-k]
 
-  if count <= 1:
-    sum = max(maxSum, sum)
-return maxSum
-  
-  if count > 1:
-    return 0
-    
+                            if count <= 1:
+                                sum = max(maxSum, sum)
+                                return maxSum
+
+                                if count > 1:
+                                    return 0
```

</details>

**Raw extracted input:**

```
 1 | #A valid window of size k is a contiguous subarray of length k that contains at most one negative number. Return the maximum sum among all valid windows.
 2 | 
 3 | def max_valid_window_sum(nums, k):
 4 |  sum = 0
 5 | 
 6 | count = 0
 7 | maxSum = 0
 8 | arraySize = len(nums)
 9 | 
10 |  for i in range(k):
11 |   sum += nums[i]
12 |    if nums[i] < 0:
13 |     count += 1
14 | 
15 |  if count <= 1:
16 |   maxSum = sum
17 | 
18 |  for i in range(k, arraySize):
19 |   maxSum += nums[i]
20 |   if nums[i] < 0:
21 |     count += 1
22 |   if nums[i-k] < 0:
23 |     count -= 1
24 |   sum -= nums[i-k]
25 | 
26 |   if count <= 1:
27 |     sum = max(maxSum, sum)
28 | return maxSum
29 |   
30 |   if count > 1:
31 |     return 0
32 |     
```

**Fixed input:**

```
 1 | #A valid window of size k is a contiguous subarray of length k that contains at most one negative number. Return the maximum sum among all valid windows.
 2 | 
 3 | def max_valid_window_sum(nums, k):
 4 |     sum = 0
 5 | 
 6 |     count = 0
 7 |     maxSum = 0
 8 |     arraySize = len(nums)
 9 | 
10 |     for i in range(k):
11 |         sum += nums[i]
12 |         if nums[i] < 0:
13 |             count += 1
14 | 
15 |             if count <= 1:
16 |                 maxSum = sum
17 | 
18 |                 for i in range(k, arraySize):
19 |                     maxSum += nums[i]
20 |                     if nums[i] < 0:
21 |                         count += 1
22 |                         if nums[i-k] < 0:
23 |                             count -= 1
24 |                             sum -= nums[i-k]
25 | 
26 |                             if count <= 1:
27 |                                 sum = max(maxSum, sum)
28 |                                 return maxSum
29 | 
30 |                                 if count > 1:
31 |                                     return 0
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01061084

| Tag | Change |
|---|---|
| [syntax-only] | line 8: added missing colon |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -6,5 +6,5 @@
 while j >= i:
  j -= 1
-else
+else:
   pairs = nums[i] + nums[j]
   while pairs <= T:
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |  count = 0
 3 |  i = 0
 4 |  j = len(nums) - 1
 5 |  
 6 | while j >= i:
 7 |  j -= 1
 8 | else
 9 |   pairs = nums[i] + nums[j]
10 |   while pairs <= T:
11 |     count += (j - i)
12 |     i += 1
13 | 
14 | return count
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |  count = 0
 3 |  i = 0
 4 |  j = len(nums) - 1
 5 |  
 6 | while j >= i:
 7 |  j -= 1
 8 | else:
 9 |   pairs = nums[i] + nums[j]
10 |   while pairs <= T:
11 |     count += (j - i)
12 |     i += 1
13 | 
14 | return count
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 0/20  (0/0 tests passed)  — load error: Traceback (most recent call last):
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01062784 — Michael DiNapoli

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `python`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01062784

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,26 +1,25 @@
 def max_valid_window_sum(nums, k):
-     currentVal = 0
-     max = 0
-     negNums = 0
+    currentVal = 0
+    max = 0
+    negNums = 0
 
-     for i in range(k):
-           currentVal += nums[i]
-           if nums[i] < 0:
-                 negNums += 1
-      if negNums <= 1:
-           max = currentVal
+    for i in range(k):
+        currentVal += nums[i]
+        if nums[i] < 0:
+            negNums += 1
+    if negNums <= 1:
+        max = currentVal
 
-      for i in range(k, len(nums)):
-           currentVal -= nums[i-k]
-           if nums[i-k]<0:
-                 negNums -=1
-           currentVal += nums[i]
-           if nums[i] < 0:
-                  negNums += 1
-           if negNums <= 1 and cuurentVal > max:
-                  max = currentVal
+    for i in range(k, len(nums)):
+        currentVal -= nums[i-k]
+        if nums[i-k]<0:
+            negNums -=1
+        currentVal += nums[i]
+        if nums[i] < 0:
+            negNums += 1
+        if negNums <= 1 and cuurentVal > max:
+            max = currentVal
 
-          
 
-     
-     
+
+
```

</details>

**Raw extracted input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |      currentVal = 0
 3 |      max = 0
 4 |      negNums = 0
 5 | 
 6 |      for i in range(k):
 7 |            currentVal += nums[i]
 8 |            if nums[i] < 0:
 9 |                  negNums += 1
10 |       if negNums <= 1:
11 |            max = currentVal
12 | 
13 |       for i in range(k, len(nums)):
14 |            currentVal -= nums[i-k]
15 |            if nums[i-k]<0:
16 |                  negNums -=1
17 |            currentVal += nums[i]
18 |            if nums[i] < 0:
19 |                   negNums += 1
20 |            if negNums <= 1 and cuurentVal > max:
21 |                   max = currentVal
22 | 
23 |           
24 | 
25 |      
26 |      
```

**Fixed input:**

```
 1 | def max_valid_window_sum(nums, k):
 2 |     currentVal = 0
 3 |     max = 0
 4 |     negNums = 0
 5 | 
 6 |     for i in range(k):
 7 |         currentVal += nums[i]
 8 |         if nums[i] < 0:
 9 |             negNums += 1
10 |     if negNums <= 1:
11 |         max = currentVal
12 | 
13 |     for i in range(k, len(nums)):
14 |         currentVal -= nums[i-k]
15 |         if nums[i-k]<0:
16 |             negNums -=1
17 |         currentVal += nums[i]
18 |         if nums[i] < 0:
19 |             negNums += 1
20 |         if negNums <= 1 and cuurentVal > max:
21 |             max = currentVal
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `python`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01062784

| Tag | Change |
|---|---|
| [syntax-only] | conservative re-indent (cluster nearby indent levels to 4-space tiers) |
| [ambiguous] | aggressive re-indent: rebuilt block structure from control-flow headers |

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,10 +1,10 @@
 def count_pairs(nums, T):
-     l = 0
-     r = len(nums) - 1 
-     num = 0 
-     while l < r:
-           if nums[l] + nums[r] <= T:
-           num += (r - l)
-           l += 1
-     else:
-           r-= 1
+    l = 0
+    r = len(nums) - 1
+    num = 0
+    while l < r:
+        if nums[l] + nums[r] <= T:
+            num += (r - l)
+            l += 1
+        else:
+            r-= 1
```

</details>

**Raw extracted input:**

```
 1 | def count_pairs(nums, T):
 2 |      l = 0
 3 |      r = len(nums) - 1 
 4 |      num = 0 
 5 |      while l < r:
 6 |            if nums[l] + nums[r] <= T:
 7 |            num += (r - l)
 8 |            l += 1
 9 |      else:
10 |            r-= 1
```

**Fixed input:**

```
 1 | def count_pairs(nums, T):
 2 |     l = 0
 3 |     r = len(nums) - 1
 4 |     num = 0
 5 |     while l < r:
 6 |         if nums[l] + nums[r] <= T:
 7 |             num += (r - l)
 8 |             l += 1
 9 |         else:
10 |             r-= 1
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0.0/20  (0/25 tests passed)
- **Problem 2:** 0.0/20  (0/22 tests passed)
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01069659 — Kristen Lee

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01069659

| Tag | Change |
|---|---|
| [syntax-only] | prepended 1 opening brace(s) `{` to balance |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,4 @@
+public class Solution {
+{
 public static int maxValidWindowSum(int[] nums, int k) {
     int sum = 0;
@@ -26,2 +28,3 @@
     return max;
 }
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int maxValidWindowSum(int[] nums, int k) {
 2 |     int sum = 0;
 3 |     int neg = 0;
 4 |     int max = 0;
 5 |     for(int i = 0; i<k; i++){
 6 |         sum += nums[i];
 7 |         if(nums[i]<0){
 8 |             neg++;
 9 |         }
10 |     }
11 |     if(neg<=1){
12 |         max = sum;
13 |     }
14 |     for(int i = 1; i<nums.length-k; i++){
15 |         sum = sum + nums[i+k-1] - nums[i-1];
16 |         if(nums[i+k-1] < 0){
17 |             neg++;
18 |         }
19 |         if(nums[i-1] < 0){
20 |             neg--;
21 |         }
22 |         if(neg<=1 && sum>max)
23 |             max = sum;
24 |         }
25 |     }
26 |     return max;
27 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | {
 3 | public static int maxValidWindowSum(int[] nums, int k) {
 4 |     int sum = 0;
 5 |     int neg = 0;
 6 |     int max = 0;
 7 |     for(int i = 0; i<k; i++){
 8 |         sum += nums[i];
 9 |         if(nums[i]<0){
10 |             neg++;
11 |         }
12 |     }
13 |     if(neg<=1){
14 |         max = sum;
15 |     }
16 |     for(int i = 1; i<nums.length-k; i++){
17 |         sum = sum + nums[i+k-1] - nums[i-1];
18 |         if(nums[i+k-1] < 0){
19 |             neg++;
20 |         }
21 |         if(nums[i-1] < 0){
22 |             neg--;
23 |         }
24 |         if(neg<=1 && sum>max)
25 |             max = sum;
26 |         }
27 |     }
28 |     return max;
29 | }
30 | }
```

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `repaired`
- **attempt #:** 1

**Diff:**

# Diff for B01069659

| Tag | Change |
|---|---|
| [syntax-only] | appended 1 missing closing brace(s) `}` |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,2 +1,3 @@
+public class Solution {
 public static int countPairs(int[] nums, int T) {
     int count = 0;
@@ -12,2 +13,4 @@
     return count;
 }
+}
+}
```

</details>

**Raw extracted input:**

```
 1 | public static int countPairs(int[] nums, int T) {
 2 |     int count = 0;
 3 |     int i = 0;
 4 |     int j = nums.length-1;
 5 |     while(i<j){
 6 |         if(nums[i]+nums[j] <=T){
 7 |             count += j-i;
 8 |             i++;
 9 |         }else{
10 |             j--;
11 |         }
12 |     return count;
13 | }
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 | public static int countPairs(int[] nums, int T) {
 3 |     int count = 0;
 4 |     int i = 0;
 5 |     int j = nums.length-1;
 6 |     while(i<j){
 7 |         if(nums[i]+nums[j] <=T){
 8 |             count += j-i;
 9 |             i++;
10 |         }else{
11 |             j--;
12 |         }
13 |     return count;
14 | }
15 | }
16 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `empty`
- **status:** `empty`

**Raw bonus code:**

_(empty)_

## Score Summary

- **Problem 1:** 0/20  (0/0 tests passed)  — load error: compile error: C:\Users\danz3\AppData\Local\Temp\jgrade_B01069659_6ebbque5\Solution.java:3: error: illegal start of expr
- **Problem 2:** 0/20  (0/0 tests passed)  — load error: compile error: C:\Users\danz3\AppData\Local\Temp\jgrade_B01069659_5jmxa7wa\Solution.java:15: error: missing return state
- **Problem 3:** manual grade (LeetCode POTD varies per student)

====================================================================================================

# B01150044 — Zhi Xiong Lu

## Problem 1 — Maximum Valid Window Sum

- **detected language:** `pseudocode`
- **status:** `pseudocode`
- **attempt #:** 1

**Diff:**

_(no diff file)_

<details><summary><b>Highlighted changes raw → fixed (click to expand)</b></summary>

```diff
--- raw
+++ fixed
@@ -1,17 +0,0 @@
-set left to 0
-set sum to 0
-set negativecount to 0
-set maxsum to 0
-
-loop from 0 until the end of the array
-
-sum = nums(right) + sum
-
-if nums(right) < 0
-negativecount = negativecount + 1
-
-if right - left + 1 > k
-
-sun = sum - nums(left)
-
-
```

</details>

**Raw extracted input:**

```
 1 | set left to 0
 2 | set sum to 0
 3 | set negativecount to 0
 4 | set maxsum to 0
 5 | 
 6 | loop from 0 until the end of the array
 7 | 
 8 | sum = nums(right) + sum
 9 | 
10 | if nums(right) < 0
11 | negativecount = negativecount + 1
12 | 
13 | if right - left + 1 > k
14 | 
15 | sun = sum - nums(left)
```

**Fixed input:**

_(empty)_

## Problem 2 — Count Valid Pairs With Constraint

- **detected language:** `java`
- **status:** `needs-manual-review`
- **attempt #:** 1

**Diff:**

# Diff for B01150044

| Tag | Change |
|---|---|
| [syntax-only] | stripped 4 leading prose line(s) |
| [syntax-only] | added missing semicolons (3 line(s)) |
| [ambiguous] | wrapped code in method signature `countPairs(int[] nums, int T)` |
| [logic-affecting] | added fallback `return 0;` (no return statement found) |
| [syntax-only] | wrapped in `public class Solution { ... }` |

<details><summary><b>Highlighted changes raw → java (repaired) (click to expand)</b></summary>

```diff
--- raw
+++ java (repaired)
@@ -1,14 +1,15 @@
-set i to 0
-set j = length of nums - 1
-set c to 0
-
+public class Solution {
+    public static int countPairs(int[] nums, int T) {
 while i < j;
 
 if nums[i] + nums[j] <= T
 
-add (j-i) to c
-i + 1
+add (j-i) to c;
+i + 1;
 
 else
 
-j-1
+j-1;
+        return 0;
+}
+}
```

</details>

**Raw extracted input:**

```
 1 | set i to 0
 2 | set j = length of nums - 1
 3 | set c to 0
 4 | 
 5 | while i < j;
 6 | 
 7 | if nums[i] + nums[j] <= T
 8 | 
 9 | add (j-i) to c
10 | i + 1
11 | 
12 | else
13 | 
14 | j-1
```

**Java source (repaired):**

```
 1 | public class Solution {
 2 |     public static int countPairs(int[] nums, int T) {
 3 | while i < j;
 4 | 
 5 | if nums[i] + nums[j] <= T
 6 | 
 7 | add (j-i) to c;
 8 | i + 1;
 9 | 
10 | else
11 | 
12 | j-1;
13 |         return 0;
14 | }
15 | }
```

## Problem 3 — Bonus (LeetCode POTD)

- **detected language:** `pseudocode`
- **status:** `pseudocode`

**Raw bonus code:**

```
1 | asfasfdad
```

## Score Summary

- **Problem 1:** no results
- **Problem 2:** 0/20  (0/0 tests passed)  — load error: compile error: C:\Users\danz3\AppData\Local\Temp\jgrade_B01150044_tnmedph5\Solution.java:3: error: '(' expected
- **Problem 3:** manual grade (LeetCode POTD varies per student)
