function solution(s) {
  return s
    .split(' ')
    .map((word) =>
      word
        .split('')
        .map((char, idx) => (idx % 2 === 0 ? char.toUpperCase() : char))
        .join('')
    )
    .join(' ');
}

solution('try hello world');

// 하나 이상의 공백문자
// 짝수번째 알파벳은 대문자
// 홀수번째 알파벳은 소문자
