function solution(n) {
  var answer = '';

  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      answer += '박';
    } else answer += '수';
  }

  return answer;
}

solution(3);

////// 다른 풀이
function solution(n) {
  return '수박'.repeat(n).slice(0, n);
}
