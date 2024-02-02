function solution(a, b) {
  var result = 0;

  for (let i = 0; i < a.length; i++) {
    result += a[i] * b[i];
  }

  return result;
}

solution([1, 2, 3, 4], [-3, -1, 0, 2]);

/////다른 풀이
function solution(a, b) {
  return a.reduce((acc, _, i) => (acc += a[i] * b[i]), 0);
}
