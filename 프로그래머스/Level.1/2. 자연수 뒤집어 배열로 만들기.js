function solution(n) {
  return n
    .toString()
    .split('')
    .reverse()
    .map((v) => parseInt(v));
}

solution(12345);
