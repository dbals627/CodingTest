function solution(emergency) {
  // 내림차순
  // [ 100, 30, 23, 10, 6 ]
  let sorted = emergency.slice().sort((a, b) => b - a);
  return emergency.map((v) => sorted.indexOf(v) + 1);
  // slice 로 기존 배열을 복사해서 새 배열을 만든다.
}

solution([30, 10, 23, 6, 100]);

///// 얕은 복사!!!!!!!
/// ...emergency, slice
