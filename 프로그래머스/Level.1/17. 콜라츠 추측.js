function solution(num) {
  for (let i = 0; i < 500; i++) {
    if (num != 1) {
      num = num % 2 === 0 ? num / 2 : num * 3 + 1;
    } else {
      return i;
    }
  }
  return -1;
}

solution(6);

/////다른 풀이

function collatz(num) {
  var answer = 0;

  while (num != 1 && answer != 500) {
    num % 2 == 0 ? (num = num / 2) : (num = num * 3 + 1);
    answer++;
  }

  return num == 1 ? answer : -1;
}
