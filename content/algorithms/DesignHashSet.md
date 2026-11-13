---
date: '2023-02-18'
---

```python
class MyHashSet:

    def __init__(self):
        self.hash = []
        

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.hash
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

```javascript
var MyHashSet = function() {
    this.hash = [];
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
    if(!this.hash.includes(key)){
        this.hash.push(key)
    }
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
    if(!this.hash.includes(key)) return;
    this.hash = this.hash.filter((item)=>item!==key)
};

/** 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
  return this.hash.includes(key)  
};

/** 
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
```
