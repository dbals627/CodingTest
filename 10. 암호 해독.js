function solution(cipher, code) {
  // code의 배수만큼 반복문 돌려서 해당하는 문자를 빈 배열에 푸쉬 후 join

  // i + code 를 사용하면 i의 값이 계속 0이 되므로 무한루프에 빠지게 된다.
  // let sum = [];
  var answer = '';
  for (let i = code - 1; i < cipher.length; i += code) {
    // sum.push(cipher[i]);
    answer += cipher[i];
  }
  console.log(answer);
}

solution('pfqallllabwaoclk', 2);

// 문자이기 때문에 문자열에 계속 추가하는 것이 낫다!!
// 처음에 배열이랑 문자열 섞어씀..😅
