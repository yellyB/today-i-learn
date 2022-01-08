function generate(numRows: number): number[][] {
    const answer = [[1]]

    for (let i=1; i<numRows; i++){
        const temp = []
        temp.push(1)
        for (let j=1; j<i; j++){
            temp.push(answer[i-1][j-1] + answer[i-1][j])
        }
        temp.push(1)
        answer.push(temp)
    }
    return answer
};