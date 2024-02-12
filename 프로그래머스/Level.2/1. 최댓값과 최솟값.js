function solution(s) {
  var arr = s.split(' ');

  return String(Math.min(...arr)) + ' ' + String(Math.max(...arr));
}

solution('1 2 3 4');
