//첫 번째 줄에 자연수 n을 입력받고, 그 다음줄에 공백으로 구분된 n개의 값들을 입력받을 때
// let fs = require("fs");
// let input = fs.readFileSync('./dev/stdin')
//     .toString()
//     .trim()
//     .split("\n");
// let arr = input
//     .slice(1, input.length)
//     .map((el) => el.split(" ").map((el) => Number(el)));
let N=9;
let arr=[N][N];
arr=[[0,0,0,1,1,1,-1,-1,-1],[0,0,0,1,1,1,-1,-1,-1],
    [0,0,0,1,1,1,-1,-1,-1],[1,1,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0],[0,1,-1,0,1,-1,0,1,-1],[0,-1,1,0,-1,1,0,-1,1],[0,1,-1,1,0,-1,0,1,-1]];

function solution(arr){
    const isBelowThreshold = (currentValue) => currentValue === 0;
    const t=[-1,0,1];
    for(i in t){
        i
    }

    console.log(arr.every(isBelowThreshold));
}


console.log(arr)
solution(arr)