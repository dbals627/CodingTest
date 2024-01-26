function solution(before, after) {
  // reverse로 순서바꿔준다음 join()
  // const res = before.split('').reverse().join('') === after ? 1 : 0;

  const res =
    before.split('').sort().join('') === after.split('').sort().join('')
      ? 1
      : 0;
  console.log(res);
}
solution('olleh', 'hello');
