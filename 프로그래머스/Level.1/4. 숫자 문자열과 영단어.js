function solution(s) {
  s = s
    .replace(/zero/g, '0')
    .replace(/one/g, '1')
    .replace(/two/g, '2')
    .replace(/three/g, '3')
    .replace(/four/g, '4')
    .replace(/five/g, '5')
    .replace(/six/g, '6')
    .replace(/seven/g, '7')
    .replace(/eight/g, '8')
    .replace(/nine/g, '9');

  console.log(Number(s));
}

// replace : 새로운 문자열 생성

solution('2three45sixseven');

///// 다른 풀이
function solution(s) {
  let numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];
  var answer = s;

  // s를 새로운 변수에 복사한 후
  // 반복문을 돌려 배열을 인덱스를 기준으로 자른다.
  // 그 후 배열을 다시 인덱스를 기준으로 합쳐 문자열로 만든다.
  for (let i = 0; i < numbers.length; i++) {
    let arr = answer.split(numbers[i]);
    answer = arr.join(i);
  }

  return Number(answer);
}
