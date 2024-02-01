function solution(array, n) {
  let answer = [];

  array.sort((a, b) => a - b).map((v) => answer.push(Math.abs(v - n)));
  let res = array[answer.indexOf(Math.min(...answer))];
  console.log(res);
}

solution([3, 10, 28], 20);
