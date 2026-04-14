```ts
# 3740. Minimum Distance Between Three Equal Elements I
# TypeScript solution
function minimumDistance(nums: number[]): number {
const lastSeen = new Map<number, number[]>();
let minDistance = Infinity;

for (let i = 0; i < nums.length; i++) {:
    const num = nums[i];

    if (!lastSeen.has(num)) {:
        lastSeen.set(num, [i]);
        continue;
    }

    const seen = lastSeen.get(num)! as [number, number];
    if (seen.length !== 2) {:
        lastSeen.set(num, [seen[0], i]);
        continue;
    }

    const [j, k] = seen;
    const distance = Math.abs(i - j) + Math.abs(j - k) + Math.abs(k - i);
    minDistance = Math.min(distance, minDistance);

    lastSeen.set(num, [k, i]);
    }

    return minDistance === Infinity ? -1 : minDistance;
};
```

My solution has O(n) time complexity because it loops through `nums` once and O(n) space complexity because it uses a hashmap of all previously seen numbers. It works by going through `nums` and checking if it's been seen twice previously; if it hasn't, then store it in the hashmap. If it has, compute the distance of the 3 indices (the current and the 2 stored indices) and store that in `minDistance`. Then, replace the oldest index in the "previously seen" hashmap with the current index, since the furthest index can't possibly produce a smaller distance in the future.