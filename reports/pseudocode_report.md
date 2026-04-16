# Pseudocode Submissions

====================================================================================================



====================================================================================================

_Students who submitted pseudocode for Problem 1 and/or Problem 2. These require manual grading._

====================================================================================================



====================================================================================================

# B01075554 — Alison Batz

## Problem 1 — Maximum Valid Window Sum

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

====================================================================================================

# B01150044 — Zhi Xiong Lu

## Problem 1 — Maximum Valid Window Sum

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

====================================================================================================

# B01063375 — Nicholas Friedlander

## Problem 2 — Count Valid Pairs With Constraint

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

====================================================================================================

# B01075554 — Alison Batz

## Problem 2 — Count Valid Pairs With Constraint

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
