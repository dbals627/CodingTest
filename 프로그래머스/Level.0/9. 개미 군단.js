function solution(hp) {
  const FirstAnt = Math.floor(hp / 5);
  const SecondAnt = Math.floor((hp % 5) / 3);
  const ThirdAnt = Math.floor(((hp % 5) % 3) / 1);

  const result = FirstAnt + SecondAnt + ThirdAnt;
  console.log('결과', result);
}

solution(999);
