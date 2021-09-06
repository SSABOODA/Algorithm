// 나의 풀이

function solution(arr) {
    var min_num = Math.min.apply(null, arr);
    // console.log(min_num);
    const idx = arr.indexOf(min_num) 
    
    if (idx > -1) arr.splice(idx, 1)
      
    
    if (arr.length < 2) {
      return [-1]
    }
    
    return arr;
  };

// 다른 사람 풀이

function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)),1);
    if(arr.length<1)return[-1];
    return arr;
}

// 여러 줄로 작성했던 코드를 한줄로 풀어냈다..

// 사용된 문법
// 1. ...문법
// 2. splice
// 3. indexOf