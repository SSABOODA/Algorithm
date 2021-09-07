// 나의 풀이
function solution(n) {
  var num = String(n);
  var numReverse = num.split("").reverse().join("");
  // console.log(numReverse);
  
  var answer = [];
  var i = 0;
  for (i in numReverse) {
    // console.log(i);
    answer.push(parseInt(numReverse[i]));
  }
  return answer;
};

console.log(solution(12345))

// 나의 풀이 설명
// 1. 정수 n 을 문자열로 변환 후 구분자 없이 split 한다.
// 2. split 한 요소들을 reverse() 메서드로 뒤집는다.
// 3. 다시 문자열로 합친다.
// 4. 뒤집힌 문자열을 반복문을 통해 요소 하나하나를 정수로 변환 해 배열에 추가한다.
// 결론 : 1차원적인 풀이방법이다. 하지만 지금은 JS문법에 익숙하지 않으니 문법을 활용해서 풀기라도 하는 것에 만족한다.



// 다른 사람 풀이
function solution(n) {
  var arr = [];

    do {
        arr.push(n%10);
        n = Math.floor(n/10);
    } while (n>0);

    return arr;
}

console.log(solution(12345))

// 다른 사람 풀이 설명
// 1. do-while 반복문을 사용했다.
// 2. arr.push(n%10); 12345 % 10 = 5 이다 나머지를 구하는 연산자 %를 활용
// 3. n = Math.floor(n/10); 12345 / 10 = 1234.5 인데 이것의 정수만 남긴다. flloor를 활용
// 4. n = Math.floor(n/10); = 1234
// 5. 다시 위에 식을 반복 
// arr = [5]
// arr = [5, 4]
// arr = [5, 4, 3]
// arr = [5, 4, 3, 2]
// arr = [5, 4, 3, 2, 1]

// 다음과 같이 마지막에 정답이 출력되는 것을 볼 수 있다. 
// 결론 : 매우 수학적으로 접근했고 연산자의 활용을 잘한 것 같다.