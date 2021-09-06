
// 나의 풀이
function solution(x, n) {
    const result = []
    
    for (i = 1; i <= n; i++) {
      result.push(i * x)
    };
    return result
};


// 다른 사람 풀이

function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
