function solution(my_string) {
  const numArr = my_string.match(/\d+/gi, '');
  const res = numArr
    ? numArr.map((v) => Number(v)).reduce((acc, cur) => acc + cur, 0)
    : 0;
  console.log(numArr);
  // 제한사항 잘보기...^^
}
solution('aAb1B2cC34oO');

/////다른풀이
function solution(my_string) {
  console.log(
    my_string.split(/\D+/).reduce((acc, cur) => acc + Number(cur), 0)
  );
}
