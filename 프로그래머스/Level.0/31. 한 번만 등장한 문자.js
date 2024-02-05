function solution(s) {
  var answer = '';

  for (let i = 0; i < s.length; i++) {
    if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) {
      answer += s[i];
    }
  }

  console.log(answer.split('').sort().join(''));
}

solution('hello');
