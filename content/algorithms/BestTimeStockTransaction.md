---
date: '2021-10-27'
---

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, buy1 = -prices[0], -prices[0]
        sell, sell1 = 0, 0
        for i in range(len(prices)):
            todayPrice = prices[i]
            buy = max(buy1, sell1 - todayPrice)  # 어제 산, 어제 판 + 오늘가격
            sell = max(sell1, todayPrice + buy1 - fee)  # 어제 판, 오늘가격 - 어제 산 - 요금
            buy1, sell1 = buy, sell
        return sell

    # 팔 때 fee 계산하는 것으로
    # 어제 - 오늘 비교해서 계산
    # buy : 어제의 buy, 어제 sell 하고난거에 오늘가격 buy
    # sell :  어제의 sell, 어제 buy 하고난거에 오늘가격으로 sell
```

```javascript
/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {
    // 0: 어제의 결과 / 1: 오늘 /  팔고살때마다 오늘은 어제로 미뤄줄거임
    let buy0 = -prices[0], buy1 = -prices[0];  // 처음에는 이미 산걸로 가정하니까 [0]가격만큼 지불해야함
    let sell0 = 0, sell1 = 0;
    for(const price of prices){
        buy1 = Math.max(buy0, sell0 - price);  // 오늘의 구매현황: 어제구매가격 vs 어제팔고 오늘 구매
        sell1 = Math.max(sell0, buy0 + price - fee);  // 오늘의 판매: 어제 판 vs 어제사고 오늘팔아(이익실현) + 요금내기
        
        // 오늘가격 어제로 미룸
        buy0 = buy1;
        sell0 = sell1;
    }
    return sell1;  // 최종 상태는 buy한 상태일수 없으니 sell 리턴
};
```
