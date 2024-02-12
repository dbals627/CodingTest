function solution(s) {
  var split = s.split(' ');
  var result = [];

  for (let i = 0; i < split.length; i++) {
    result.push(
      split[i].charAt(0).toUpperCase() + split[i].slice(1).toLowerCase()
    );
  }
  console.log(result.join(' '));
}

solution('3people unFollowed me');

////// 다른 풀이
function solution(s) {
  return s
    .split(' ')
    .map((v) => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase())
    .join(' ');
}
