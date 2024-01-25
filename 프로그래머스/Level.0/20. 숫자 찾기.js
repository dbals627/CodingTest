function solution(num, k) {
  return (
    num
      .toString()
      .split('')
      .map((e) => Number(e))
      .indexOf(k) + 1 || -1
  );
}

solution(232443, 4);

// 숫자를 문자로 변환 후 쪼개서 배열로 반환
// map으로 배열 순회 후 인덱스 찾아서 반환

///// 다른 풀이
function solution(num, k) {
  var answer = num.toString();
  if (answer.includes(k)) {
    return answer.indexOf(k) + 1;
  } else {
    return -1;
  }
}
