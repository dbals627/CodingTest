function solution(left, right) {
  let answer = 0;

  for (let i = left; i <= right; i++) {
    let count = 0;
    for (let j = 1; j <= i; j++) {
      if (i % j == 0) count++;
    }

    if (count % 2 === 0) {
      answer += i;
    } else answer -= i;
  }

  return answer;
}

solution(13, 17);

/////// 다른 풀이
function solution(left, right) {
  var answer = 0;

  for (let i = left; i <= right; i++) {
    // Number.isInteger : 정수인지 판별
    // 제곱근이 정수면 약수의 개수는 홀수!!
    if (Number.isInteger(Math.sqrt(i))) {
      answer -= i;
    } else {
      answer += i;
    }
  }
  return answer;
}
