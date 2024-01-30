function solution(i, j, k) {
  var answer = '';
  for (i; i <= j; i++) {
    answer += i;
  }

  console.log(answer.split(k).length - 1);
}

solution(10, 50, 5);
