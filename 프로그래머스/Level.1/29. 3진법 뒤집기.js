function solution(n) {
  // toString()은 10진수 => n진수로 변환 가능
  // parseInt(변환할 값, 진수)는 n진수 => 10진수로 변환 가능
  return parseInt(n.toString(3).split('').reverse().join(''), 3);
}

solution(45);
solution(125);

////// 다른 풀이
const solution = (n) => {
  return parseInt([...n.toString(3)].reverse().join(''), 3);
};
