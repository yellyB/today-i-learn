---
date: '2022-03-11'
---

```python
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
```
