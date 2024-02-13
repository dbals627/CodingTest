function solution(arr, divisor) {
  var answer = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % divisor == 0) {
      answer.push(arr[i]);
    }
  }

  return answer.length == 0 ? [-1] : answer.sort((a, b) => a - b);
}

solution([2, 36, 1, 3], 1);
solution([3, 2, 6], 10);

/////// 다른 풀이
function solution(arr, divisor) {
  var answer = arr.filter((v) => v % divisor == 0);
  return answer.length == 0 ? [-1] : answer.sort((a, b) => a - b);
}
