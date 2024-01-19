function solution(my_string) {
  const array = my_string.replace(/[^0-9]/g, '');
  const sort = array.split('').sort((a, b) => a - b);
  const result = sort.map((e) => parseInt(e));
  return result;
}
solution('hi12392');

/////// 다른 풀이
function solution(my_string) {
  return my_string
    .match(/\d/g)
    .sort((a, b) => a - b)
    .map((n) => Number(n));
}

// String.prototype.match() 메서드는 정규 표현식과 매치되는
// 문자열의 일치 항목을 검색하고 배열로 반환한다.
// 전역 플래그 (g)를 사용하여 문자열 내에서 모든

// 정규 표현식은 \d는 숫자(digit)를 나타내는 정규 표현식 패턴이다.
// 따라서 /\d/g는 문자열에서 모든 숫자를 찾아내는 패턴을 의미한다.

// 숫자에 매치되는 모든 부분을 찾아 배열로 반환한다.
