---
date: '2022-04-05'
---

```python
class Trie:

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        for t in self.trie:
            if t == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for t in self.trie:
            if prefix == t[:len(prefix)]:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

```javascript

var Trie = function() {
    this.trie = [];
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    this.trie.push(word);
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    for(const t of this.trie){
        if(t == word) return true;
    }
    return false;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    for(const t of this.trie){
        if(prefix == t.slice(0, prefix.length)) return true;
    }
    return false;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```
