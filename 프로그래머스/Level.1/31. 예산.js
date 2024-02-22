function solution(d, budget) {
  d.sort((a, b) => a - b);

  while (d.reduce((acc, cur) => acc + cur, 0) > budget) d.pop();

  return d.length;
}

solution([1, 3, 2, 5, 4], 9);

////// 다른풀이

function solution(d, budget) {
  return d
    .sort((a, b) => a - b) // [1,2,3,4,5]
    .reduce((count, price) => {
      return count + ((budget -= price) >= 0);
      // 9 - 1 = 8 은 0보다 크기 때문에(true = 1) count를 1증가 (1)
      // 8 - 2 = 6 은 0보다 크기 때문에 count 1증가 (2)
      // 6 - 3 = 3 은 0보다 크기 때문에 count 1증가 (3)
      // 3 - 4 = -1 은 0보다 작기 때문에 증가 x
      // -1 -5 도 마찬가지
      // 따라서 count는 3
    }, 0);
}
