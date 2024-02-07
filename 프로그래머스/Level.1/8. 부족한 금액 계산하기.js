function solution(price, money, count) {
  const arr = [];

  while (0 < count) {
    arr.push(price * count);
    count--;
  }

  const res = arr.reduce((acc, cur) => acc + cur, 0);

  return res - money < 0 ? 0 : res - money;
}

solution(3, 20, 4);

///////다른 풀이

function solution(price, money, count) {
  let answer = 0;

  for (let i = 1; i <= count; i++) {
    answer += price * i;
  }

  return answer > money ? answer - money : 0;
}
