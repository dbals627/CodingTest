function solution(x, n) {
  var answer = [];

  for (let i = 1; i <= n; i++) {
    answer.push(i * x);
  }

  return answer;
}

///// 다른풀이
function solution(x, n) {
  return Array(n)
    .fill(x)
    .map((v, i) => (i + 1) * v);
}

solution(2, 5);
