function solution(a, b) {
  var num = 0;

  if (a < b) {
    for (let i = a; i <= b; i++) {
      num += i;
    }
  } else if (a >= b) {
    for (let i = b; i <= a; i++) {
      num += i;
    }
  }

  return num;
}

solution(3, 5);

///// 다른 풀이
function solution(a, b) {
  var num = 0;

  for (var i = Math.min(a, b); i <= Math.max(a, b); i++) num += i;
  return num;
}
