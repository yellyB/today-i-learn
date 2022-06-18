/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function(recipes, ingredients, supplies) {
    const res = [];
    let i = 0;
    while(i<ingredients.length){
        if(res.includes(recipes[i])){
            i ++;
            continue
        }
        if(!ingredients[i].every(ing => supplies.includes(ing))){
            i ++;
            continue
        }
        // 만들 수 있으면?
        res.push(recipes[i]);
        supplies.push(recipes[i]);
        i = 0;  // 처음으로 되돌아가 다시 확인
    }
    return res;
};
