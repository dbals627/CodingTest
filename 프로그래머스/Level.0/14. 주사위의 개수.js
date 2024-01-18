///////// 나의 풀이
function solution(box, n) {
  let result = 1;
  for (let i = 0; i < box.length; i++) {
    let num = Math.floor(box[i] / n);
    result *= num;
  }
  console.log(result);
  return result;
}

solution([10, 8, 6], 3);

// box의 길이가 정해져 있기 때문에 반복문을 돌리는 것은 비효율적이다.

//////// 다른 풀이
function solution(box, n) {
  return (
    Math.floor(box[0] / n) * Math.floor(box[1] / n) * Math.floor(box[2] / n)
  );
}

// 박스의 각 요소들을 n으로 나눠 준다.
