# Mock Technical Interview - Grading Report

> Generated 2026-05-19 13:38  
> 75 graded, 27 all-pass, 7 minor errors, 41 critical errors, 0 compile errors after repair

## How to read this report

- **PASS**: all tests pass
- **Minor Error**: right approach, some bugs (>50% tests pass)
- **Critical Error**: wrong approach or major logic bugs (<=50% tests pass), or uncompilable after all repair attempts
- **Repair level**: `lightweight` = basic syntax fixes only; `aggressive` = re-indentation / bracket balancing / force-runnable (flagged changes may affect logic); `java-transpile` = mechanical Java-to-Python conversion

## Summary

| # | Student | Problem | Score | Severity | Optimal | Repair | Failed Tests |
|--:|---------|---------|------:|----------|---------|--------|--------------|
| 1 | Coverdale, Solomon | Contains Nearby Duplicate | 8/8 | PASS | Yes | lightweight |  |
| 2 | Genc, Sude | Contains Nearby Duplicate | 8/8 | PASS | Yes | lightweight |  |
| 3 | Safronov, Danila | Contains Nearby Duplicate | 8/8 | PASS | Yes | lightweight |  |
| 4 | Weisberg, Evan | Contains Nearby Duplicate | 8/8 | PASS | Yes | lightweight |  |
| 5 | Wong, Ethan | Contains Nearby Duplicate | 8/8 | PASS | Yes | lightweight |  |
| 6 | Broderick, Maddie | Contains Nearby Duplicate | 0/8 | Critical Error | Yes | lightweight | true_basic, true_adjacent, false_too_far, false_k_zero, single_element, no_dups, true_exact_k, empty |
| 7 | Chan, Cheong Ting Eland | Contains Nearby Duplicate | 6/8 | Minor Error | Yes | lightweight | true_basic, true_exact_k |
| 8 | Guo, Jason | Contains Nearby Duplicate | 1/8 | Critical Error | Yes | lightweight | true_basic, true_adjacent, false_too_far, false_k_zero, single_element, no_dups, true_exact_k |
| 9 | Lin, Brian | Contains Nearby Duplicate | 5/8 | Minor Error | Yes | aggressive | true_basic, true_adjacent, true_exact_k |
| 10 | Lin, Tiffany | Contains Nearby Duplicate | 4/8 | Critical Error | Yes | lightweight | true_basic, true_adjacent, true_exact_k, empty |
| 11 | McBean, Andrew | Contains Nearby Duplicate | 1/8 | Critical Error | Yes | lightweight | true_basic, true_adjacent, false_too_far, false_k_zero, single_element, no_dups, true_exact_k |
| 12 | Stevens, Jack | Contains Nearby Duplicate | 6/8 | Minor Error | Yes | lightweight | false_too_far, false_k_zero |
| 13 | Carozza, Ashley | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes | lightweight |  |
| 14 | Cheung, Ivan | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes | lightweight |  |
| 15 | Ng, Gavin | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes | lightweight |  |
| 16 | Sellam, Naomi | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes | lightweight |  |
| 17 | Singh, Kushagra | Evaluate Reverse Polish Notation | 7/7 | PASS | Yes | lightweight |  |
| 18 | Attina, Ava | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | aggressive | example1, example2, example3, add_only, single, subtract, neg_divide |
| 19 | Carhart, Sean | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | aggressive | example1, example2, example3, add_only, single, subtract, neg_divide |
| 20 | Godzki, Kyle | Evaluate Reverse Polish Notation | 3/7 | Critical Error | Yes | lightweight | example2, example3, subtract, neg_divide |
| 21 | Mahaman Sani, Abdoul Razakou | Evaluate Reverse Polish Notation | 5/7 | Minor Error | Yes | lightweight | example3, single |
| 22 | Majlis, Mahir | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | aggressive | example1, example2, example3, add_only, single, subtract, neg_divide |
| 23 | Moran, Juan | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | lightweight | example1, example2, example3, add_only, single, subtract, neg_divide |
| 24 | Patel, Ved | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | aggressive | example1, example2, example3, add_only, single, subtract, neg_divide |
| 25 | Regueiferos, Logan | Evaluate Reverse Polish Notation | 6/7 | Minor Error | Yes | lightweight | example3 |
| 26 | Seng, Jason | Evaluate Reverse Polish Notation | 1/7 | Critical Error | Yes | lightweight | example1, example2, example3, add_only, subtract, neg_divide |
| 27 | Stehura, Max | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | lightweight | example1, example2, example3, add_only, single, subtract, neg_divide |
| 28 | Vallarta, Giankyle | Evaluate Reverse Polish Notation | 0/7 | Critical Error | Yes | aggressive | example1, example2, example3, add_only, single, subtract, neg_divide |
| 29 | Wahlin, Kartik | Evaluate Reverse Polish Notation | 3/7 | Critical Error | Yes | lightweight | example2, example3, subtract, neg_divide |
| 30 | Chen, Albert | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 31 | Diusheyeva, Lilia | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 32 | Kukreti, Naman | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 33 | Park, Matthew | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 34 | Rpk, Parks | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 35 | Wang, Hewitt | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 36 | Zhou, Qianjun | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 37 | Zuluaga, Santiago | Guess Number Higher or Lower | 7/7 | PASS | Yes | lightweight |  |
| 38 | Chan, Gaven | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | lightweight | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 39 | Connors, William | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | aggressive | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 40 | Juance, Reginald | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | aggressive | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 41 | Ramos Rodriguez, Jordanny | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | aggressive | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 42 | Yang, Kevin | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | aggressive | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 43 | Yuan, Lilian | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | aggressive | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 44 | Zaidi, Rijaa | Guess Number Higher or Lower | 0/7 | Critical Error | Yes | aggressive | basic, single, pick_low, pick_high, large, mid_range, pick_is_n |
| 45 | Calandra, Clare | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes | lightweight |  |
| 46 | Conroy, William | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes | lightweight |  |
| 47 | Friedlander, Nicholas | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes | lightweight |  |
| 48 | Halsband, Samuel | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes | lightweight |  |
| 49 | Steck, Jake | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes | lightweight |  |
| 50 | Yang, Isabella | Longest Substring Without Repeating Characters | 8/8 | PASS | Yes | lightweight |  |
| 51 | Balkam, Tianna | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | lightweight | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 52 | Carey, Carson | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | aggressive | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 53 | Chen, Shunyi | Longest Substring Without Repeating Characters | 6/8 | Minor Error | Yes | lightweight | example3, spaces |
| 54 | DiNapoli, Michael | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | lightweight | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 55 | Gaston, Justin | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | aggressive | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 56 | Noh, Jin | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | aggressive | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 57 | Thelusma, Treyson | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | lightweight | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 58 | Vega, Dominic | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | aggressive | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 59 | Zhang, Jiarong | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | aggressive | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 60 | Zhang, Ryan | Longest Substring Without Repeating Characters | 7/8 | Minor Error | No - Nested loops instead of sliding window | lightweight | example1 |
| 61 | Zuniga, Christian | Longest Substring Without Repeating Characters | 1/8 | Critical Error | Yes | aggressive | example1, all_same, example3, single_char, all_unique, spaces, end_longest |
| 62 | Calin, Stephania | Merge Two Sorted Lists | 7/7 | PASS | Yes | lightweight |  |
| 63 | Lu, Zhi Xiong | Merge Two Sorted Lists | 7/7 | PASS | Yes | lightweight |  |
| 64 | Tsui, Ryan | Merge Two Sorted Lists | 7/7 | PASS | Yes | lightweight |  |
| 65 | Batz, Alison | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | aggressive | example1, both_empty, one_empty, other_empty, interleave, all_same, single_each |
| 66 | Gnajewski, Monica | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | aggressive | example1, both_empty, one_empty, other_empty, interleave, all_same, single_each |
| 67 | Karamchandani, Varun | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | lightweight | example1, both_empty, one_empty, other_empty, interleave, all_same, single_each |
| 68 | Minhas, Vikram | Merge Two Sorted Lists | 1/7 | Critical Error | Yes | lightweight | example1, both_empty, other_empty, interleave, all_same, single_each |
| 69 | Ng, Kenneth | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | aggressive | example1, both_empty, one_empty, other_empty, interleave, all_same, single_each |
| 70 | Porto, Ian | Merge Two Sorted Lists | 1/7 | Critical Error | Yes | lightweight | example1, both_empty, one_empty, interleave, all_same, single_each |
| 71 | Santhosh, Athulya | Merge Two Sorted Lists | 3/7 | Critical Error | Yes | lightweight | example1, interleave, all_same, single_each |
| 72 | Schauber, Kathryn | Merge Two Sorted Lists | 3/7 | Critical Error | Yes | lightweight | example1, interleave, all_same, single_each |
| 73 | Yang, Gabriel | Merge Two Sorted Lists | 1/7 | Critical Error | Yes | lightweight | example1, one_empty, other_empty, interleave, all_same, single_each |
| 74 | Yu, Justin | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | aggressive | example1, both_empty, one_empty, other_empty, interleave, all_same, single_each |
| 75 | Zheng, Vincent | Merge Two Sorted Lists | 0/7 | Critical Error | Yes | aggressive | example1, both_empty, one_empty, other_empty, interleave, all_same, single_each |

---

## Student Details

### Contains Nearby Duplicate

#### Solomon Coverdale (`77672`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | True | PASS |
| true_adjacent | True | True | PASS |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | True | PASS |
| empty | False | False | PASS |

