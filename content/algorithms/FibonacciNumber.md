---
date: '2021-10-18'
---

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0

        return self.fib(n - 1) + self.fib(n - 2)
```
