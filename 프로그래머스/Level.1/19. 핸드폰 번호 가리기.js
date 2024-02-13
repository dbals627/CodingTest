function solution(phone_number) {
  var answer =
    phone_number.slice(0, -4).replace(/./g, '*') + phone_number.slice(-4);

  return answer;
}

solution('01033334444');
solution('027778888');

////// 다른 풀이

// repeat 함수! n번 반복
// 끝에 네자리를 빼고 변환해야 하기 때문에
// 문자열의 길이에서 4를 빼준다.
function solution(s) {
  var result = '*'.repeat(s.length - 4) + s.slice(-4);
  return result;
}
