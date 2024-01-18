function solution(n) {
  // 초기값은 피자 한판
  let pizza = 1;
  // 피자한판은 6개의 조각으로 이루어진다.
  // 이 조각들을 n으로 나누면 모두 똑같은 조각을 먹게된다.

  // 정확한 범위를 알지 못할 때는 while문을 쓰자!
  while ((pizza * 6) % n) {
    pizza++;
  }
  console.log(pizza);
}

solution(4);
