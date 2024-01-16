function solution(my_string) {
  const result = my_string
    // 정규식
    .replace(/[^0-9]/g, '')
    .split('')
    .reduce((acc, curr) => acc + Number(curr), 0);

  console.log(result);
}

solution('aAb1B2cC34oOp');
