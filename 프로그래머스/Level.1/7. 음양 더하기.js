function solution(absolutes, signs) {
  var newAbs = [];

  for (let i = 0; i < absolutes.length; i++) {
    if (signs[i] === true) {
      newAbs.push(absolutes[i]);
    } else if (signs[i] === false) {
      newAbs.push(absolutes[i] * -1);
    }
  }

  return newAbs.reduce((acc, cur) => acc + cur, 0);
}
solution([4, 7, 12], [true, false, true]);

////// 다른 풀이
function solution(absolutes, signs) {
  return absolutes.reduce((acc, val, i) => acc + val * (signs[i] ? 1 : -1), 0);
}
