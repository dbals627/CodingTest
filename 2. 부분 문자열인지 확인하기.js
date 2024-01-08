function solution(my_string, target) {
  //   if (my_string.includes(target)) {
  //     return 1;
  //   } else return 0;

  return my_string.includes(target) ? 1 : 0;
}

console.log(solution('banana', 'ana'));
console.log(solution('banana', 'wxyz'));
