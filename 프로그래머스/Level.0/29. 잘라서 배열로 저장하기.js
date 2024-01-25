function solution(my_str, n) {
  var answer = [];

  for (let i = 0; i < my_str.length; i += n) {
    answer.push(my_str.slice(i, i + n));
  }
  return answer;
}

solution('abc1Addfggg4556b', 6);

////// 다른 풀이
// match(문자열 메소드) : 정규식과 매치되는 부분 검색
function solution(my_str, n) {
  return my_str.match(new RegExp(`.{1,${n}}`, 'g'));
}