<details>
<summary>Student Code (77672.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dict = {}
    for i,val in enumerate(nums):
        if val in dict and i-dict[val] <= k:
            return True
        else:
            dict[val] = i

    return False
```

</details>

---

#### Sude Genc (`73748`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | True | PASS |
| true_adjacent | True | True | PASS |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | True | PASS |
| empty | False | False | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Fixed typo -> 'False'

</details>

<details>
<summary>Student Code (73748.py)</summary>

```python
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for i , var in enumerate(nums):
        if var in d and i-d[var] <= k:
            return True
        else:
            d[var]=i
    return False

#time complexity for this solution is O(n). turns list into a dictionary(hashmap), 
#then looped through variables using sliding windows. if satisfies the condition return true
# else add to the dictionary(hashmap) and continue to loop. at the end of the loop if condition
# did not met return false
```

</details>

---

#### Danila Safronov (`78296`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | True | PASS |
| true_adjacent | True | True | PASS |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | True | PASS |
| empty | False | False | PASS |

<details>
<summary>Student Code (78296.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool: 

    seen = {}

    for i, num in enumerate(nums): 
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
```

</details>

---

#### Evan Weisberg (`66281`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | True | PASS |
| true_adjacent | True | True | PASS |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | True | PASS |
| empty | False | False | PASS |

<details>
<summary>Student Code (66281.py)</summary>

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index,n in enumerate(nums):
            if n in d:
                if index-d[n] <= k:
                    return True 
            d[n] = index
        return False
```

</details>

---

#### Ethan Wong (`75870`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | True | PASS |
| true_adjacent | True | True | PASS |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | True | PASS |
| empty | False | False | PASS |

<details>
<summary>Student Code (75870.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: in) -> bool:
    dict = {}

    for key, value in enumerate(nums):
        if value in dict:
            if abs(key - dict[value]) <= k:
                return True
            dict[value] = key
        else:
            dict[value] = key
    
    return False
```

</details>

---

#### Maddie Broderick (`77137`)

- **Severity: Critical Error**
- **Score:** 0/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | ERROR: TypeError: 'int' object is not iterable | FAIL |
| true_adjacent | True | ERROR: TypeError: 'int' object is not iterable | FAIL |
| false_too_far | False | ERROR: TypeError: 'int' object is not iterable | FAIL |
| false_k_zero | False | ERROR: TypeError: 'int' object is not iterable | FAIL |
| single_element | False | ERROR: TypeError: 'int' object is not iterable | FAIL |
| no_dups | False | ERROR: TypeError: 'int' object is not iterable | FAIL |
| true_exact_k | True | ERROR: TypeError: 'int' object is not iterable | FAIL |
| empty | False | ERROR: TypeError: 'int' object is not iterable | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Lowered keyword 'If'

</details>

<details>
<summary>Student Code (77137.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mapp = {}
    j = 0
    for j in len(nums):
        if nums[j] in mapp:
            if j - mapp[nums[j]] <= k:
                return True
        mapp[nums[j]] = j
    return False
        
# Time complexity: O(n) because it runs through the array once
# Solves the problem by running through the list and adding values
# to the hashmap. If the value already exist, it checks if abs(i-j) <= k
```

</details>

---

#### Cheong Ting Eland Chan (`77139`)

- **Severity: Minor Error**
- **Score:** 6/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | False | FAIL |
| true_adjacent | True | True | PASS |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | False | FAIL |
| empty | False | False | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Fixed typo -> 'False'

</details>

<details>
<summary>Student Code (77139.py)</summary>

```python
# the two elements have to be the same
# the difference of the indices of the same element has to be less than or equal to k

#this duplicates 

#hash table 

# O(N)

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_set = {}

    for i, num in enumerate(nums):
        temp = num_set.get(num)
        if temp and abs(temp - i) <= k:
            return true
        
        num_set[num] = i

    return false
```

</details>

---

#### Jason Guo (`79145`)

- **Severity: Critical Error**
- **Score:** 1/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | ERROR: AttributeError: 'set' object has no attr | FAIL |
| true_adjacent | True | ERROR: AttributeError: 'set' object has no attr | FAIL |
| false_too_far | False | ERROR: AttributeError: 'set' object has no attr | FAIL |
| false_k_zero | False | ERROR: AttributeError: 'set' object has no attr | FAIL |
| single_element | False | ERROR: AttributeError: 'set' object has no attr | FAIL |
| no_dups | False | ERROR: AttributeError: 'set' object has no attr | FAIL |
| true_exact_k | True | ERROR: AttributeError: 'set' object has no attr | FAIL |
| empty | False | False | PASS |

<details>
<summary>Student Code (79145.py)</summary>

```python
def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
    s = set()
    d = {}
    
    for i in range(len(nums)):
    
        if nums[i] in s:
            if abs(d[nums[i]] - i) <= k:
                return True
            else:
                d[nums[i]] = i
        else:
            s.append(nums[i]) 
            d[nums[i]] = i
    
    return False
            
# Time complexity is O(n) because set and dictionary lookup is O(1) so only the for loop O(n) applies.
# This solves the problem by creating a set to detect duplicates and the dictionary to keep track of indices. It works by iterating through the array until it finds a duplicate. When it finds a duplicate, it looks up the previous indice with the dictionary and does the abs(i - j) <= k operation to return True or continue if False until it reaches the end of the array.
```

</details>

---

#### Brian Lin (`69560`)

- **Severity: Minor Error**
- **Score:** 5/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | False | FAIL |
| true_adjacent | True | False | FAIL |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | False | FAIL |
| empty | False | False | PASS |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def containsNearbyDuplicate(nums, k): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Replaced && with and
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def containsNearbyDuplicate(nums, k): return 0`

</details>

<details>
<summary>Student Code (69560.java)</summary>

```java
public Boolean containsNearbyDuplicate(int[] nums, int k){


    Map<Integer,Integer> x = new HashMap<>();

    for(int i=0; i<nums.length();i++){
        int val = nums[i];


        if(x.containsValue(val) && i - x.value(i) <= k){
            return true;
        }else{
            x.put(value,i);
        }
    }
    return false;
}
```

</details>

---

#### Tiffany Lin (`78601`)

- **Severity: Critical Error**
- **Score:** 4/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | False | FAIL |
| true_adjacent | True | False | FAIL |
| false_too_far | False | False | PASS |
| false_k_zero | False | False | PASS |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | False | FAIL |
| empty | False | None | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Fixed typo -> 'False'

</details>

<details>
<summary>Student Code (78601.py)</summary>

```python
def containsNearbyDuplicate(nums:List[int],k:int) --> bool:
    d = {}
    
    for i,j in enumerate(nums):
        if j in d and i - d[j] <= k:
            return true
        else:
            d[j] = i   
            
        return false
```

</details>

---

#### Andrew McBean (`74837`)

- **Severity: Critical Error**
- **Score:** 1/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | ERROR: NameError: name 'unique' is not defined | FAIL |
| true_adjacent | True | ERROR: NameError: name 'unique' is not defined | FAIL |
| false_too_far | False | ERROR: NameError: name 'unique' is not defined | FAIL |
| false_k_zero | False | ERROR: NameError: name 'unique' is not defined | FAIL |
| single_element | False | ERROR: NameError: name 'unique' is not defined | FAIL |
| no_dups | False | ERROR: NameError: name 'unique' is not defined | FAIL |
| true_exact_k | True | ERROR: NameError: name 'unique' is not defined | FAIL |
| empty | False | False | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Student Code (74837.py)</summary>

```python
The time complexity of the code is O(n). The function utilizes a fixed sliding window where both pointers are incremented checking for the condition of whether there are duplicates. To check the duplicates I used a hash map, but a hash set could have also been used to simplify the if statements. It solves the problem by returning True when a duplicate is detected and False if the entire function runs without a return.

def containsNearbyDuplicate(nums: List[int], k:int) -> bool:
    unqique = {}
    for i in range(k):
        if unique.get(num[i], 0) == 0:
            unique[nums[i]] = i
        else:
            return True
    for i in range(k, len(nums)):
        if unique.get(nums[i], 0) == 0:
            unique[nums[i]] = i
        else:
            return True
        dic.remove(nums[i-k])
    return False
```

</details>

---

#### Jack Stevens (`77510`)

- **Severity: Minor Error**
- **Score:** 6/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| true_basic | True | True | PASS |
| true_adjacent | True | True | PASS |
| false_too_far | False | True | FAIL |
| false_k_zero | False | True | FAIL |
| single_element | False | False | PASS |
| no_dups | False | False | PASS |
| true_exact_k | True | True | PASS |
| empty | False | False | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Lowered keyword 'Def'
- [syntax-only] Lowered keyword 'For'
- [syntax-only] Lowered keyword 'If'
- [syntax-only] Lowered keyword 'Return'
- [syntax-only] Replaced em/en dashes with hyphens

</details>

<details>
<summary>Student Code (77510.py)</summary>

```python
#Use a set to hold checked values of the array to compare the current index to the past values #to find duplicates
#I can use the indexes within the set and then add that to the current list length to find the #original list indexes and compare them to K 

Def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        s = {}
        For i in range(len(nums)):
                if nums[i] in s:
                        If(abs(i – s[nums[i]]) <= k):
                                Return True
                s[i] = nums[i]
        return False
```

</details>

---

### Evaluate Reverse Polish Notation

#### Ashley Carozza (`69252`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 22 | PASS |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (69252.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    #create empty stack
    stack = []
    #set of the operations
    operations = {"+", "*", "-", "/"}

    for token in tokens:
        if token in operations:
            #second operand (top of stack)
            b = stack.pop()
            #first operand
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                #truncate toward 0, not floor
                stack.append(int(a / b))
        else:
            #convert string to int and push onto stack
            stack.append(int(token))
    #final result is only element left
    return stack[0]
            
#Approach: I used a stack to process the token from left to right. I push numbers onto the stack, and when an operator is hit, I pop the two operands, apply the operation, 
#and then push the result. The final value left on the stack is the answer.
#Time complexity: The solution is O(n) where n is the number of tokens, since every token is visited exactly once and all stack operations (push/pop) are O(1).m
```

</details>

---

#### Ivan Cheung (`70932`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 22 | PASS |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (70932.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:

    stack = []
    for e in tokens:
        
        if e == "+":
            stack.append(stack.pop() + stack.pop())
        
        elif e == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)

        elif e == "*":
            
            stack.append(stack.pop() * stack.pop())
        
        elif e == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first / second))
        
        else:
            stack.append(int(e))
        
    return stack[0]
```

</details>

---

#### Gavin Ng (`79826`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 22 | PASS |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (79826.py)</summary>

```python
#Gavin Ng
#Noel Maldaro 
#Evaluate Reverse Polish Notation
#Candidate Form


from typing import List 

def evalRPN(tokens: List[str]) -> int:
    sum = 0
    stack = []
 
    for i in range(len(tokens)):
        if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/": #checks if token is an operator
            num2 = stack.pop()#pops the 2 operands
            num1 = stack.pop()
            if tokens[i] == "+": 
                sum = num1 + num2
            elif tokens[i] == "-":
                sum = num1 - num2
            elif tokens[i] == "*":
                sum = num1 * num2
            else:
                sum = int(num1 / num2) #else divides already checked is operator
            stack.append(sum) #push the result back to stack
        else:
            stack.append(int(tokens[i])) #else pushes next token to stack as int

    return stack.pop() #last element would be final answer




print(evalRPN(["2", "1", "+", "3", "*"])) #sol: 9 
print(evalRPN(["4", "13", "5", "/", "+"])) #sol: 6
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) #sol: 22 (did math on paper)
```

</details>

---

#### Naomi Sellam (`79751`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 22 | PASS |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (79751.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    stack = []
    
    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            
            b = stack.pop()  
            a = stack.pop()  
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
        else:
            stack.append(int(token))
    
    return stack[0]
```

</details>

---

#### Kushagra Singh (`75746`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 22 | PASS |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (75746.py)</summary>

```python
from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)
    }
    
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    
    return stack[0]
