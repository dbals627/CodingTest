function solution(n) {
  let length = n
    .toString(2)
    .split('')
    .filter((v) => v == 1).length;

  while (true) {
    n++;
    if (
      n
        .toString(2)
        .split('')
        .filter((v) => v == 1).length == length
    )
      return n;
  }
}

solution(78);
