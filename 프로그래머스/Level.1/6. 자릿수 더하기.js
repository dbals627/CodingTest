function solution(n) {
  return String(n)
    .split('')
    .map((v) => Number(v))
    .reduce((acc, cur) => acc + cur, 0);
}

solution(987);
