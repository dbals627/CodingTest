function solution(s) {
  return (s.length === 4 || s.length === 6) && !isNaN(s) ? true : false;
}

solution('a234');

////// 다른 풀이
function solution(s) {
  return (s.length === 4 || s.length === 6) && s == parseInt(s);
}
