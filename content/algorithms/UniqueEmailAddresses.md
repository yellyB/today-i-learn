---
date: '2022-08-02'
---

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        confirmed = set()
        for email in emails:
            splited = email.split('@')
            splitedWithPlus = splited[0].split('+')[0]
            confirmed.add(splitedWithPlus.replace('.','')+'@'+splited[-1])
            
        return len(confirmed)
```

```javascript
/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const confirmed = emails.map((email)=>{
        let splited = email.split('@');
        return splited[0].split('+')[0].replace(/\./g, '') + '@' + splited[splited.length-1];
    });
    
    return [...new Set(confirmed)].length;
};
```
