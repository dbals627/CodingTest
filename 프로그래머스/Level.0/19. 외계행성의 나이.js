function solution(age) {
  var alphabets = 'abcdefghij';
  var result = '';
  var stringAge = age.toString();

  for (let i = 0; i < stringAge.length; i++) {
    result += alphabets[stringAge[i]];
  }
  console.log(result);
}

solution(100);

///// 다른 풀이
function solution(age) {
  return age
    .toString()
    .split('')
    .map((v) => 'abcdefghij'[v])
    .join('');
}

// age 숫자를 문자열로 변환
// 문자열을 쪼갠 후 배열로 반환 [1,0,0]
// 배열을 순회해서 문자열에 맞는 인덱스로 반환 [b,a,a]
// 다시 합친 후 문자열로 반환
