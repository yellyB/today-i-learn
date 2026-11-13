class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0) return false;
        return !(n&(n-1));
    }
};

// 191. Number of 1 Bits 이거 응용한건데
// 이진수에 -1한걸 (원래값 & -1한값) 해서 계산하는거임
// 만약 1000(8)에서 1을 빼면 0111이 되잖? 둘을 &연산하면 1이됨
// 2의 제곱수라면 이진수중 단 한개만 1일테니 모든 2제곱수에 적용가능