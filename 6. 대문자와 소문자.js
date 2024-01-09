function solution(my_string) {
  const arr = [];
  for (let i = 0; i < my_string.length; i++) {
    if (my_string[i] === my_string[i].toUpperCase()) {
      arr.push(my_string[i].toLowerCase());
    } else if (my_string[i] === my_string[i].toLowerCase()) {
      arr.push(my_string[i].toUpperCase());
    }
  }
  //join(): 배열의 모든 요소를 하나의 문자열로 만듦
  return arr.join('');
}

console.log(solution('cccCCC'));
