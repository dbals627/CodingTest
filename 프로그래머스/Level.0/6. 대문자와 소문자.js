function solution(my_string) {
  const arr = [];
  for (let i = 0; i < my_string.length; i++) {
    if (my_string[i] === my_string[i].toUpperCase()) {
      arr.push(my_string[i].toLowerCase());
    } else if (my_string[i] === my_string[i].toLowerCase()) {
      arr.push(my_string[i].toUpperCase());
    }
  }
  return arr.join('');
}

console.log(solution('ccccCCC'));
