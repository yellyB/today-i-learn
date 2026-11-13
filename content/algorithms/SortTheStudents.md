---
date: '2023-02-08'
---

```python
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x:-x[k])
```

```javascript
function sortTheStudents(score: number[][], k: number): number[][] {
    return score.sort((a,b)=>b[k]-a[k])
};
```
