---
date: '2022-01-03'
---

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = 0
        for i in range(len(arr)):
            xor = arr[i]
            for j in range(i+1, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    cnt += j-i
        return cnt
```

```cpp
class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int cnt = 0;
        for (int i = 0; i < arr.size(); i++){
            int xorVal = arr[i];
            for (int j = i+1; j < arr.size(); j++){
                xorVal ^= arr[j];
                if (xorVal == 0){
                    cnt += j-i;
                }
            }
        }

        return cnt;
    }
};
```
