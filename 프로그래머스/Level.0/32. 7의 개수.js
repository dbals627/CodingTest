function solution(array) {
  var answer = 0;
  var str = array.join(''); // 문자열

  for (let i = 0; i < str.length; i++) {
    if (str[i] == 7) {
      answer += 1;
    }
  }
  console.log(answer);
}

solution([7, 77, 17]);

////// 다른 풀이
function solution(array) {
  console.log(array.join('').split('7').length - 1);
}
