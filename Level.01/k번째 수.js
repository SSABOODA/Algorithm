// 2번째 시도 정답 o , 테스트 1개 실패
function solution(array, commands) {
    
    const answer = []
  
  for (const item of commands) {
    var slice_ary = array.slice(item[0]-1, item[1])
    slice_ary.sort();
    // console.log(slice_ary);
    var result = slice_ary[item[2]-1]
    
    answer.push(result)
  };
    return answer
};

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

// 2번째 시도 정답 o , 테스트 1개 실패
function solution(array, commands) {
    
  const answer = []

  
for (var i = 0; i < commands.length; i++) {
  // console.log(i);
  var slice_ary = array.slice(commands[i][0]-1, commands[i][1])
  slice_ary.sort()
  console.log(slice_ary);
  
  answer.push(slice_ary[commands[i][2]-1])

};
  return answer
};

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

// 정답 케이스
function solution(array, commands) { 
  var answer = []; 
  
  for(let i in commands) 
    answer.push(array.slice(commands[i][0] - 1, commands[i][1]).sort((a, b) => a - b)[commands[i][2] - 1]); 
  
  return answer; 
};

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

// sort함수를 사용할 때, sort()로만 작성하니 테스트케이스 2번이 실패가 떴다. 

// 찾아보니, sort( (a,b) => a - b)형태로 sort함수를 사용해야 통과였다.

// 원인은 sort()는 문자열을 정렬한다고 가정한다. 숫자를 정렬 할 때 기본 동작은 올바르게 정렬되지 않는다.

// 따라서 정수를 정렬할 때에는 위와같이 작성해줘야 한다.

 