```

</details>

---

#### Ava Attina (`66963`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 0 | FAIL |
| example2 | 6 | 0 | FAIL |
| example3 | 22 | 0 | FAIL |
| add_only | 7 | 0 | FAIL |
| single | 18 | 0 | FAIL |
| subtract | 2 | 0 | FAIL |
| neg_divide | 3 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Appended 1 missing closing bracket(s)
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Student Code (66963.py)</summary>

```python
def evalPRN(tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            second, first = stack.pop(), stack.pop()
            stack.append(first - second)
        elif i == '*':
            stack.append(stack.pop() * stack.pop()
        elif i == '/':
            second, first = stack.pop(), stack.pop()
            stack.append(int(first/second))
        else:
        
            stack.append(int(i))
        
        return stack[0]
# O(1) time complexity
# Ava Attina
```

</details>

---

#### Sean Carhart (`77764`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 0 | FAIL |
| example2 | 6 | 0 | FAIL |
| example3 | 22 | 0 | FAIL |
| add_only | 7 | 0 | FAIL |
| single | 18 | 0 | FAIL |
| subtract | 2 | 0 | FAIL |
| neg_divide | 3 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Student Code (77764.java)</summary>

```java
public int evalRPN(String[] tokens){
deque<Integer> stack = new deque<>();
for (int i = 0;  i < tokens.length; i++)
{
        String character = tokens[i];
        if(character.equals(“+”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 + num2;
                stack.push(result);
        }
        else if(character.equals(“-”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 - num2;
                stack.push(result);
        }
        else if(character.equals(“*”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 * num2;
                stack.push(result);
        }
        else if(character.equals(“/”))
        {
                int num2 = stack.pop();
                int num1 = stack.pop();
                int result = num1 / num2;
                stack.push(result);
        }
        else
        {
                int num = character.parseInt();
                stack.push(num);
        }
}
return stack.pop();
}
```

</details>

---

#### Kyle Godzki (`67982`)

- **Severity: Critical Error**
- **Score:** 3/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 4 | FAIL |
| example3 | 22 | -198 | FAIL |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | -2 | FAIL |
| neg_divide | 3 | 0 | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Student Code (67982.py)</summary>

```python
#Kyle Godzki
#Ethan Wong

# Stack -> LIFO


def evalRPN(tokens: List[str]) -> int:
        stack = []
        for token in tokens: O(N) # This is the for loop
                if token in '+-*/':
                        a, b = stack.pop(), stack.pop() #O(1) # Pops last two entries in stack
                        if token == '+': stack.append(a + b) # O(1) # Adds last two popped entries, answer entered
                        if token == '-': stack.append(a - b) 
                        if token == '*': stack.append(a * b)
                        if token == '/': stack.append(a / b)
                else:
                        stack.append(int(token))
        return stack[0] # return answer

Final complexity was O(N) since only one for loop and everything else just for loops. Space complexity was O((N/2) + 1) with our added stack.
```

</details>

---

#### Abdoul Razakou Mahaman Sani (`78738`)

- **Severity: Minor Error**
- **Score:** 5/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 12 | FAIL |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | FAIL |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (78738.py)</summary>

```python
def evalRPN(tokens: List[str]):
    stack = []
    operator = ["+","-","*","/"]
    for i in tokens:
        if i not in operator:
            stack.append(i)
        else:
            val1 = int(stack.pop()) 
            val2 = int(stack.pop())
            if i == "/":
                result = val2//val1

            else:
                if i == "+":
                    result = val2+val1
                elif i == "-":
                    result = val2-val1
                elif i == "*":
                    result = val2*val1
            stack.append(result)
    return stack[0]
```

</details>

---

#### Mahir Majlis (`79344`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 0 | FAIL |
| example2 | 6 | 0 | FAIL |
| example3 | 22 | 0 | FAIL |
| add_only | 7 | 0 | FAIL |
| single | 18 | 0 | FAIL |
| subtract | 2 | 0 | FAIL |
| neg_divide | 3 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

<details>
<summary>All syntax changes made</summary>

- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Student Code (79344.py)</summary>

```python
The valid operators are '+', '-', '*', and '/'.
```

</details>

---

#### Juan Moran (`79318`)

- **Severity: Critical Error**
- **Score:** 0/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | ERROR: AttributeError: 'str' object has no attr | FAIL |
| example2 | 6 | ERROR: AttributeError: 'str' object has no attr | FAIL |
| example3 | 22 | ERROR: AttributeError: 'str' object has no attr | FAIL |
| add_only | 7 | ERROR: AttributeError: 'str' object has no attr | FAIL |
| single | 18 | ['18'] | FAIL |
| subtract | 2 | ERROR: AttributeError: 'str' object has no attr | FAIL |
| neg_divide | 3 | ERROR: AttributeError: 'str' object has no attr | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Student Code (79318.py)</summary>

```python
arr = [4,13,5, / , +]
stack = [4,13,5]
term1 = 5 , stack [4,13]
term2 = 13, stack [4]
[4,2]
term1 = 2 , stack = [4]
term2 = 4, stack =[]
stack = [6]

def evalRPN(arr) :
        stack = []
        term1 = ""
        term2 = ""
        for i in range(len(arr)):
                if (len(arr) == 1):
                        return arr
                if arr[i].isDigit():
                        stack.push(arr[i])
                if arr[i] == "*":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term1)*int(term2)
                        stack.push(term2)
                if arr[i] == "/":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term2)/int(term1)
                        stack.push(term2)
                if arr[i] == "+":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term1)+int(term2)
                        stack.push(term2)
                if arr[i] == "-":
                        term1 = stack[-1]
                        stack.pop()
                        term2 = stack[-1]
                        stack.pop()
                        term2 = int(term2)-int(term1)
                        stack.push(term2)
        return stack[-1]
```

</details>

---

#### Ved Patel (`69531`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 0 | FAIL |
| example2 | 6 | 0 | FAIL |
| example3 | 22 | 0 | FAIL |
| add_only | 7 | 0 | FAIL |
| single | 18 | 0 | FAIL |
| subtract | 2 | 0 | FAIL |
| neg_divide | 3 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Replaced || with or
- [syntax-only] Removed trailing semicolons
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Student Code (69531.py)</summary>

```python
def evalRPN(tokens: List[str] -> int): 
    # [4, 13, 5, /, +]

    # Time Complexity O(n)
    # Space Complexity O(n)

    #5
    #13 /  (2)
    #4 +  = 6 

    #13 / 5 = 2.5 = 2   


    #[result] 

    #result
    #result + 5 
    #result + 17
    #result * 10
    #result / 6
    #result * - 11
    #(3 + 9)

    #results = 0
    #l, r = 0, 1

    operations = {}

    if len(tokens) <= 2:
        return tokens[0]

    while(len(tokens) > 1):
        if tokens[r+1] != "*" || tokens[r+1] != "/" || tokens[r+1] != "+" :
            l++ 
            r++
            continue

        operations.append(tokens[l] + tokens[r+1] + tokens[r]);
        tokens.remove(r)
        tokens.remove(r+1)
        tokens[l] = "x"


    lr, rr, op = 0, 0 , 0
    results = 0
    for i in operations: 
        lr = operations[i][0]
        op = operations[i][1]
        rr = operations[i][2]

        if lr == "x":
            lr = results

        if op == "+":
            result = lr + rr    

        elif op == "*":
    
            result = lr * rr
        elif op == "/":
            result = lr // rr
    
    return results
```

</details>

---

#### Logan Regueiferos (`70953`)

- **Severity: Minor Error**
- **Score:** 6/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 6 | PASS |
| example3 | 22 | 21 | FAIL |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | 2 | PASS |
| neg_divide | 3 | 3 | PASS |

<details>
<summary>Student Code (70953.py)</summary>

```python
def reversepolishnotation ( tokens ):
    stack = []
    i = 0
    while (i < len(tokens)):
        if (tokens[i] == "+"):
            stack.append(stack.pop() + stack.pop())
        elif (tokens[i] == "-"):
            temp = 0
            temp = stack.pop()
            stack.append(stack.pop() - temp)
        elif (tokens[i] == "*"):
            stack.append(stack.pop() * stack.pop())
        elif (tokens[i] == "/"):
            temp = 0
            temp = stack.pop()
            stack.append(stack.pop() / temp)
        else:
            stack.append(float(tokens[i]))
        i+=1
    return stack[0]
print(reversepolishnotation(["1","2","3","/","+"]))
```

</details>

---

#### Jason Seng (`77220`)

- **Severity: Critical Error**
- **Score:** 1/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 2 | FAIL |
| example2 | 6 | 4 | FAIL |
| example3 | 22 | 10 | FAIL |
| add_only | 7 | 3 | FAIL |
| single | 18 | 18 | PASS |
| subtract | 2 | 5 | FAIL |
| neg_divide | 3 | 7 | FAIL |

<details>
<summary>Student Code (77220.py)</summary>

```python
def exalRPN(tokens: List[str]):
    arr=[]
    
    for i in tokens:
        if i == "+":
            arr.append(arr.pop() + arr.pop())
        elif i == "*":
            arr.append(arr.pop() * arr.pop())
        elif i == "/":
            second = arr.pop()
            first = arr.pop()
            arr.append(int(first / second))
        elif i == "-":
            second = arr.pop()
            first = arr.pop()
            arr.append(first - second)
        else:
            arr.append(int(i))
        return arr[0]
```

</details>

---

#### Max Stehura (`80058`)

- **Severity: Critical Error**
- **Score:** 0/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | ERROR: TypeError: can't multiply sequence by no | FAIL |
| example2 | 6 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| example3 | 22 | ERROR: TypeError: can't multiply sequence by no | FAIL |
| add_only | 7 | 43 | FAIL |
| single | 18 | 18 | FAIL |
| subtract | 2 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| neg_divide | 3 | ERROR: TypeError: unsupported operand type(s) f | FAIL |

<details>
<summary>Student Code (80058.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i == "+":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x1 + x2
            stack.append(y)
        elif i == "-":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x2 - x1
            stack.append(y)
        elif i == "/":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x2 / x1
            stack.append(y)
        elif i == "*":
            x1 = stack.pop()
            x2 = stack.pop()
            y = x1 * x2
            stack.append(y)
        else:
            stack.append(i)
    return stack.pop()
```

</details>

---

#### Giankyle Vallarta (`70939`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 0 | FAIL |
| example2 | 6 | 0 | FAIL |
| example3 | 22 | 0 | FAIL |
| add_only | 7 | 0 | FAIL |
| single | 18 | 0 | FAIL |
| subtract | 2 | 0 | FAIL |
| neg_divide | 3 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Added missing colons
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def evalRPN(tokens): return 0`

</details>

<details>
<summary>Student Code (70939.java)</summary>

```java
evalRPN(String[]
 
tokens)
 
{
 
 
stack<Integers>
 
token2
 
=
 
new
 
Stack<>();
 
 
 
 
for
 
(String
 
x
 
:
 
tokens)
 
{
 
 
 
if
 
(x.equals("+"))
 
{
  
 
 
token2.push(token2.pop()
 
+
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("-"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one
 
-
 
two);
 
 
 
}
 
 
else
 
if
 
(x.equals("*"))
 
{
 
 
 
 
token2.push(token2.pop()
 
*
 
token2.pop());
 
 
 
}
 
 
else
 
if
 
(x.equals("/"))
 
{
 
 
 
 
int
 
two
 
=
 
token2.pop();
 
 
 
 
int
 
one
 
=
 
token2.pop();
 
 
 
 
token2.push(one/two);
 
 
}
 
}
 
 
 
return
 
token2.peek();
 
 
}
```

</details>

---

#### Kartik Wahlin (`75620`)

- **Severity: Critical Error**
- **Score:** 3/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 9 | 9 | PASS |
| example2 | 6 | 4 | FAIL |
| example3 | 22 | -198 | FAIL |
| add_only | 7 | 7 | PASS |
| single | 18 | 18 | PASS |
| subtract | 2 | -2 | FAIL |
| neg_divide | 3 | 0 | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Lowered keyword 'Return'

</details>

<details>
<summary>Student Code (75620.py)</summary>

```python
def evalRPN(tokens: List[str]) -> int:
    tack = []
    num1 = 0 
    num2 = 0
    for bench in tokens:
        if bench == “+”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1+num2)
        elif bench == “-”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1-num2)
        elif bench == “/”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack. append(num1/num2)
        elif bench == “*”:
            num1 = tack.pop()
            num2 = tack.pop()
            tack.append(num1*num2)
        else:
            tack.append(int(bench)) #if the element is not an operator, it can be cast to an int.
    return tack.pop()
#explanation on paper.
#Stack of encountered numbers - String array
#When we hit an operator, we condense the last 2 numbers into their result and add it back into the stack.
#repeat until end of array, where stack size = 1. Return int value.

#Edge cases are safe: min size is 1 and a valid arithmetic operation is guaranteed
```

</details>

---

### Guess Number Higher or Lower

#### Albert Chen (`78939`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>Student Code (78939.py)</summary>

```python
def guess (n:int) ->int:
    if (n==1):
        return 1
    left =1
    right = n
    middlePointer = (left+right)//2
    while (guess(middlePointer) !=0 and left<=right):
        if (guess(middlePointer) ==-1): #if our guess is too high we move the right pointer
            right = middlePointer -1
        if (guess(middlePointer) == 1): #if our guess is too high we move the left pointer
            left = middlePointer +1
        middlePointer = (left+right)//2
    return middlePointer
    
    
    #1,2 pick=2
#    left =2
#    right = 2
    #middlePointer = 2
```

</details>

---

#### Lilia Diusheyeva (`73721`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Student Code (73721.py)</summary>

```python
4: Fully understood, restated clearly

    Re-explained problem back to ensure all constraints were understood.
    Talked about the examples and how the output would reach that result.


2) Communication & Collaboration
    4: Very clear, structured, highly collaborative and adaptive

    Asked questions to clarify and explained why the sliding window approach was optimal for this problem.
    Asked for hints but starting thinking out loud how each hint led to the way to solution.


