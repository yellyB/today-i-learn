/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    const count=(num)=>{
        let sum = 0;
        while(num){
            sum += (num & 1);
            num = num >> 1;
        }
        return sum;
    }
    
    const sorting =(a, b)=>{
        const bitA = count(a);
        const bitB = count(b);
        if(bitA === bitB){
            if(a > b) return 1;
            if(a === b) return 0;
            if(a < b) return -1;
        }else{
            if(bitA > bitB) return 1;
            if(bitA === bitB) return 0;
            if(bitA < bitB) return -1;
        }
    }
    
    
    return arr.sort((a, b)=>sorting(a, b));
    
};
