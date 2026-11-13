---
date: '2021-10-18'
---

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for stone in stones:
            if stone in jewels:
                cnt += 1
        return cnt
```