3) Implementation & Technical Depth
    2: Partially correct solution, basic or incomplete analysis
    
    Computed code and explained how time complexity resulted as O(n) by ensuring there were no duplicates however, multiple syntax errors found. Also, explained the use of two-pointer and how it would be implemented within the problem but did not fully implement correctly.


4) Team Fit & Working Style
    3: Positive teammate; receptive, steady, easy to work with

    Calm under questioning, good at communicating their thoughts, can be strong asset but a bit uncertain and lacks confidence. Could be more assertive about his ideas and points.


Final Evaluation
    13/16 Hire


Final Decision
    Reginald would be a good candidate for hire as he displayed a good amount of communication and was fully emersed into the problem through his questions and implementation of code. I believe he works well and fast under uncertainty. Despite, being a bit unsure of himself in the beginning, Reginald shows hard work and perseverance through his thinking and problem solving. Even with minor errors, I believe Reginald could do well within a team. 


Candidate Form: Guess Number Higher or Lower 

O log(n) 

def guessNumber(n: int) --> int:
    #initizalize the start and end of the range in guess
    start = 1
    end  = n

    #create while loop to search through while the guesses are valid
    while (start <= end):
        middle = start + (end - start) //2 #get the middle to avoid overflow

        #create statements for the various results
        if guess(middle) == 0:
            return middle #if guess equals 0 then it is the correct guess

        elif guess(middle) ==1:
            start = middle + 1 #guess is too low

        else: 
            end = middle - 1 #guess is too high

    return 0 #in case of fallback
```

</details>

---

#### Naman Kukreti (`75854`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>Student Code (75854.py)</summary>

```python
def guessnumber(num):
    #because pick is guarenteed to be in range, there's no need to check out of range/return -1 or not found
    L = 1
    R = num
    mid = (R+L)//2
    while(guess(mid) != 0):
        mid = (R+L)//2
        if(guess(mid) == -1):
            R = mid-1
        elif(guess(mid) == 1):
            L = mid + 1
    return mid
```

</details>

---

#### Matthew Park (`75927`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>Student Code (75927.py)</summary>

```python
#n is the highest possible number
#return the number that I picked
def guessNumber(n: int) -> int:
    low = 1
    high = n
    
    #loop until we find pick
    while high >= low:
        #set guess number to halfway
        mid = (high + low) // 2#don't worry about overflow in python
        #based on guess number, set low or high
        api_result = guess(mid)
        if api_result == 0:
            return mid
        if api_result == 1:
            low = mid + 1
        if api_result == -1:
            high = mid - 1
        
    return 0#should never reach this line of code - indicates an error


#time complexity: O(log n)
#space complexity: O(1)
#this algorithm uses a binary search, which has an O(log n) time complexity since it repeatedly cuts all possible values in half with each iteration of the loop.
#it uses a loop instead of a recursive call, which keeps the space complexity at O(1). The algorithm first assumes that pick can be any number from 1 to n and then
# shrinks the lower and upper bounds until it finds pick. Since n can be up to 2^31 -1, binary serach is required because an O(n) solution may continue to run for an extremely long time.
```

</details>

---

#### Parks Rpk (`65685`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Removed stray bracket at EOF

</details>

<details>
<summary>Student Code (65685.py)</summary>

```python
def guessNumber(n: int) -> int:
    l, r = 1, n                    
    while l <= r:                  
        mid = (l + r) // 2
        result = guess(mid)        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid
                                ]
```

</details>

---

#### Hewitt Wang (`70374`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>Student Code (70374.py)</summary>

```python
# -1 if the real number is lower
# 0 if the number is equal
# 1 if the real number is higher
# placeholder for testing
def guess(n: int) -> int:
    if (n == 42): return 0
    elif (n > 42): return -1
    else: return 1

def guessNumber(n: int) -> int:
    l = 1
    r = n
    
    while l <= r:
        mid = (l + r) // 2
        result = guess(mid)
        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid

    # no fallback case - we assume correctness

