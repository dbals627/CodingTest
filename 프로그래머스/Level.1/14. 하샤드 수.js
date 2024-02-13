function solution(x) {
  return (
    x %
      String(x)
        .split('')
        .map((v) => Number(v))
        .reduce((acc, cur) => acc + cur, 0) ===
    0
  );
}

solution(12);

///////다른 풀이
function Harshad(n) {
  return !(n % (n + '').split('').reduce((a, b) => +b + +a));
}

// (n + "").split(""): 주어진 숫자 n을 문자열로 변환하고,
// split("") 메서드를 사용하여 각 자릿수를 분리한 배열로 변환
// reduce((a, b) => +b + +a ): 각 자릿수의 합을 계산
// +b와 +a는 각 자릿수를 숫자로 변환하여 합을 계산
