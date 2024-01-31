function solution(numbers) {
  const allNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  return allNum
    .map((v) => (numbers.includes(v) ? 0 : allNum.indexOf(v)))
    .reduce((acc, cur) => acc + cur, 0);
}

solution([1, 2, 3, 4, 6, 7, 8, 0]);

//////다른풀이
/// 전체합으로 푸니까 매우 간단해졌다..!!
function solution(numbers) {
  return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}
