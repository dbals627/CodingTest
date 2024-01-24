function solution(my_string) {
  return my_string
    .split('')
    .filter((el, index, arr) => arr.indexOf(el) === index)
    .join('');
}
solution('We are the world');

// indexOf() 메서드는 특정 요소가 배열 내에서 **처음**으로 등장하는 인덱스를 반환
// filter() 메서드는 콜백 함수를 이용하여 조건에 맞는 요소만 추출한 배열을 반환

///// 다른 풀이
function solution(my_string) {
  return [...new Set(my_string)].join('');
  // console.log([...new Set(my_string)].join(''));
}
solution('We are the world');

// my_string을 이용하여 Set 객체를 생성한다.
// 문자열을 이터러블 객체로 변환하기 위해 스프레드 연산자(...)를 사용한다.
// Set 객체는 중복된 값들을 제거하고 유일한 값들만 남긴다.
// Set 객체를 다시 배열로 변환하고, join('') 메서드를 사용하여 배열의 각 요소를
// 빈 문자열로 연결하여 새로운 문자열을 생성한다.