# testing
print(guessNumber(90))
```

</details>

---

#### Qianjun Zhou (`77691`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Removed trailing triple-quote

</details>

<details>
<summary>Student Code (77691.py)</summary>

```python
def guessNumber(n: int) -> int:
    min = 1
    max = n
    while True:
        currGuess = min + ((max - min) // 2)
        guessRet = guess(currGuess)
        if (guessRet == 1):
            min = currGuess + 1
        if (guessRet == -1):
            max = currGuess - 1
        if (guessRet == 0):
            return currGuess
"""
```

</details>

---

#### Santiago Zuluaga (`79862`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 6 | PASS |
| single | 1 | 1 | PASS |
| pick_low | 1 | 1 | PASS |
| pick_high | 2 | 2 | PASS |
| large | 73 | 73 | PASS |
| mid_range | 25 | 25 | PASS |
| pick_is_n | 20 | 20 | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Removed trailing semicolons
- [syntax-only] Removed stray bracket at EOF
- [syntax-only] Added missing colons

</details>

<details>
<summary>Student Code (79862.py)</summary>

```python
def guessNumber(n: int):
    
    start, end = 1, n


    while start <= end:
        
        pick = start + (end-start) // 2 
        
        if guess(pick) == 1:
            start = pick + 1

        elif guess(pick) == -1:
            end = pick - 1 

        else
            return pick; 
 
]
```

</details>

---

#### Gaven Chan (`69954`)

- **Severity: Critical Error**
- **Score:** 0/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |
| single | 1 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |
| pick_low | 1 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |
| pick_high | 2 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |
| large | 73 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |
| mid_range | 25 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |
| pick_is_n | 20 | ERROR: TypeError: make_guess.<locals>.guess() m | FAIL |

<details>
<summary>Student Code (69954.py)</summary>

```python
#-1 if its higher
#1 if its lower
#0 if equal 

#constraints x >= 1 
#guess() = some_number
#n is the upper limit 
#1, 2, 3, 4 ... n 
#n/2

def guessingGame(int n):
    lower = 1
    upper = n
    
    while(guess() != 0):
        middle = (upper + lower)/2
        if guess(middle) == 0:
            return middle
        
        if guess(middle) == -1:
            upper =  middle - 1
            
        if guess(middle) == 1:
            lower = middle + 1
```

</details>

---

#### William Connors (`78627`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 0 | FAIL |
| single | 1 | 0 | FAIL |
| pick_low | 1 | 0 | FAIL |
| pick_high | 2 | 0 | FAIL |
| large | 73 | 0 | FAIL |
| mid_range | 25 | 0 | FAIL |
| pick_is_n | 20 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

<details>
<summary>All syntax changes made</summary>

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Student Code (78627.py)</summary>

```python
def guessNumber (n: int) -> int:
        l, r = 0, n

        int guess (5)

        while l <= r:
                    mid = (1 + r) // 2
                    if nums [mid] == target:
                        return mid
                    elif nums [mid] < target:
                                l = mid + 1
                    else:
                            r = mid - 1

        return -1
```

</details>

---

#### Reginald Juance (`68931`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 0 | FAIL |
| single | 1 | 0 | FAIL |
| pick_low | 1 | 0 | FAIL |
| pick_high | 2 | 0 | FAIL |
| large | 73 | 0 | FAIL |
| mid_range | 25 | 0 | FAIL |
| pick_is_n | 20 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Lowered keyword 'While'
- [syntax-only] Fixed typo -> 'True'
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Student Code (68931.py)</summary>

```python
🙏Refer back to the Paired Technical Interview Print outs to the content you should submit.In general, you should submit at least a number and some notes for the interviewer side, and your full code solution for the Candidate.We encourage you to comment your code if you'd like!Reginald JuanceLilia DiusheveyaInterviewer Form[Problem Given] Guess Number Higher or Lower1) Problem Understanding: 4/4- Lilia understands the problem to a binary search immediately off of the bat- Ordered based on equal, greater than, or lower than- Understands all the constraints given to her (size restrictions)2) Communication & Collaboration: 2/4- While she explained some things throughout the problem, like her thought process and reasoning behind Binary Search, she failed to engage with interviewer clearly- At moments, she struggled to keep eye contact and social connections- Too focused on coding, forgot to explain her entire thought process through the UMPIRE method3) Implementation & Technical Depth: 4/4- Time complexity is O(log n) --> natural to binary search- Implementation is true and correct- Updates range effectively based on guesses4) Team Fit & Working Style: 3/4- Lilia is a positive personality when going through the interview process- She is incredibly receptive to hints, and is easy to work with- She will undoubtedly work well in any conditions that she facesFinal Evaluation- Score: 13/16- Hiring Recommendation: Lean HireFinal Decision- While Lilia is completely capable in implementing the question successfully, she falls short in the team aspect a hiring manager is looking for.She needs to learn to effectively communicate her thoughts when going through the interview process, or else this could raise concerns. However,throughout the interview, she was a positive person when acting under pressure and took into account any comments made. Her implementation was logically soundand ensured a complexity of O(log n)Candidate FormCode in Python:# Two pointer/sliding window problem for left pointer & hash set to prevent duplicates, ensures O(n) time complexity# Sliding window to optimize time complexity O(n)def lengthOfLongestSubstring(s: str) -> int: left = 0 # left pointer to start window max_length =  # maximum substring length, initialize it as 0 & update accordingly char_set = set() # ensures that string follows criteria regarding valid strings, and keeps track of unique/non-duplicate characters  for right in range(len(s): # right pointer for pointer   while s[right] in char_set: # remove invalid characters or duplicates   char_set.remove(s[left])   left = left + 1 # move left pointer over to slide   char_set.add(s[right]) # add the current char to the given set  max_length = max(max_length, right - left + 1) # new answer, accounting for current length  return max_length
```

</details>

---

#### Jordanny Ramos Rodriguez (`70834`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 0 | FAIL |
| single | 1 | 0 | FAIL |
| pick_low | 1 | 0 | FAIL |
| pick_high | 2 | 0 | FAIL |
| large | 73 | 0 | FAIL |
| mid_range | 25 | 0 | FAIL |
| pick_is_n | 20 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

<details>
<summary>All syntax changes made</summary>

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Student Code (70834.py)</summary>

```python
def guessNumber(n: int) -> int:left, right = 1, nwhile left =< right:mid = (left + right) // 2if guess(mid) == -1:right -
if guess(mid) == 1:left += 1else:return mid
```

</details>

---

#### Kevin Yang (`79336`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 0 | FAIL |
| single | 1 | 0 | FAIL |
| pick_low | 1 | 0 | FAIL |
| pick_high | 2 | 0 | FAIL |
| large | 73 | 0 | FAIL |
| mid_range | 25 | 0 | FAIL |
| pick_is_n | 20 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Fixed typo -> 'True'
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Student Code (79336.java)</summary>

```java
public int guessNumber(int n){
    int low = 1;
    int high = n;
    int middleNum = (int) n /2;
    while(true){
        if(guess(middleNum) == 0){ //Equals
            return middleNum;
        }else if(guess(middleNum) == -1){ //High
            high = middleNum;
        }else{//Low
            low = middleNum;
        }
        middleNum = (high - low) / 2 + low;
    }
}
```

</details>

---

#### Lilian Yuan (`75939`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | ERROR: UnboundLocalError: local variable 'guess | FAIL |
| single | 1 | ERROR: UnboundLocalError: local variable 'guess | FAIL |
| pick_low | 1 | ERROR: UnboundLocalError: local variable 'guess | FAIL |
| pick_high | 2 | ERROR: UnboundLocalError: local variable 'guess | FAIL |
| large | 73 | ERROR: UnboundLocalError: local variable 'guess | FAIL |
| mid_range | 25 | ERROR: UnboundLocalError: local variable 'guess | FAIL |
| pick_is_n | 20 | ERROR: UnboundLocalError: local variable 'guess | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers

</details>

<details>
<summary>Student Code (75939.java)</summary>

```java
public int guessNumber(int n){
    int min= 1;
    int max = n;

    while(min<=max){
        int pick = n/2;
        int guess = guess(pick);
        if(guess == -1){
            min = pick-1;
        }
        else if(guess == 1){
            max = pick;
        else{
            return pick;
        }
    }
    return 0;

}
```

</details>

---

#### Rijaa Zaidi (`67309`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| basic | 6 | 0 | FAIL |
| single | 1 | 0 | FAIL |
| pick_low | 1 | 0 | FAIL |
| pick_high | 2 | 0 | FAIL |
| large | 73 | 0 | FAIL |
| mid_range | 25 | 0 | FAIL |
| pick_is_n | 20 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Converted // comments to #
- [syntax-only] Converted // comments to #
- [syntax-only] Lowered keyword 'While'
- [syntax-only] Extracted function block from noisy file
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def guessNumber(n): return 0`

</details>

<details>
<summary>Student Code (67309.py)</summary>

```python
Date: 04/27/2026
Problem Given: Longest Substring Without Repeating Characters

Problem Understanding (0-4): 1
Notes: recognized sliding window pattern and hashset, required step by step assistance across all parts of the problem

Communication and Collaboration (0-4): 2
Notes: Didn't address the interviewer very much, thoughts were spoken in parts rather than a full sentence, I had to questions to understand the problem rather than being asked questions

Implementation and Technical Depth (0-4): 3
Notes: correct solution after heavy assistance

Team Fit and Working Style (0-4): 1
Notes: Took a few attempts to recieve feedback, spent a not insignificant amount of time on disliking sliding window

Total Score: 7/16
Hiring Reccomendation: No Hire

Final Decision (3-5 Sentences):
Strignths: Tianna didn't outright reject advice and was open to recieving new information. 
Weaknesses: That said, most of that information was about basic implementation and explaining how data structures worked, leaving little time for complexity analysis and discussion
Reasoning: While I appreciate that she's open to learn, it took a lot of time and help to get to the final solution. Lack of technical skill ultimately swayed me to no hire.


Leetcode Solution:
Rijaa Zaidi
Tianna Balkam

def guessNumber(n: int) -> int:
        //n is input, we want pick
        //binary search

        l,r = 1, n

        while l <= r:
                mid = (l + r) // 2
                if guess(mid) == 0:
                        return mid
                elif guess(mid) == 1:
                        l = mid + 1
                else:
                        r = mid - 1
        return 0


        Write-up:
        This solution uses binary search to cut down on the search range and find the solution in O(logn) time. by finding the middle value between l and r and adjusting each pointer based on the guess function output (increasing l if mid was less than pick and decreasing r if mid was greater than pick), the correct picked value will eventually found.
```

</details>

---

### Longest Substring Without Repeating Characters

#### Clare Calandra (`68530`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>Student Code (68530.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    set_of_chars = set() #create a HashSet to track chars (make sure no repeats)
    left = 0 #track elements (2-pointer method start left pointer at index 0)
    length = 0 #keep track of return value (start at 0)
    for i in range(len(s)): #iterate through the elements(characters) of the given string s 
        while s[i] in set_of_chars: # if the element is in the set, execute the following
            set_of_chars.remove(s[left]) #remove the character from the set 
            left += 1 #increment left pointer 
        set_of_chars.add(s[i]) #add the element back to set after removing duplicates  
        length = max(length, i - left + 1) # to return the correct length, take max 
        #of the current length and (the difference between the right and left pointer indices + 1)  
    return length #return the length of the string without duplicates 
# time complexity is O(n) because I utilized a HashSet and iterated through each element in the given string using # the two-pointer method (the left pointer starts at zero and increments by 1 to the right)
```

</details>

---

#### William Conroy (`67634`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>Student Code (67634.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:

    l = 0

    windowSum = 0

    h = set()

    for right in range(len(s)):
        while s[right] in h:
            h.remove(s[l])
            l += 1
        h.add(s[right])
        windowSum = max(windowSum, right - l + 1)

    return windowSum
```

</details>

---

#### Nicholas Friedlander (`67138`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Lowered keyword 'If'
- [syntax-only] Replaced em/en dashes with hyphens
- [syntax-only] Added missing colons

</details>

<details>
<summary>Student Code (67138.py)</summary>

```python
# I would achieve this problem by doing a dynamic sliding window solution
# Set and left and right integer
# Go through the string and update a variable with the longest substring length being equal to the window size
# If a letter of the substring is repeated the window would shift to the right
# Time complexity of O(n)

def lengthOfLongestSubstring(s: str) -> int: 
    left = 0
    longestLength = 0
    substringSet = set()
    for right in range(len(s)): 
        while s[right] in substringSet 
            substringSet.remove(s[left])
            left += 1
        substringSet.add(s[right])

        if (right – left + 1 > longestLength):
            longestLength = right – left + 1

    return longestLength
```

</details>

---

#### Samuel Halsband (`68358`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>Student Code (68358.py)</summary>

```python
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        maxLen = 0
        l = 0
        for r in range(0,len(s)):
            while (s[r] in s[l:r]):
                l+=1
            maxLen = max(maxLen,r-l+1)
        return maxLen
```

</details>

---

#### Jake Steck (`69296`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>Student Code (69296.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    result = 0
    length = len(s)
    left = 0
    
    for right in range(length):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result
```

</details>

---

#### Isabella Yang (`67686`)

- **PASS**
- **Score:** 8/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>Student Code (67686.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    left = maxLength = 0
    # right = 0
    stringSet = set()

    for right in range (len(s)):
        while s[right] in stringSet:
            stringSet.remove(s[left])
            left += 1

        stringSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength

# Approaching this problem using sliding window + set 
# The time complexity is O(n), even though there is a nested while loop, it's still in linear time since each character
# is added and removed at most once. The right pointer goes through everything and left goes through it n times
# The space complexity is O(min(n,k)) since  the memory usage depends on the smaller input of n, k
```

</details>

---

#### Tianna Balkam (`67581`)

- **Severity: Critical Error**
- **Score:** 1/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| all_same | 1 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| example3 | 3 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| all_unique | 6 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| spaces | 3 | ERROR: TypeError: unsupported operand type(s) f | FAIL |
| end_longest | 2 | ERROR: TypeError: unsupported operand type(s) f | FAIL |

<details>
<summary>Student Code (67581.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    count = 0
    seen = set()
    for r in range(len(s)):
        if s[r] in seen:
            seen.remove(s[l])
            left += 1
        seen.add(s[r])
        count = max(count, s[r] - s[l] + 1)
    return count
```

</details>

---

#### Carson Carey (`74510`)

- **Severity: Critical Error**
- **Score:** 1/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 0 | FAIL |
| all_same | 1 | 0 | FAIL |
| example3 | 3 | 0 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | 0 | FAIL |
| end_longest | 2 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Student Code (74510.java)</summary>

```java
//

public int lengthOfLongestSubstring(String s) {
    HashSet<Character> seen = new HashSet<Character>();
    int maxLength = 0;
    int l = 0;

    for(int r = 0; r<s.length(); r++) {
        while(seen.contains(s.charAt(r))) {
            seen.remove(s.charAt(l));
            l++;
        }
        seen.add(s.charAt(r));

        if(r-l+1>maxLength) {
            maxLength = r-l+1;
        }
    }
    return maxLength;
}
```

</details>

---

#### Shunyi Chen (`79105`)

- **Severity: Minor Error**
- **Score:** 6/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 3 | PASS |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 4 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 4 | FAIL |
| end_longest | 2 | 2 | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Replaced Unicode line separator

</details>

<details>
<summary>Student Code (79105.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int
    dict = {}
    right, left = 0, 0
    max = 0
    while right < len(s):
        if not s[right] in dict:
            dict[s[right]] = 0
            right+=1
            temp = right - left
            if temp > max:
                max = temp
        else:             left+=1
            del dict[s[left]]

    return max
```

</details>

---

#### Michael DiNapoli (`65542`)

- **Severity: Critical Error**
- **Score:** 1/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | ERROR: TypeError: '>' not supported between ins | FAIL |
| all_same | 1 | ERROR: TypeError: '>' not supported between ins | FAIL |
| example3 | 3 | ERROR: TypeError: '>' not supported between ins | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | ERROR: TypeError: '>' not supported between ins | FAIL |
| all_unique | 6 | ERROR: TypeError: '>' not supported between ins | FAIL |
| spaces | 3 | ERROR: TypeError: '>' not supported between ins | FAIL |
| end_longest | 2 | ERROR: TypeError: '>' not supported between ins | FAIL |

<details>
<summary>Student Code (65542.py)</summary>

```python
def lengthOfLongestSubstring(s):
    left = 0
    maxlength = 0
    substring = set()

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left+=1
        substring.add(s[right])
        maxlength = max(substring, right - left + 1)

    return maxlength

# Michael DiNapoli O(n^2)
```

</details>

---

#### Justin Gaston (`78797`)

- **Severity: Critical Error**
- **Score:** 1/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 0 | FAIL |
| all_same | 1 | 0 | FAIL |
| example3 | 3 | 0 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | 0 | FAIL |
| end_longest | 2 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Student Code (78797.java)</summary>

```java
public int lengthOfLongestSubstring(String s){
    String final = 0;
    int maxLength = 0;
    HashSet <String> hashSet = new HashSet<>();
    for(int i = 0; i< s.length; i++){
        hashSet.add(s.charAt(i);
        while(hashSet.contains(s.charAt(i)){
            if(final.length > maxLength){
                maxLength = final.Length;
            }
            hashSet.remove();
        }
        
    }
    return final.length;
}

//I do not think that I implimented this properly at all
//However my thought process was this:
//Add letters to hasset until I encounter a duplicates
//then while the hashSet isn't empty, remove the letters from the 
//hashSet and add them to a string, and save that strings length
//then when the while loop is done clear out the string and repeat the process
//until the string is exhausted
```

</details>

---

#### Jin Noh (`70971`)

- **Severity: Critical Error**
- **Score:** 1/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 0 | FAIL |
| all_same | 1 | 0 | FAIL |
| example3 | 3 | 0 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | 0 | FAIL |
| end_longest | 2 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Added missing colons
- [syntax-only] Appended 1 missing closing bracket(s)
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Student Code (70971.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:

    maxString = 0

    duplicate = {}

    left = 0
    
    for right in range(len(s.str)):

        window_sum += s.str [r]

        while left < len(s.str)
            window_sum == s.str[left
            left += 1

        if (s.substring(i) != (s.subtring[i+1]):
            maxString =+ 1

        elif (s.subtring(i) == s.subtring[i+1]):
            maxString =+ 1
            
            return (maxString)
```

</details>

---

#### Treyson Thelusma (`79860`)

- **Severity: Critical Error**
- **Score:** 1/8

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | ERROR: TimeoutError: exceeded 5s | FAIL |
| all_same | 1 | ERROR: TimeoutError: exceeded 5s | FAIL |
| example3 | 3 | ERROR: TimeoutError: exceeded 5s | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | ERROR: TimeoutError: exceeded 5s | FAIL |
| end_longest | 2 | ERROR: TimeoutError: exceeded 5s | FAIL |

<details>
<summary>Student Code (79860.py)</summary>

```python
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        max_length = 0
        length = 0
        seen = {}
        
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r    
                length = r - l + 1
                r += 1        
            else:
                max_length = max(max_length, length)
                l = seen[s[r]] + 1        
        return max_length
```

</details>

---

#### Dominic Vega (`66500`)

- **Severity: Critical Error**
- **Score:** 1/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 0 | FAIL |
| all_same | 1 | 0 | FAIL |
| example3 | 3 | 0 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | 0 | FAIL |
| end_longest | 2 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Extracted function block from noisy file
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Student Code (66500.py)</summary>

```python
# Dominic Vega

# Athulya Santhosh (Interviewer)

# Candidate Form

def lengthOfLongestSubstring(s: str) -> int:
    # init some variables
    letter_map = {}
    left_ptr = 0
    right_ptr = 0
    longest_sub = 0

    # empty string case
    if (str == ""): return 0

    # run through string, visiting each character once (O(n))
    for (right_ptr in range(len(str))):
        # what is the last time we saw this character? if it hasn't appeared, last_seen is None
        last_seen = letter_map.get(str[right_ptr])

        # if we've seen this character and the last time we saw it was in our window, adjust window
        if (last_seen != None and last_seen >= left_ptr):
            left_ptr = last_seen + 1
    
        # set the last time we've seen this letter to where it is right now
        letter_map[str[right_ptr]] = right_ptr
    
        # the longest substring is either what it currently is or the length of the current window
        longest_sub = max(longest_sub, right_ptr-left_ptr+1)

    #zhe returnne
    return longest_sub
```

</details>

---

#### Jiarong Zhang (`69558`)

- **Severity: Critical Error**
- **Score:** 1/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 0 | FAIL |
| all_same | 1 | 0 | FAIL |
| example3 | 3 | 0 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | 0 | FAIL |
| end_longest | 2 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Inserted `pass` into empty block at line 1
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Replaced || with or
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Inserted `pass` into empty block at line 1
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Student Code (69558.java)</summary>

```java
if(s.length() == 0){
        return 0;    
    }
    int maxLen = 1;
    int currLen = 1;
    HashSet<Character> set = new HashSet<>();
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i<s.length(); i++){
        char c = s.charAt(i);
        if(!set.contains(c)){
            sb.append(c);
            currLen++;
            set.add(c);
        }else{
            while(set.contains(c) || sb.length() > 0){
                char first = sb.charAt(0);
                set.remove(c);
            }
            currLen = 1;
            sb.append(c);
        }
        maxLen = Math.max(currLen, maxLen);
    }
    return maxLen;
```

</details>

---

#### Ryan Zhang (`75295`)

- **Severity: Minor Error**
- **Score:** 7/8
- **Not optimal:** Nested loops instead of sliding window

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 1 | FAIL |
| all_same | 1 | 1 | PASS |
| example3 | 3 | 3 | PASS |
| empty | 0 | 0 | PASS |
| single_char | 1 | 1 | PASS |
| all_unique | 6 | 6 | PASS |
| spaces | 3 | 3 | PASS |
| end_longest | 2 | 2 | PASS |

<details>
<summary>Student Code (75295.py)</summary>

```python
def lengthOfLongestSubstring(s: str) -> int:
    chars = set()
    max = 0
    left = 0

    for i in range(len(s)):
        while s[i] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[i])
        max = len(chars)
    return max

# I chose to create a hashset, which would only store unique characters in it. I defined a variable max for storing the max value, and left so that I could iterate through the string as sort of a sliding window. After iterating through everything, I returned the value stored in max. Should be O(n).
```

</details>

---

#### Christian Zuniga (`56934`)

- **Severity: Critical Error**
- **Score:** 1/8
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | 3 | 0 | FAIL |
| all_same | 1 | 0 | FAIL |
| example3 | 3 | 0 | FAIL |
| empty | 0 | 0 | PASS |
| single_char | 1 | 0 | FAIL |
| all_unique | 6 | 0 | FAIL |
| spaces | 3 | 0 | FAIL |
| end_longest | 2 | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Replaced || with or
- [syntax-only] Added missing colons
- [syntax-only] Removed C-style braces
- [syntax-only] Extracted function block from noisy file
- [syntax-only] Appended 1 missing closing bracket(s)
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def lengthOfLongestSubstring(s): return 0`

</details>

<details>
<summary>Student Code (56934.py)</summary>

```python
class Solution:

    def lengthofLongestSubstring(s:str) -> int:
        counter = 0
        visited = {}

        for x in s:
            #Base Case
            if (len(s) < 0 || len(s) > 50000){
                        return 0
            }

            if(s{x] != visited):
                counter = counter + 1
                s[x] = visited #Add visited string to the dict.

        return counter
```

</details>

---

### Merge Two Sorted Lists

#### Stephania Calin (`68729`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | [1, 1, 2, 3, 4, 4] | PASS |
| both_empty | [] | [] | PASS |
| one_empty | [0] | [0] | PASS |
| other_empty | [1] | [1] | PASS |
| interleave | [1, 2, 3, 4, 5, 6] | [1, 2, 3, 4, 5, 6] | PASS |
| all_same | [1, 1, 1, 1] | [1, 1, 1, 1] | PASS |
| single_each | [1, 2] | [1, 2] | PASS |

<details>
<summary>Student Code (68729.py)</summary>

```python
def mergeTwoLists(list1, list2): 
    # changed the function parameters because its easier for me to follow
        dummy = ListNode(0)
        current = dummy
    
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #now ill attach remaining list
        current.next = list1 if list1 else list2
    
        return dummy.next
```

</details>

---

#### Zhi Xiong Lu (`79884`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | [1, 1, 2, 3, 4, 4] | PASS |
| both_empty | [] | [] | PASS |
| one_empty | [0] | [0] | PASS |
| other_empty | [1] | [1] | PASS |
| interleave | [1, 2, 3, 4, 5, 6] | [1, 2, 3, 4, 5, 6] | PASS |
| all_same | [1, 1, 1, 1] | [1, 1, 1, 1] | PASS |
| single_each | [1, 2] | [1, 2] | PASS |

<details>
<summary>Student Code (79884.py)</summary>

```python
def mergeTwoLists(self, list1, list2):
        list3 = ListNode(0)
        current = list3

        while list1 and list2:
            
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                
            else:
                current.next = list2
                list2 = list2.next
                
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return list3.next
```

</details>

---

#### Ryan Tsui (`69792`)

- **PASS**
- **Score:** 7/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | [1, 1, 2, 3, 4, 4] | PASS |
| both_empty | [] | [] | PASS |
| one_empty | [0] | [0] | PASS |
| other_empty | [1] | [1] | PASS |
| interleave | [1, 2, 3, 4, 5, 6] | [1, 2, 3, 4, 5, 6] | PASS |
| all_same | [1, 1, 1, 1] | [1, 1, 1, 1] | PASS |
| single_each | [1, 2] | [1, 2] | PASS |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Lowered keyword 'Return'

</details>

<details>
<summary>Student Code (69792.py)</summary>

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #base cases so if these are none, I can just return the other list and save memory
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    #if the value of list1 is less than or equal to list 2, recursively call the function
    #Set list1.next to the merged result of the remaining nodes.
    #Return list1 as the current head.
    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    #do the same with list2
    else: 
        list2.next = self.mergeTwoLists(list2.next, list1)
        return list2
```

</details>

---

#### Alison Batz (`67454`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | 0 | FAIL |
| both_empty | [] | 0 | FAIL |
| one_empty | [0] | 0 | FAIL |
| other_empty | [1] | 0 | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | 0 | FAIL |
| all_same | [1, 1, 1, 1] | 0 | FAIL |
| single_each | [1, 2] | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed --> to ->
- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Fixed typo -> 'True'
- [syntax-only] Removed C-style braces
- [ambiguous] Conservative re-indent: normalized indent levels to 4-space tiers
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Student Code (67454.py)</summary>

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode] -> Optional[ListNode]:


        #Compare the two linked lists -- starting with head

        #insert based on smaller to larger value 

        #Linked List will vary in size --> Nodes already set up


        #Special Cases: Both can be empty

        current1 = new_node()
        current1 = list1   #don't lose track of the head

        current2 = new_node()
        current2 = list2  #don't lose track of the second head 

        #Third List (result linked list)

        current3 = new_node()
        current3 = list3 #new list (currently empty)



        while (current1 != NULL and current2 != NULL){   #while both conditions are true 

                if current1.val > current2.val:  #current1 greater than current2

                current2.next = current1
                current3.next = current2
                #add to list3  

                elif current2.val < current1.val:  #current2 less than current1
                    current1.next = current2
                    current3.next = current1
                                    #add to list3 


        return list3
```

</details>

---

#### Monica Gnajewski (`66827`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | 0 | FAIL |
| both_empty | [] | 0 | FAIL |
| one_empty | [0] | 0 | FAIL |
| other_empty | [1] | 0 | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | 0 | FAIL |
| all_same | [1, 1, 1, 1] | 0 | FAIL |
| single_each | [1, 2] | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Added missing colons
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Student Code (66827.py)</summary>

```python
mergeTwoLists(list1:
 
Optional[ListNode],
 
list2:
 
Optional[ListNode])
 
->
 
Optional[ListNode]:
 
 
newList
 
=
 
ListNode()
 
 
currNode
 
=
 
newList
  
 
while
 
list1
 
and
 
list2
 
!=
 
NULL:
 
 
 
if
 
list1.val
 
>
 
list2.val:
 
 
 
 
newList.next
 
=
 
list2
 
 
 
 
list2
 
=
 
list2.next
 
 
 
else:
 
 
 
 
newList.next
 
=
 
list1
 
 
 
 
list1
 
=
 
list1.next
 
 
 
 
currNode
 
=
 
currNode.next
 
 
 
 
if
 
list1:
 
 
 
 
currNode
 
=
 
list1.next
 
 
 
else:
 
 
 
 
currNode
 
=
 
list2.next
 
 
 
return
 
newList
```

</details>

---

#### Varun Karamchandani (`74406`)

- **Severity: Critical Error**
- **Score:** 0/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |
| both_empty | [] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |
| one_empty | [0] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |
| other_empty | [1] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |
| all_same | [1, 1, 1, 1] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |
| single_each | [1, 2] | ERROR: TypeError: ListNode.__init__() takes fro | FAIL |

<details>
<summary>Student Code (74406.py)</summary>

```python
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # attach whatever is left
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next
```

</details>

---

#### Vikram Minhas (`70844`)

- **Severity: Critical Error**
- **Score:** 1/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | [0, 1, 1, 2, 3, 4] | FAIL |
| both_empty | [] | [0] | FAIL |
| one_empty | [0] | [0] | PASS |
| other_empty | [1] | [0] | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | [0, 1, 2, 3, 4, 5] | FAIL |
| all_same | [1, 1, 1, 1] | [0, 1, 1] | FAIL |
| single_each | [1, 2] | [0, 1] | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Student Code (70844.py)</summary>

```python
Time complexity of my problem: O(n+m)
My solution goes through each of the lists completely and since the lists aren't identical, we have list1 of length n and list2 of length m. We compare each of the values and then go through until no more left to search and then return the head. We choose the head of the list that has a bigger value and then we move the pointer and keep repeating until the comparison is done. 


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> optional[ListNode]:
    x = listNode()
    curr = x

    while list1 and list2 != null:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        elif list1.val >= list2.val:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    return x
```

</details>

---

#### Kenneth Ng (`75928`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | 0 | FAIL |
| both_empty | [] | 0 | FAIL |
| one_empty | [0] | 0 | FAIL |
| other_empty | [1] | 0 | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | 0 | FAIL |
| all_same | [1, 1, 1, 1] | 0 | FAIL |
| single_each | [1, 2] | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Mechanical Java->Python transpile
- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Replaced && with and
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Student Code (75928.java)</summary>

```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode();
        ListNode current = head;

        while (list1 != null && list2 != null) {
                if (list1.value <= list2.value) {
                    current.next = list1;
                    list1 = list1.next;
                } else {
                    current.next = list2;
                    list2 = list2.next;
                }

                current = current.next;
        }
        current.next = list1 != null ? list1 : list2;

        return head.next;
}
```

</details>

---

#### Ian Porto (`78282`)

- **Severity: Critical Error**
- **Score:** 1/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | ERROR: TimeoutError: exceeded 5s | FAIL |
| both_empty | [] | ERROR: UnboundLocalError: local variable 'head' | FAIL |
| one_empty | [0] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| other_empty | [1] | [1] | PASS |
| interleave | [1, 2, 3, 4, 5, 6] | ERROR: TimeoutError: exceeded 5s | FAIL |
| all_same | [1, 1, 1, 1] | ERROR: TimeoutError: exceeded 5s | FAIL |
| single_each | [1, 2] | ERROR: AttributeError: 'NoneType' object has no | FAIL |

<details>
<summary>Student Code (78282.py)</summary>

```python
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #Initialize two nodes to step through list 1 and list 2
    cur1 = list1
    cur2 = list2


    #loop through list 1
    i = 0
    while cur1:
        i += 1 

        #Check to see if we have completed list2 or list1 is larger then just insert the next value of list1
        if (cur2 == None) or (cur1.next.val < cur2.val):

            #if current value is first then set the head
            if i == 1:
                head = cur1
            cur1 = cur1.next

        #insert next value of list2 into list1
        else:
            temp = cur2
            cur2.next = cur1.next
            cur1.next = cur2

            #if current value is first then set the head
            if i == 1:
                head = cur1

            cur2 = temp.next
            cur1 = cur1.next
    
    #if list1 ends before list2 then add list2 to the end
    if (cur2 != None):
        cur1.next = cur2

    return head
```

</details>

---

#### Athulya Santhosh (`77421`)

- **Severity: Critical Error**
- **Score:** 3/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| both_empty | [] | [] | PASS |
| one_empty | [0] | [0] | PASS |
| other_empty | [1] | [1] | PASS |
| interleave | [1, 2, 3, 4, 5, 6] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| all_same | [1, 1, 1, 1] | ERROR: TimeoutError: exceeded 5s | FAIL |
| single_each | [1, 2] | ERROR: AttributeError: 'NoneType' object has no | FAIL |

<details>
<summary>Student Code (77421.py)</summary>

```python
def mergeTwoList(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    curr1 = list1
    curr2 = list2
    if list1 == None and list2 == None:
        return None
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1
    while curr1 and curr2:
        if curr1.val <= curr2.val and curr1.next == None:
            curr1.next = curr2
            curr2 = curr2.next
        if curr1.val <= curr2.val and curr1.next != None and curr2.val < curr1.next.val:
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = temp
        curr1 = curr1.next
    return list1
```

</details>

---

#### Kathryn Schauber (`75705`)

- **Severity: Critical Error**
- **Score:** 3/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | ERROR: TimeoutError: exceeded 5s | FAIL |
| both_empty | [] | [] | PASS |
| one_empty | [0] | [0] | PASS |
| other_empty | [1] | [1] | PASS |
| interleave | [1, 2, 3, 4, 5, 6] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| all_same | [1, 1, 1, 1] | ERROR: TimeoutError: exceeded 5s | FAIL |
| single_each | [1, 2] | ERROR: AttributeError: 'NoneType' object has no | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Extracted function block from noisy file

</details>

<details>
<summary>Student Code (75705.py)</summary>

```python
Date: 5/6/26
Problem Given: Contains Duplicate Interviewer

Problem Understanding: Partial understanding, some clarification needed
Notes: took a long time to realize i and j were indices

Communication and Collaberation: Very Unclear, stuggled with feedback
Notes: when I asked her to explain why she was doing what she was doing, she would say she didn't know, when she finally did tho, she realized what she was doing wrong, and fixed Interviewer

Implementation and Technical Depth: Mostly correct, reasonable testing, correct complexity analysis
Notes: correct code. did not trace through super throughly. Correct time complexity analysis

Team fit and working style: Friction-heavy, resistant to feedback or collaboration
Notes: kept trying to hint towards hashmap, eventually she figured out it was a hashmap, but was resistant to switching to hashmap and sticking to a two pointer approach. did eventually switch to hashmap

Hiring Recommendation: No hire
Key strenghts was once she switched to hashmap she completed the solution quickly. Key weakness was communication and collaberation, was very resistant. I made my decision because of the communication.
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #will be ediiting list 1
    #head = list1
    #prev = temp value

    #while list2:
            #if val2 is than val1, set the next node to be the node in list1, update previous or head value if necessesary

    if not list1 and not list2:
            return None
    if not list1:
            return list2
    if not list2:
            return list1

    head = list1            #1 - 2- 4
    prev = None

    while list2 and list1:       
            if list2.val <= list1.val:               
                list2.next = list1                
                if prev is None:
                    head = list2                #1 -1 -2- 4
                    prev = list2
                else:
                    prev.next = list2
                    prev = prev.next
                    list2 = list2.next
            else:
                list1 = list1.next
                prev = prev.next


    while list2:
            prev.next = list2
            prev = prev.next

    return head



# The time complexity of my code is O(n) because it iterates through each loop at least once, say the length of list1 is n an list2 is m the time complexity would be O(n + m) which is the same as linear time and 0(n)
# The space complexity of my code is O(1) because no new objects are created therefore constant space is used
# My solution is a two pointer solution that updates list one based on the value of list2. if the value of list2 is less than or equal 2 my code updates the previous node to point to the list2 node and the list2 node points to the current list1 pointer. the list2 pointer is moved forward
# if list2 value is greater than the list 1 pointer the list 1 pointer is moved forward and the prev node is updated.
# basically it insterts the list2 nodes in the correct spot of list1

# My interviewer guided me a little with edge cases and other small errors, did not feel antagonized.
```

</details>

---

#### Gabriel Yang (`79975`)

- **Severity: Critical Error**
- **Score:** 1/7

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| both_empty | [] | [] | PASS |
| one_empty | [0] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| other_empty | [1] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| all_same | [1, 1, 1, 1] | ERROR: AttributeError: 'NoneType' object has no | FAIL |
| single_each | [1, 2] | ERROR: AttributeError: 'NoneType' object has no | FAIL |

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Lowered keyword 'If'

</details>

<details>
<summary>Student Code (79975.py)</summary>

```python
def mergeTwoLists(list1, list2):
    dummy = ListNode()

    curr = dummy
    while list1 or list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return dummy.next

#Iterates through both list nodes until one of them is empty, adding the lesser nodes to the new head node. If one is empty, just  #append the non-empty list onto the end of the new head.
```

</details>

---

#### Justin Yu (`78968`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | 0 | FAIL |
| both_empty | [] | 0 | FAIL |
| one_empty | [0] | 0 | FAIL |
| other_empty | [1] | 0 | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | 0 | FAIL |
| all_same | [1, 1, 1, 1] | 0 | FAIL |
| single_each | [1, 2] | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Extracted function block from noisy file
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Student Code (78968.py)</summary>

```python
# Time complexity O(n)

def mergeTwoList(list1, list2)
    my_node = None
    while list1.next != None and list2.next != None:
        if list1.val > list2.val:
            my_node.next = list1
            list1 = list1.next
            if list1 = None:
                my_node = list2.next
        else:
            my_node.next = list2
            list2 = list2.next
    return my_node
```

</details>

---

#### Vincent Zheng (`79930`)

- **Severity: Critical Error**
- **Score:** 0/7
- **Repair level:** aggressive

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| example1 | [1, 1, 2, 3, 4, 4] | 0 | FAIL |
| both_empty | [] | 0 | FAIL |
| one_empty | [0] | 0 | FAIL |
| other_empty | [1] | 0 | FAIL |
| interleave | [1, 2, 3, 4, 5, 6] | 0 | FAIL |
| all_same | [1, 1, 1, 1] | 0 | FAIL |
| single_each | [1, 2] | 0 | FAIL |

**Warning: potentially logic-affecting changes were applied:**

- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

<details>
<summary>All syntax changes made</summary>

- [syntax-only] Fixed typo -> 'None'
- [syntax-only] Removed trailing semicolons
- [syntax-only] Added missing colons
- [ambiguous] Aggressive re-indent: rebuilt block structure from control-flow headers
- [logic-affecting] Replaced unparseable code with stub `def mergeTwoLists(list1, list2): return 0`

</details>

<details>
<summary>Student Code (79930.py)</summary>

```python
def ListNode
mergeTwoList(ListNode list1, ListNode list2)


ListNode das = new LlistNode(
cur = das



while list1 and list2 not null:
list1.val
list2.val

if list1.val > list2.val
    current = list1.val;
```

</details>

---
