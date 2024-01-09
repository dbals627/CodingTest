function solution(n, numlist) {
  const result = numlist.filter((num) => num % n === 0);
  console.log(result);
}
solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]);
